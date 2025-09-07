import os
import re
from datetime import datetime
import subprocess

# -------------------------------
# Notion 文章資料範例（標題與文章先留白）
# -------------------------------
notion_pages = [
    {
        "title": "Threads 各行業經營指南",  # 這裡填文章標題
        "content": """ ## 🏢 業務類建議

**適用對象：** 業務員、保險業、業務型創業者

### 內容策略

- **真實故事分享：** 業務日常、心酸歷程、客戶奇遇記
- **熱門話題：** 暴發戶觀察、客戶百態、職場八卦
- **互動技巧：** 裝作不懂提問，善用問號引發討論
- **發文格式：** 長文拆分成串文，增加互動機會

### 人設建立

- 建立鮮明個人品牌，讓讀者產生認同感
- 分享真實經歷，增加可信度
- 以文字內容為主（Threads 影片效果較差）

### 行動呼籲

- 明確 CTA：引導留言、追蹤、私訊
- 例句：「你們遇過最奇葩的客戶是什麼樣？留言分享！」

---

## 🛒 電商類建議

**適用對象：** 蝦皮賣家、聯盟行銷、分潤業者

### 避免事項

- 不直接貼外部購物連結（可能被限流）
- 避免過度銷售導向內容

### 內容策略

- **心得分享式行銷：** 以「使用體驗」取代「產品推銷」
- **故事包裝法：** 描述產品使用場景、生活結合方式
- **關係建立：** 先交朋友，再談合作

### 導流策略

- 建立私域流量池（IG、個人網站）
- 發文時間策略：
    - 軟性銷售 → 下午時段
    - 資訊分享 → 晚上時段

---

## 🏪 實體店面建議

**適用對象：** 餐廳、美髮沙龍、零售店面

### 引流策略

- 設計有趣文案吸引實際造訪
- 結合故事、趣聞、情境演出
- 分享在地特色、周邊推薦

### 內容方向

- 強調實體體驗價值
- 分享在地生活話題
- 整合多平台增加信任度

### 社群證明

- 分享客戶評論與體驗
- 創造使用者生成內容
- CTA 範例：「你有來過我們店嗎？留言分享你的體驗！」

---

## 🔮 命理占卜類建議

**適用對象：** 面相師、命理師、心理測驗創作者

### 內容方向

- **趣味性優先：** 「最容易發財的面相」、「天生好命的特徵」
- **故事化包裝：** 用案例分析取代理論說教
- **親民語言：** 避免過於專業的術語

### 信任建立

- 分享「為什麼準確」的背後邏輯
- 收集並分享使用者真實故事
- 避免制式化 AI 文案，加入個人觀點

### 擴展內容

- 結合花語、心測、塔羅等相關主題
- 吸引不同興趣的受眾群體

---

## 📝 自媒體類建議

**適用對象：** 內容創作者、知識型網紅

### 文章架構

1. **吸睛開頭** - 抓住注意力
2. **分段排版** - 提升閱讀體驗
3. **明確 CTA** - 引導下一步行動

### 經營策略

- 導流至主要平台（IG、個人網站、電子報）
- 善用「文字溫度」建立情感連結
- 拆分長文為短句串文，符合演算法偏好

### 發文時機

- **心理層面內容** → 深夜發佈
- **高互動問句** → 中午或傍晚

---

## 📊 通用經營策略

### 平台特性

- **以文字為主導** - Threads 文字內容效果最佳
- **長文拆短串** - 配合演算法推薦機制
- **重視互動** - 提問式內容提升參與度

### 發文時間指南

| 時段 | 適合內容類型 | 發文目的 | 範例方向 |
| --- | --- | --- | --- |
| **上午 07:00–09:00** | 輕鬆廢文、觀察文、情緒短句 | 快速吸睛，輕度互動 | 厭世上班族、上班前心情、生活側寫 |
| **中午 12:00–13:00** | 干貨文、方法論、經營筆記 | 建立專業信任感 | 自媒體教學、經營策略、商業模型 |
| **下午 16:00–18:00** | 話題感強的觀點文、對話式內容、互動型貼文 | 創造討論與留言 | Threads 實驗、職場觀察、反思問句 |
| **晚上 21:00 以後** | 情緒面、內心獨白、深度故事、暖系長文 | 建立連結、觸動人心 | 自我覺察、心累心得、低潮故事 |

### 內容核心原則

1. **故事優於銷售** - 用情感連結取代硬性推銷
2. **互動勝過單向** - 每篇貼文都要有明確 CTA
3. **真實勝過完美** - 分享真實經歷比包裝形象更有效

### 必備 CTA 範例

- 「你的經驗是什麼？留言告訴我」
- 「覺得有用的話，分享給需要的朋友」
- 「想了解更多可以私訊我」
- 「追蹤我獲得更多實用內容」

---

## 🎯 成功指標

### 短期目標

- 提升單篇貼文互動率
- 增加追蹤者數量
- 建立穩定發文節奏

### 長期目標

- 建立個人品牌識別度
- 培養忠實讀者群
- 創造實際商業價值

記住：**內容為王，互動為后，真誠為本。** 在 Threads 上成功的關鍵是建立真實的人際連結，而不是單純的流量追求。
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
<div class="card-section-1">
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
