import argparse
import json
import re
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text or "untitled"


def generate_description(content: str) -> str:
    plain = re.sub(r"<[^>]+>", "", content)
    plain = re.sub(r"\s+", " ", plain).strip()
    return plain[:100] + "..." if len(plain) > 100 else plain


def generate_tags(content: str) -> list[str]:
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    tags = list(dict.fromkeys(word for word in words if len(word) > 1))
    return tags[:5]


def parse_notion_content(md_content: str) -> str:
    lines = md_content.splitlines()
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith("### "):
            new_lines.append(f"<h3>{line[4:]}</h3>")
            i += 1
            continue
        if line.startswith("## "):
            new_lines.append(f"<h2>{line[3:]}</h2>")
            i += 1
            continue
        if line.startswith("# "):
            new_lines.append(f"<h1>{line[2:]}</h1>")
            i += 1
            continue
        if line == "---":
            new_lines.append("<hr>")
            i += 1
            continue

        if "|" in line:
            table_rows = []
            while i < len(lines) and "|" in lines[i]:
                row = [cell.strip() for cell in lines[i].split("|")[1:-1]]
                table_rows.append(row)
                i += 1
            if table_rows:
                table_html = ['<table class="table-card">', "<thead>"]
                table_html.append("<tr>" + "".join(f"<th>{h}</th>" for h in table_rows[0]) + "</tr>")
                table_html.append("</thead><tbody>")
                for row in table_rows[1:]:
                    table_html.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
                table_html.append("</tbody></table>")
                new_lines.append("\n".join(table_html))
            continue

        if line:
            new_lines.append(f"<p>{line}</p>")
        i += 1

    return "\n".join(new_lines)


def normalise_categories(raw_categories) -> list[str]:
    if isinstance(raw_categories, list):
        return [str(cat).strip() for cat in raw_categories if str(cat).strip()]
    if isinstance(raw_categories, str) and raw_categories.strip():
        return [raw_categories.strip()]
    return ["content-strategy"]


def build_post(page: dict) -> tuple[str, str]:
    title = str(page.get("title", "")).strip()
    if not title:
        raise ValueError("Each page must include a title.")

    categories = normalise_categories(page.get("categories"))
    raw_content = str(page.get("content", "")).strip()
    content_parsed = parse_notion_content(raw_content)
    description = str(page.get("description") or generate_description(content_parsed))
    tags = page.get("tags") or generate_tags(content_parsed)
    permalink = page.get("permalink") or f"/articles/{slugify(title)}/"

    date_value = page.get("date")
    if date_value:
        date_obj = datetime.fromisoformat(str(date_value))
    else:
        date_obj = datetime.today()
    date_str = date_obj.strftime("%Y-%m-%d")

    front_matter = f"""---
layout: post
title: "{title}"
date: {date_str}
last_modified_at: {date_str}
lang: zh-TW
description: "{description}"
categories: {categories}
tags: {tags}
permalink: {permalink}
image: /assets/images/og-default.jpg
---
"""

    body = f"""
<section class="card-section">
{content_parsed}
</section>
"""

    filename = f"{date_str}-{slugify(title)}.md"
    return filename, front_matter + body.lstrip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert exported Notion content JSON into Jekyll posts without touching git."
    )
    parser.add_argument("input", help="Path to a JSON file containing a list of pages.")
    parser.add_argument(
        "--output-dir",
        default="_posts",
        help="Directory for generated markdown files. Defaults to _posts.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Actually write files. Without this flag the script runs in dry-run mode.",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    pages = payload if isinstance(payload, list) else payload.get("pages", [])

    if not pages:
        raise ValueError("Input JSON did not contain any pages.")

    generated = [build_post(page) for page in pages]

    if not args.write:
        for filename, _ in generated:
            print(f"[dry-run] {output_dir / filename}")
        print("Dry run complete. Re-run with --write to create files.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, content in generated:
        target = output_dir / filename
        target.write_text(content, encoding="utf-8")
        print(f"Generated {target}")


if __name__ == "__main__":
    main()
