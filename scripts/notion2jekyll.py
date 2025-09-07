import os
import re
from datetime import datetime
import subprocess

# -------------------------------
# Notion 文章資料範例（標題與文章先留白）
# -------------------------------
notion_pages = [
    {
        "title": "自媒體起號不靠天份",  # 這裡填文章標題
        "content": """ 用PDCA玩轉Threads的內容實戰筆記

---

# 🧩 前言｜帳號沒人看？不是你不夠努力，而是少了方法

很多人以為：「只要每天發文，總有一天會紅」，但你會發現

努力發了100則，還是沒人追蹤、沒人回應。

問題不在你懶，而是「沒策略」。

Threads 是一個適合「從0開始」的平台，

但唯有掌握 PDCA 策略，才能讓你避開迷路、走出變現之路。

這份筆記式電子書，將結合：

- PDCA經典商業循環框架（Plan / Do / Check / Act）
- K叔實戰策略精華
- 適合懶人自媒體者的執行法

如果你也想把 Threads 打造成一個會長大的內容資產，那這本就是為你寫的。

---

# 📍 Chapter 1｜Plan：定位好，才能不白忙

## 🔸 你是誰？你的差異點是什麼？

觀眾滑過你的頁面，只會問一個問題：「這帳號有什麼好追蹤的？」

所以你需要一個明確人設（角色＋特質＋提供價值）

🧑‍🎤 常見人設範例：

- 教學型｜快速傳授技巧，讓人覺得有收穫
- 搞笑型｜用幽默方式紓壓日常，吸引年輕TA
- 陪伴型｜寫內心話與情緒觀察，建立共鳴
- 逆襲型｜真實記錄從0到1的過程，吸引同路人
- 觀察型｜洞察社會與現象，製造思考點

✅ 建議練習：寫出你的「30字定位句」

---

## 🔸 你為誰而寫？目標受眾三步驟：

1. 選一群你熟悉 or 願意深入了解的人
2. 理解他們的痛點與渴望（想變現、沒靈感、怕曝光…）
3. 針對性地寫內容，幫他們解決一個一個問題

記住：不是誰都會看你，而是那群「懂你」的人，才會留著。

---

## 🔸 別等流量才想變現，請先設計出路

很多帳號流量很高，卻沒收入。因為他們忽略了這件事：

「變現路線要先想，內容策略才有方向。」

常見變現方式：

- 📦 商單合作（品牌曝光）
- 🛒 電商導購（賣產品、聯盟行銷）
- 🧠 數位產品（課程、懶人包、模板）
- 🫂 私域經營（Line群、訂閱制、社團）

✅ 寫下你最想嘗試的變現方式，之後內容圍繞它鋪設

---

# 🚀 Chapter 2｜Do：內容輸出，不再靠靈感

## 🔸 Threads平台運作邏輯（你懂越多，流量越穩）

- Threads推薦邏輯 ≈ 小流量池測試（10人） → 中池 → 大池
- 看重完播率、停留時間、互動（讚、留言、分享）
- 使用演算法友善的標籤與格式，增加曝光機率

---

## 🔸 爆款有邏輯，請學會「複製」

步驟如下：

1. 找出你領域中互動高的中小帳
2. 觀察他的開場、段落結構、CTA誘導
3. 用同樣架構，重寫成你的主題

「抄對結構 → 模仿邏輯 → 做出變體」

---

## 🔸 好內容不只要「寫得好」，還要「包裝對」

- 開頭3秒要有勾子（痛點、好奇、對話式）
- 畫面整齊、情緒明確、語氣真實
- 使用 Threads 支援的格式與功能（投票、串文等）

✅ 多平台轉發建議：Threads → IG限動 → 粉專 → 收集私訊

---

# 📊 Chapter 3｜Check：不是發完就結束，數據才是老師

## 🔸 基本數據你要看：

- 完播率（是否看到最後）
- 留存率（是否停留超過5秒）
- 點擊 / 留言 / 分享 數

✅ 小帳必看「前5秒完播率」，直接決定你能不能進下一池！

---

## 🔸 用數據找出成功模板

每週挑出1–2則表現最好的內容：

- 是哪個主題？
- 開場用了什麼句型？
- CTA在哪裡放？互動率高嗎？

將這些拆解下來，就能建立屬於你的「內容複製公式」。

---

# 🔁 Chapter 4｜Act：持續優化，把帳號養成長期資產

## 🔸 固定發文節奏，建立觀眾期待感

- 一天 1–3 則最佳，每日同時段可養成習慣
- 可用「系列化」打造記憶點，例如：每週一 #教學系列

---

## 🔸 多互動 ≠ 辛苦經營，而是養熟流量

- 每則文加入 CTA（你呢？你會怎麼做？留言告訴我）
- 定期辦互動小挑戰（+1送電子包、留言抽筆記）
- 私訊回覆，讓觀眾感到「被看見」

---

## 🔸 舊文活化再利用

- 表現好的內容，重新包裝、轉格式、放到其他平台
- 每月復盤一次，做出「最佳表現合集」

---

# 🎁 附錄資源

- 🔖 5種開場句式公式
- 🧰 Threads內容格式建議表
- 📓 爆款文觀察記錄表格
- 📎 CTA範例50句
- 📊 每週內容自評模板

---

# ✅ 行動引導 CTA

👉 喜歡這本電子書？記得：

1. 追蹤 Threads：@runing_9to5
2. 加入電子報，每週送你1篇Threads成長筆記
3. 想釐清個人策略？私訊我【起號諮詢】

---

你不是沒內容，而是還沒找到正確的方法
        """,  # 這裡填文章內容，保留 Markdown 排版
        "categories": ["教學"]  # 文章分類
    },
    # 可以再新增多篇文章
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
    return plain[:100] + "..." if len(plain) > 100 else plain

# -------------------------------
# 簡單自動生成 tags
# -------------------------------
def generate_tags(content):
    words = re.findall(r"[\u4e00-\u9fff]+|\b\w+\b", content)
    tags = list(dict.fromkeys(words))
    return tags[:5]

# -------------------------------
# 生成 Markdown 檔案（H1 標題 + 分類 + 標籤卡片，套用現有 CSS）
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

    # 將內容換行轉成 <p> 標籤
    content_paragraphs = page['content'].split('\n\n')
    content_html = ''.join(f'<p>{p.replace("\n","<br>")}</p>\n' for p in content_paragraphs)

    # 組成完整卡片 HTML
    card_html = f'''
<div class="card-section">
    <h1>{page['title']}</h1>
    {content_html}
    <p><strong>分類:</strong> {page['categories'][0]}</p>
    <p><strong>標籤:</strong> {', '.join(tags)}</p>
</div>
'''

    # 寫入 Markdown 檔案
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + card_html)

    print(f"生成文章：{filename}")

    # Git commit & push
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"新增文章：{page['title']}"])
    subprocess.run(["git", "push", "origin", "main"])

print("完成！")
