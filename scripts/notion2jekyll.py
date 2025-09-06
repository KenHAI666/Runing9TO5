import os
from datetime import datetime

# ----------------------------
# 文章資訊
# ----------------------------
# 1. 將 Notion 文章標題與內容貼在這裡
title = "示範文章標題"
content = """
這是從 Notion 複製過來的文章內容
可包含多行文字。
"""

# 2. 日期
date = datetime.now().strftime("%Y-%m-%d")

# ----------------------------
# 生成 Jekyll Markdown
# ----------------------------
# 轉成檔名格式 YYYY-MM-DD-文章標題.md
slug = title.replace(" ", "-")
filename = f"{date}-{slug}.md"

# Jekyll front matter
front_matter = f"""---
layout: post
title: "{title}"
date: {date} 00:00:00 +0800
---

"""

# 組合完整 Markdown
markdown = front_matter + content

# 儲存到 _posts/
posts_dir = os.path.join(os.path.dirname(__file__), "../_posts")
os.makedirs(posts_dir, exist_ok=True)
filepath = os.path.join(posts_dir, filename)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"文章已生成: {filepath}")
