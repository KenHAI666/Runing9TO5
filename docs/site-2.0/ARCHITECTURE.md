---
published: false
---
# 架構｜保留 Jekyll 的漸進升級

本文件為提案，沒有建立下列功能。基線與路由見 [ROUTE-INVENTORY.md](ROUTE-INVENTORY.md)。

## 現有資料流

```text
_posts/*.md + _config.yml + Liquid layouts/includes + assets
  → bundle exec jekyll build → _site → GitHub Pages
free.html（獨立 HTML/CSS/JS）→ POST JSON → n8n（站外）→ 郵件系統（未核實）
contact.md → 外部 Google Forms（不在靜態站處理訂單）
Notion JSON → notion2jekyll.py dry-run／人工審核 → 文章
```

兩個 layout、五個 include、一份 972 行共用 CSS；無獨立 JS 檔，JS 分布於 header/default/index/articles/free。`free.html` 不經共用 head，`privacy.md` 依賴 Minima `page`，其 default/head 被本地同名模板覆寫；實際仍有共用 SEO／追蹤，但重複 H1。沒有 `_data`、自定義 `_plugins`、collections、測試套件或 lockfile。

## 目標結構與責任

| 建議位置 | 責任 | 首次階段 |
| --- | --- | --- |
| `assets/css/tokens.css` | 語意色彩、尺寸、間距、動態規則 | 1 |
| `assets/css/components.css` | 導覽、按鈕、卡片、長文、表單狀態 | 1 |
| `assets/js/navigation.js` | 選單狀態、Escape、焦點與漸進增強 | 1 |
| `_includes/ui/button.html`、`card.html` | 受控參數、可存取連結／操作區分 | 1 |
| 現有 header/footer/layouts | 漸進接入 tokens，不改文章 URL | 1 |
| `_data/navigation.yml`、`taxonomy.yml` | 導覽與分類單一來源，暫保留 site.nav adapter | 2 |
| `start.md`、`search.json`、`assets/js/search.js` | 新手路徑、最小本地索引與前端搜尋 | 2 |
| `_resources/`、`_tools/`、`_services/`、`_courses/` | 公開行銷內容 collections | 3 |
| `_layouts/catalog.html`、`offering.html` | 目錄與詳情共用模板 | 3 |
| `scripts/validate_content.py` | schema、ID、路由、連結與敏感欄位檢查 | 3 |
| PR build-only workflow | 不帶正式 secrets、無 pages:write、只產驗證報告 | 1 |

新增 collection 必須 `output: true` 並明定 permalink；詳情路徑提案 `/resources/:slug/`、`/tools/:slug/`、`/services/:slug/`、`/courses/:slug/`。`/resources/` 仍是既有轉址，未核准 ROUTE-01 前不得建立目錄或移除別名。資源集合可先以待核准命名規劃，不能逕自換正式入口。

## 內容與渲染契約

1. `_posts` 留在原地，permalink 明定且凍結；缺少新欄位仍可用舊 layout，先做 adapter。
2. JSON 搜尋索引只收當次建置的公開文章；不含草稿、未來內容、訂閱資訊、內部備註或未上架商品。
3. 所有連結使用 relative_url／absolute_url，文章與新目錄的 canonical 各只有一個。JSON-LD 使用 jsonify，頁面標題及屬性 escape。
4. 商品資料預設 draft；商業上架狀態與 Jekyll `published` 是兩件事，必須驗證並同步控制公開輸出。
5. Schema 不臆造價格、評價、庫存、銷售數或課程完成證明。未核准 Offer 不輸出價格或 InStock。
6. 自訂外掛能不用則不用，維持 GitHub Pages 與 Cloudflare 的可攜性。

## 表單與分析邊界

正式 Webhook 保持原樣。本地測試只用攔截 fetch；未來預覽預設禁用送出或使用另核准的 sandbox。表單請求與分析事件不傳 email/name 到 dataLayer。後端才負責輸入檢查、重複訂閱、限流、CORS、同意紀錄、郵件交付及退訂；前端成功狀態須依經核准回應契約，不能憑 HTTP 2xx 宣稱已完成訂閱。

追蹤應集中於單一 adapter；GTM 與直接 GA4 的去重需先查容器。正式 ID 只在正式構建載入，預覽不送正式事件。沒有帳戶權限不能宣稱已修復分析或已符合法規。

## 學院界線

`academy.runing9to5.com` 僅為規劃中的獨立來源。官網只放核准介紹與前往連結；不放會員名單、訂單、API key、影片私密 URL、授權 token。未來由受保護後端驗證登入、付款 webhook 簽章與冪等、權限、短效影音存取、進度及稽核。公開 JSON、前端 localStorage 或隱藏 CSS 都不能作為權限控制。

會員／金流／影片供應商、Cookie 範圍、跨域 SSO、資料保留與備份均待 Phase 5 決策，Phase 1–4 不先植入未核准 SDK。
