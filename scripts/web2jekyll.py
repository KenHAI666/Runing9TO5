import os
from datetime import datetime

POSTS_DIR = "_posts"

def create_article(title, category, content):
    """後台輸入文章 → 存成 Markdown 檔案"""

    # 產生檔名
    date = datetime.now().strftime("%Y-%m-%d")
    slug = title.replace(" ", "-").lower()
    filename = f"{date}-{slug}.md"

    # 文章 Front Matter（Jekyll 必須要有）
    front_matter = f"""---
layout: post
title: "{title}"
categories: {category}
---

"""

    # 套用 card-section-1 CSS
    styled_content = f'<div class="card-section-1">\n{content}\n</div>'

    # 合併完整內容
    final_content = front_matter + styled_content

    # 存檔
    path = os.path.join(POSTS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(final_content)

    return path

if __name__ == "__main__":
    # 測試用
    path = create_article(
        title="測試文章",
        category="測試分類",
        content="這是一篇測試文章，內容由後台輸入。",
    )
    print(f"✅ 已建立文章: {path}")
