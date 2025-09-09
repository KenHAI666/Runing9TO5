import os
import re
from datetime import datetime
import subprocess

# -------------------------------
# Notion 文章資料範例
# -------------------------------
notion_pages = [
    {
        "title": "你的圈子決定你的成就",
        "categories": ["電子報"],
        "content": """我希望帶給大家，如同朋友間的感覺
我不是什麼自媒體大神，也不是甚麼高人
只是各位，在自媒體經營上的朋友，所以歡迎提出你想問的問題

**你的 財富/認知 取決於身邊最親近6人的平均**

你可能聽過這句話，但你有仔細想過它的影響有多深嗎？
🔸 他們怎麼看待賺錢，你就容易複製同樣的模式
🔸 他們遇到挑戰是選擇退縮，還是找方法突破，也會影響你的行動習慣
🔸 他們聊的話題，是買房買車，還是抱怨上班、存不到錢？
不知不覺，大家就都在同一個水平

所以
如果你開始覺得卡關、不滿現狀、但又說不上來問題是什麼
**很可能，是圈子該更新了。**
✔️ 找對的人互動
✔️ 看對的內容
✔️ 追蹤讓你變更好的創作者

這些選擇，就是你未來的方向
因為我相信： **努力很重要，但選對圈子更快**你可以沒資源、沒背景，但你不能繼續一個人亂撞如果你正在打造個人品牌、學習自媒體變現我在做這件事，

也歡迎你一起 加入我的朋友圈目前我覺得最簡單 也最有效的方式就是在THREADS上透過內容，

去打開你的圈子當你開始發文，你會發現你接觸到的人變多了當你開始做個人品牌，

你會發現你一只低估了自己經營內容，不只是曝光自己，

更是在重塑你的圈子你的帳號可以是你跳脫現狀、認識新圈子、建立影響力的起點
而個人品牌，不是要你去演一個更好的自己，

而是**去長出「你想成為的樣子」**

"""
    },
]

# -------------------------------
# 確認 _posts 資料夾
# -------------------------------
if not os.path.exists("_posts"):
    os.makedirs("_posts")

# -------------------------------
# 幫標題生成安全檔名
# -------------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

# -------------------------------
# 簡單生成 SEO description
# -------------------------------
def generate_description(content):
    plain = re.sub(r"<[^>]+>", "", content)
    plain = re.sub(r"\s+", " ", plain)
    return plain[:100] + "..." if len(plain) > 100 else plain

# -------------------------------
# 簡單自動生成 tags
# -------------------------------
def generate_tags(content):
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    tags = list(dict.fromkeys(words))
    return tags[:5]

# -------------------------------
# Markdown -> HTML 保留標題與分隔線
# -------------------------------
def markdown_to_html_keep_headers(md_content):
    html_lines = []
    for line in md_content.split("\n"):
        line = line.strip()
        if line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line == "---":
            html_lines.append("<hr>")
        else:
            html_lines.append(line)  # 保留原 Markdown（表格或段落）
    return "\n".join(html_lines)

# -------------------------------
# 生成 Markdown 檔案
# -------------------------------
for page in notion_pages:
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"_posts/{today}-{slugify(page['title'])}.md"

    description = generate_description(page['content'])
    tags = generate_tags(page['content'])
    title_with_category = f"[{page['categories'][0].capitalize()}] {page['title']}"

    # Front matter
    front_matter = f"""---
layout: default
title: "{title_with_category}"
date: {today}
categories: {page.get('categories', [])}
tags: {tags}
description: "{description}"
---
"""

    # 內容轉 HTML / 保留 Markdown 表格
    content_html = markdown_to_html_keep_headers(page['content'])

    # 組成完整文章
    full_content = f'''
{content_html}

<p><strong>分類:</strong> {page['categories'][0]}</p>
<p><strong>標籤:</strong> {', '.join(tags)}</p>
'''

    # 寫入 Markdown 檔案
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + full_content)

    print(f"生成文章：{filename}")

    # Git commit & push
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"新增文章：{page['title']}"])
    subprocess.run(["git", "push", "origin", "main"])

print("完成！")
