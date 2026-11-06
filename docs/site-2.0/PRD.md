---
published: false
---
# K叔個人網站 2.0｜PRD

狀態：Phase 0 審核稿，尚未核准後續實作。盤點日：2026-11-06（Asia/Taipei）。
基線：`KenHAI666/Runing9TO5` main `b951dfc0657ff43e2edc8f4468cfec4de0d8268b`（完整 SHA 以 ROUTE-INVENTORY 為準）。
本次僅新增文件；正式網域、DNS、部署、Webhook、金流與網站功能均不變。

## 目標與成功條件

服務已有商品、服務或專業能力的個人品牌經營者，維持「低粉 × 高信任 × 低摩擦」。從部落格升級為品牌官網、SEO 與免費資源中心、工具／數位商品／服務入口、課程介紹站；會員學院另案。

| 需求 | 可驗收結果 | 階段 |
| --- | --- | --- |
| 品牌一致 | 共用導覽、頁尾、卡片、按鈕、文章排版，手機可操作 | 1 |
| 找到下一步 | 首頁與 `/start/` 明確區分讀文章、拿資源、看服務 | 2 |
| 找內容 | 搜尋標題／描述／分類，有空結果與無 JS 降級 | 2 |
| 可維護目錄 | 資源、工具、服務、課程由可驗證資料與模板產生 | 3 |
| 保留內容資產 | 現有 permalink 不變，路由與 sitemap 差異須審核 | 全程 |
| 安全遷移 | 先獨立預覽，排程、轉址、SEO、回復演練過關才提案 | 4 |
| 獨立學院 | 認證、訂單、權限、影片與進度在受保護後端 | 5，另行核准 |

基線指標尚未取得 GA4／Search Console 權限，不編造流量或轉換目標。先記錄 SEO 索引、自然搜尋點擊、資源 CTA 點擊與經後端確認的訂閱成功；數值目標與歸因待 K叔確認。前端顯示成功不得等同已完成 double opt-in。

## 現況架構與功能

Jekyll + `github-pages` gem，Minima 提供 fallback layout；GitHub Actions 自行建置及 Pages 部署。根頁包含首頁、文章分類列表、關於、諮詢、隱私與獨立免費資源頁。文章 52 篇（51 篇在盤點日期可發布，1 篇為 11/09 未來文章）；19 份 `_drafts` 不會因日期到期自動發布。另有 `_posts/post.html` 非標準文章檔。

可用功能：置頂文章、前端分類篩選、相關／最新文章、文章 CTA、手機漢堡選單、返回頂端、FAQ、捲動動畫、免費資源訂閱、Google Forms 諮詢入口、GA4／GTM、部分 FAQ／Service 結構化資料。尚無全文搜尋、商品資料庫、購物車、會員、訂單、課程權限或金流後端。

## 可保留資產

- 全部文章、草稿、圖片、既有標題／描述／permalink／來源欄位與內部連結；草稿不自動上線。
- `_includes/header.html`、`footer.html`、`primary-cta.html`、`post-cta.html` 的分工；移除重複樣式採漸進 PR。
- `_layouts/post.html` 的長文、表格與行動版支援；`default.html` 的共用骨架與相關文章概念。
- `_includes/head.html` 的動態 canonical、OG、JSON-LD；先修證據明確的問題，不整段重寫。
- 原 `/free` 入口與兩個訂閱位置、諮詢表單入口、品牌素材、目前分類與置頂機制。
- `scripts/notion2jekyll.py` 的 dry-run 概念；匯入器需補 YAML escaping、覆寫保護後再擴充。

## 問題與優先級

P0＝進入後續開發／發布前的阻擋；P1＝近期應修；P2＝可排後。此處均為提案，非已修正。

| ID | 優先級 | 證據與影響 | 建議處理／階段 |
| --- | --- | --- | --- |
| GOV-01 | P0 | `scripts/server.py` 的 `/publish` 執行 git add/commit/push origin main，README 描述與程式不一致 | 禁止啟動舊編輯器；另開 PR 移除自動 push、改分支與審核 |
| ROUTE-01 | P0 | `/resources/`、`/resources.html` 已轉址 `/free` | Phase 3 前核准路由所有權與替代承接；新集合不得覆寫別名 |
| MIG-01 | P0（遷移） | Cloudflare HTML 正規化可能把 `/contact.html` 導到 `/contact`，與現 canonical 不同；無根 404 | 預覽逐條驗證 redirect loop、soft 404，再選映射 |
| SEO-01 | P2 | 朋友圈文章引用 `/free.html`；本地確實有此檔，canonical 為 `/free` | 查正式主機的別名／正規化，不誤報缺檔；統一內連另 PR |
| FORM-01 | P1 | `free.html` 兩表單 input type=text、只有非空檢查；離線重現錯誤 email 被送出 | type=email、可存取 label、格式錯誤提示，獨立 PR |
| FORM-02 | P1 | `res.ok` 即成功、不讀 body、無 timeout；確認信／完成訂閱文案混用 | 先取得 n8n 回應契約；區分待確認、重複、限流、失敗與逾時 |
| SEO-02 | P1 | `privacy.md` 用 theme page → 本地 default/head，實際輸出兩個 H1，description 採站級 fallback | 另 PR 保留共用 head、去重 H1、補頁面描述 |
| ANALYTICS-01 | P1 | 共用 head 同時有 GTM 和直接 GA4；無容器設定證據 | 查容器是否重複送 page_view；預覽停用正式追蹤 |
| ADS-01 | P1 | ads.enabled=false，但 head 無條件載入 AdSense JS | 經 PR 統一 gate；不假設已啟用廣告或有收入 |
| A11Y-01 | P1 | 表單無 label／live region；FAQ 不更新 aria-expanded；動畫依賴 JS | keyboard、focus、減少動態與無 JS 基線 |
| BUILD-01 | P1 | 無 Gemfile.lock，CI Ruby 3.2，依賴每次重新解析；include-cache 由 github-pages 233 傳遞提供 | 鎖定經驗證版本、確認直接／傳遞依賴、CI 與本地一致 |
| SCHEDULE-01 | P1 | 每日 23:10 UTC＝隔日台北 07:10；只 push main 才驗證 | 明確排程 SLA、PR build-only、避免並行舊輸出覆蓋 |
| PERF-01 | P2 | 外部字體、inline CSS/JS、多處圖片未定尺寸；CSS URL 每次 build 變更 | 漸進抽取、圖像尺寸與壓縮、內容 hash 快取 |
| CONTENT-01 | P2 | 分類 label 重複寫在列表；定價／Offer 散落多處 | 集中資料模型，現有 NT$1,000/60 分鐘僅為原碼快照，續用需確認 |

## 邊界與停止點

本次不修改以上問題，也不更動部署 workflow。八份文件使用 `published: false`，避免被 Jekyll 當公開頁面輸出；合併前須驗證。Phase 0 完成即停止，Phase 1 僅列任務。

需 K叔核准：進入 Phase 1；暖金色候選方案；`/resources/` 新用途與 redirect 取捨；目前諮詢價格／服務內容是否仍有效；追蹤與同意政策；Cloudflare 帳戶／預覽授權／排程方案／正式切換；學院技術、金流、退款、稅務與交付。所有正式操作必須再經具體審核。

外部服務與成本清單見 [MIGRATION.md](MIGRATION.md)，執行任務見 [TASKS.md](TASKS.md)，本次證據與未驗證項目見 [QA-CHECKLIST.md](QA-CHECKLIST.md)。
