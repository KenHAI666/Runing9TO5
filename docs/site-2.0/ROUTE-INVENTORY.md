---
published: false
---
# 路由與原始碼盤點

盤點日 2026-11-06，基線 main `b951dfc0657ff43e2edc8f4468cfec4de0d8268b`。本清單為本地 Jekyll 3.10.0／github-pages 233 實際建置推導，不宣稱等於正式站當下部署；正式站 GET 受目前網路政策 403 阻擋。公開 URL 一律以 `https://runing9to5.com` 加下表 path 組成。

台北 2026-11-06 12:00 固定時鐘建置：51 篇公開文章、6 個主要頁、4 個 redirect 頁、19 個其餘輸出，共 80 個檔案。sitemap 57 個 loc＝51 篇文章＋6 個主要頁；redirect、landing 與 assets 不在該 sitemap。沒有路由碰撞。canonical path 與實體輸出檔不同時，下表分別列出；HTTP status、extensionless 別名與主機正規化仍需正式／預覽主機驗證。

## 頁面、轉址與插件輸出

| Jekyll URL／靜態 path | 實體輸出 | 來源／性質 |
| --- | --- | --- |
| `/about.html` | `/about.html` | `about.md；default` |
| `/articles/` | `/articles/index.html` | `articles.md；default` |
| `/contact.html` | `/contact.html` | `contact.md；default` |
| `/free` | `/free.html` | `free.html；無 layout` |
| `/` | `/index.html` | `index.md；default` |
| `/privacy/` | `/privacy/index.html` | `privacy.md；page` |
| `/assets/main.css` | `/assets/main.css` | `assets/main.scss；無 layout` |
| `/contact/` | `/contact/index.html` | `redirect.html；redirect` |
| `/free/` | `/free/index.html` | `redirect.html；redirect` |
| `/resources/` | `/resources/index.html` | `redirect.html；redirect` |
| `/resources.html` | `/resources.html` | `redirect.html；redirect` |
| `/redirects.json` | `/redirects.json` | `redirects.json；無 layout` |
| `/feed.xml` | `/feed.xml` | `feed.xml；無 layout` |
| `/sitemap.xml` | `/sitemap.xml` | `sitemap.xml；無 layout` |

redirects.json 證實：`/contact/` → `https://runing9to5.com/contact.html`；`/free/`、`/resources/`、`/resources.html` → `https://runing9to5.com/free`。這些是 jekyll-redirect-from 的 HTML refresh/canonical，不是已驗證的 HTTP 301。

`/landing` 為靜態 HTML 內容（無副檔名），noindex + meta refresh 到 `/free`；未驗證主機 MIME。`/about`、`/contact`、`/articles` 等無 slash／無副檔名連結需主機 alias 支援，不能只憑檔案清單保證 status。

## 公開文章（日期已到，51 篇）

| URL path | 原始碼 | 實體輸出 |
| --- | --- | --- |
| `/articles/which-content-type-suits-you/` | `_posts/2025-09-07-threads-各行業經營指南.md` | `/articles/which-content-type-suits-you/index.html` |
| `/articles/social-media-growth-with-pdca/` | `_posts/2025-09-07-自媒體起號不靠天份.md` | `/articles/social-media-growth-with-pdca/index.html` |
| `/articles/your-circle-determines-your-ceiling/` | `_posts/2025-09-09-你的圈子決定你的成就.md` | `/articles/your-circle-determines-your-ceiling/index.html` |
| `/articles/threads-account-level-kpi/` | `_posts/2025-09-10-threads-等級-kpi-表.md` | `/articles/threads-account-level-kpi/index.html` |
| `/articles/product-before-content/` | `_posts/2025-09-12-自媒體不是先發文而是先賣東西.md` | `/articles/product-before-content/index.html` |
| `/articles/side-hustle-while-employed/` | `_posts/2025-09-13-不離職創業指南成為薪水小偷.md` | `/articles/side-hustle-while-employed/index.html` |
| `/articles/introvert-content-creator-guide/` | `_posts/2025-12-10-3個困境與5步心法，不露臉也能打造高信任變現系統.md` | `/articles/introvert-content-creator-guide/index.html` |
| `/articles/before-you-quit-your-job/` | `_posts/2025-12-11-為什麼 90% 的上班族，裸辭也沒用？建立你的不敗職涯系統.md` | `/articles/before-you-quit-your-job/index.html` |
| `/articles/stop-comparing-your-progress/` | `_posts/2025-12-12-停止比較別人的進度｜建立自己的節奏與自信.md` | `/articles/stop-comparing-your-progress/index.html` |
| `/articles/self-review-system/` | `_posts/2026-04-09-自我考核變得更有意義的完整流程｜從過場到真實成長.md` | `/articles/self-review-system/index.html` |
| `/articles/threads-vs-blog-platform-guide/` | `_posts/2026-05-04-threads-還是-blog-上班族自媒體平台選擇指南.md` | `/articles/threads-vs-blog-platform-guide/index.html` |
| `/articles/threads-content-repurpose-strategy/` | `_posts/2026-05-06-threads-舊文重發提升87倍觸及-上班族自媒體內容再利用策略.md` | `/articles/threads-content-repurpose-strategy/index.html` |
| `/articles/self-media-start-mistakes/` | `_posts/2026-05-28-self-media-start-mistakes.md` | `/articles/self-media-start-mistakes/index.html` |
| `/articles/content-branch-method/` | `_posts/2026-05-29-content-branch-method.md` | `/articles/content-branch-method/index.html` |
| `/articles/threads-posting-time-guide/` | `_posts/2026-05-30-threads-posting-time-guide.md` | `/articles/threads-posting-time-guide/index.html` |
| `/articles/threads-business-guide/` | `_posts/2026-05-31-threads-business-guide.md` | `/articles/threads-business-guide/index.html` |
| `/articles/side-hustle-before-quitting/` | `_posts/2026-06-01-side-hustle-before-quitting.md` | `/articles/side-hustle-before-quitting/index.html` |
| `/articles/content-trust-conversion/` | `_posts/2026-06-02-content-trust-conversion.md` | `/articles/content-trust-conversion/index.html` |
| `/articles/who-should-do-self-media/` | `_posts/2026-06-03-who-should-do-self-media.md` | `/articles/who-should-do-self-media/index.html` |
| `/articles/make-content-easy-to-understand/` | `_posts/2026-06-04-make-content-easy-to-understand.md` | `/articles/make-content-easy-to-understand/index.html` |
| `/articles/content-optimization-loop/` | `_posts/2026-06-05-content-optimization-loop.md` | `/articles/content-optimization-loop/index.html` |
| `/articles/low-followers-high-trust/` | `_posts/2026-06-06-low-followers-high-trust.md` | `/articles/low-followers-high-trust/index.html` |
| `/articles/positioning-for-right-audience/` | `_posts/2026-06-07-positioning-for-right-audience.md` | `/articles/positioning-for-right-audience/index.html` |
| `/articles/trust-before-traffic/` | `_posts/2026-06-08-trust-before-traffic.md` | `/articles/trust-before-traffic/index.html` |
| `/articles/company-of-one-side-hustle/` | `_posts/2026-06-09-company-of-one-side-hustle.md` | `/articles/company-of-one-side-hustle/index.html` |
| `/articles/measurable-content-system/` | `_posts/2026-06-10-measurable-content-system.md` | `/articles/measurable-content-system/index.html` |
| `/articles/content-with-product-first/` | `_posts/2026-06-19-content-with-product-first.md` | `/articles/content-with-product-first/index.html` |
| `/articles/content-needs-exit/` | `_posts/2026-06-21-content-needs-exit.md` | `/articles/content-needs-exit/index.html` |
| `/articles/personal-brand-magnifier/` | `_posts/2026-06-23-personal-brand-magnifier.md` | `/articles/personal-brand-magnifier/index.html` |
| `/articles/in-office-creator-reason/` | `_posts/2026-06-25-in-office-creator-reason.md` | `/articles/in-office-creator-reason/index.html` |
| `/articles/creator-positioning-iteration/` | `_posts/2026-06-27-creator-positioning-iteration.md` | `/articles/creator-positioning-iteration/index.html` |
| `/articles/put-yourself-into-content/` | `_posts/2026-06-29-put-yourself-into-content.md` | `/articles/put-yourself-into-content/index.html` |
| `/articles/three-trust-content-types/` | `_posts/2026-07-01-three-trust-content-types.md` | `/articles/three-trust-content-types/index.html` |
| `/articles/content-works-while-you-rest/` | `_posts/2026-07-03-content-works-while-you-rest.md` | `/articles/content-works-while-you-rest/index.html` |
| `/articles/free-resource-trust-entry/` | `_posts/2026-07-05-free-resource-trust-entry.md` | `/articles/free-resource-trust-entry/index.html` |
| `/articles/repeatable-side-hustle-path/` | `_posts/2026-07-07-repeatable-side-hustle-path.md` | `/articles/repeatable-side-hustle-path/index.html` |
| `/articles/threads-traffic-no-sales/` | `_posts/2026-07-09-threads-traffic-no-sales.md` | `/articles/threads-traffic-no-sales/index.html` |
| `/articles/product-self-media-start/` | `_posts/2026-07-11-product-self-media-start.md` | `/articles/product-self-media-start/index.html` |
| `/articles/sell-service-under-1000-followers/` | `_posts/2026-07-13-sell-service-under-1000-followers.md` | `/articles/sell-service-under-1000-followers/index.html` |
| `/articles/content-conversion-system/` | `_posts/2026-07-15-content-conversion-system.md` | `/articles/content-conversion-system/index.html` |
| `/articles/threads-leads-for-services/` | `_posts/2026-07-17-threads-leads-for-services.md` | `/articles/threads-leads-for-services/index.html` |
| `/articles/not-everyone-needs-self-media/` | `_posts/2026-08-31-not-everyone-needs-self-media.md` | `/articles/not-everyone-needs-self-media/index.html` |
| `/articles/content-diagnosis-consulting/` | `_posts/2026-09-07-content-diagnosis-consulting.md` | `/articles/content-diagnosis-consulting/index.html` |
| `/articles/professional-needs-visibility/` | `_posts/2026-09-14-professional-needs-visibility.md` | `/articles/professional-needs-visibility/index.html` |
| `/articles/self-media-second-run/` | `_posts/2026-09-21-self-media-second-run.md` | `/articles/self-media-second-run/index.html` |
| `/articles/market-crowding-before-product/` | `_posts/2026-09-28-market-crowding-before-product.md` | `/articles/market-crowding-before-product/index.html` |
| `/articles/k-uncle-friends/` | `_posts/2026-10-10-k-uncle-friends.md` | `/articles/k-uncle-friends/index.html` |
| `/articles/self-media-is-a-tool/` | `_posts/2026-10-16-self-media-is-a-tool.md` | `/articles/self-media-is-a-tool/index.html` |
| `/articles/threads-no-traffic-shadowban/` | `_posts/2026-10-19-threads-no-traffic-shadowban.md` | `/articles/threads-no-traffic-shadowban/index.html` |
| `/articles/threads-pdca-one-change/` | `_posts/2026-10-22-threads-pdca-one-change.md` | `/articles/threads-pdca-one-change/index.html` |
| `/articles/threads-no-engagement-positioning/` | `_posts/2026-10-29-threads-no-engagement-positioning.md` | `/articles/threads-no-engagement-positioning/index.html` |

## 未來文章與草稿（非目前公開 URL）

| 來源 | 規劃 permalink | 狀態 |
| --- | --- | --- |
| `_drafts/2026-10-20-ordinary-script-needs-a-project.md` | `/articles/ordinary-script-needs-a-project/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-10-23-set-goal-before-posting.md` | `/articles/set-goal-before-posting/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-10-27-turn-your-mix-into-positioning.md` | `/articles/turn-your-mix-into-positioning/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-10-30-part-time-feel-repositioning.md` | `/articles/part-time-feel-repositioning/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-11-03-teach-without-big-following.md` | `/articles/teach-without-big-following/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-11-06-why-threads-for-personal-brand.md` | `/articles/why-threads-for-personal-brand/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-11-10-threads-account-with-a-mission.md` | `/articles/threads-account-with-a-mission/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-11-13-lower-the-bar-for-content.md` | `/articles/lower-the-bar-for-content/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-11-17-small-tasks-fragment-time.md` | `/articles/small-tasks-fragment-time/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-11-20-repeat-to-build-trust.md` | `/articles/repeat-to-build-trust/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-11-24-post-with-purpose.md` | `/articles/post-with-purpose/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-11-27-solve-your-own-problem-first.md` | `/articles/solve-your-own-problem-first/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-12-01-choose-coach-for-your-stage.md` | `/articles/choose-coach-for-your-stage/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-12-04-lychee-second-path.md` | `/articles/lychee-second-path/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-12-08-broad-vs-niche-traffic.md` | `/articles/broad-vs-niche-traffic/` | _drafts；日期到也不自動發布 |
| `_drafts/2026-12-11-posting-vs-engaging-threads.md` | `/articles/posting-vs-engaging-threads/` | _drafts；日期到也不自動發布 |
| `_drafts/fb-2026-05-28-notion-blog-batch.md` | `未設定（社群批次備稿）` | _drafts；日期到也不自動發布 |
| `_drafts/fb-2026-06-03-notion-blog-batch-2.md` | `未設定（社群批次備稿）` | _drafts；日期到也不自動發布 |
| `_drafts/fb-2026-06-09-book-notes-batch.md` | `未設定（社群批次備稿）` | _drafts；日期到也不自動發布 |
| `_posts/2026-11-09-ai-copywriting-human-review.md` | `/articles/ai-copywriting-human-review/` | 未來 _posts；日期到後需 rebuild |

`_posts/post.html` 只有 layout front matter，檔名不符合 Jekyll 文章日期規則，本次未產生公開路由。3 份 fb-* 草稿為社群批次文字，其餘 16 份為文章草稿。不得用 --drafts／--future 建置正式站。

## 其他靜態公開輸出（完整清單）

| URL path | 來源 |
| --- | --- |
| `/ads.txt` | `/ads.txt` |
| `/assets/css/style.css` | `/assets/css/style.css` |
| `/assets/images/articles/threads-account-status-result.webp` | `/assets/images/articles/threads-account-status-result.webp` |
| `/assets/images/articles/threads-account-status-step1.webp` | `/assets/images/articles/threads-account-status-step1.webp` |
| `/assets/images/favicon.png` | `/assets/images/favicon.png` |
| `/assets/images/in-1.PNG` | `/assets/images/in-1.PNG` |
| `/assets/images/me.jpeg` | `/assets/images/me.jpeg` |
| `/assets/images/og-default.jpg` | `/assets/images/og-default.jpg` |
| `/assets/images/testimonials/IMG_9410.jpeg` | `/assets/images/testimonials/IMG_9410.jpeg` |
| `/assets/images/testimonials/IMG_9416.JPG` | `/assets/images/testimonials/IMG_9416.JPG` |
| `/assets/images/testimonials/IMG_9417.jpeg` | `/assets/images/testimonials/IMG_9417.jpeg` |
| `/assets/images/testimonials/IMG_9817.jpeg` | `/assets/images/testimonials/IMG_9817.jpeg` |
| `/landing` | `/landing` |
| `/robots.txt` | `/robots.txt` |
| `/assets/minima-social-icons.svg` | `/assets/minima-social-icons.svg` |

`assets/main.css` 與 `assets/minima-social-icons.svg` 由 Minima 額外輸出。圖片 10 個，共用 CSS 1 個；沒有獨立 JS 檔。favicon 為 118,306 bytes、me.jpeg 127,658 bytes、in-1.PNG 471,672 bytes，值得優化但本次不改圖。

## Layout、Include、CSS、JS 與開發來源

| 檔案 | 現有責任／可沿用與注意事項 |
| --- | --- |
| `_layouts/default.html` | 共用 head/header/main/footer、相關與最新文章、backToTop；footer 在 main 內、需 skip link |
| `_layouts/post.html` | 文章 metadata、HTML／Markdown 長文與表格、廣告 slot gate；樣式 inline |
| `_includes/head.html` | SEO／canonical／OG／JSON-LD、GTM/GA4/AdSense；廣告 JS gate 與追蹤去重待修 |
| `_includes/header.html` | 手機導覽與 inline toggle JS，已有 aria-expanded／controls |
| `_includes/footer.html` | 品牌／privacy，年份寫死 2026 |
| `_includes/primary-cta.html` | 訂閱入口與 generate_lead 點擊事件；點擊不等於訂閱成功 |
| `_includes/post-cta.html` | 作者介紹、訂閱／諮詢 CTA，價格散落 |
| `assets/css/style.css` | 972 行，tokens、components、動畫、480/768 breakpoint，@import Google Fonts |
| `index.md` | 品牌、痛點、服務、FAQ、文章等區塊與 IntersectionObserver |
| `articles.md` | 置頂、前端分類篩選，無搜尋、無分頁，clickable div 需鍵盤檢查 |
| `free.html` | 775 行獨立 HTML、inline CSS／JS、兩個訂閱位置、FAQ、reveal |
| `about.md` / `contact.md` / `privacy.md` | 品牌與諮詢／外部表單／政策內容 |
| `scripts/notion2jekyll.py` | JSON 匯入、dry-run、外部 output-dir 可測；未 escape YAML 字串、會覆寫同名檔 |
| `scripts/server.py` / `web2jekyll.py` | 舊 Flask 編輯器與文章產生器；前者會直接 push main，禁止啟動 |
| `templates/editor.html` | 舊 Flask 編輯 UI，開發用、被 exclude |
| `.github/workflows/jekyll-deploy.yml` | push main + 每日排程 + dispatch，Ruby 3.2、Pages artifact/deploy |
| `README.md` / `README.html` / `scripts/READ ME` | 前兩者 exclude；READ ME 有不再相符的安全敘述，需另 PR |

根目錄其餘為 Gemfile、_config.yml、.gitignore、robots、ads、landing。無 CNAME、根 404、自訂 plugins、_data 或 collections；GitHub Pages domain／環境／branch protection 是帳戶設定，不可由檔案缺少推論沒有配置。全部文字來源已讀取並掃描 metadata／標題／連結，圖片只稽核檔名／大小，未聲稱逐張視覺審核。

## SEO 與 Analytics 實際輸出

62 份 HTML（含 landing／轉址）：每份只有 1 個 canonical；59 個 JSON-LD script 均可 JSON parse，並非 Google rich result eligibility 保證。51 BlogPosting；Organization/Person 各 56；FAQPage 3（首頁＋兩篇文）；Service 2；AboutPage/ContactPage/CollectionPage/WebSite 各 1。未見 BreadcrumbList；`free.html` 沒 JSON-LD。

H1：60 份 HTML 各 1 個、landing 0 個、privacy 2 個。隱私頁藉 Minima page → 本地 default 使用共用 head，description 為站級 fallback；應修雙 H1 與專屬描述。兩篇文章 FAQ 類型需人工確認與可見問題答案一致；不能承諾 FAQ rich results。

共享 head 有 GTM `GTM-PNKDN6F6`、直接 GA4 `G-V656NSBTJR`；免費頁只有直接 GA4。容器內容／事件去重／Consent Mode／cookie 行為未取得帳戶或瀏覽器證據。ads.enabled=false 不阻止共用 head 載入 AdSense JS。robots 允許全站與 OAI-SearchBot，引用正式 sitemap。sitemap 配置的自定 include/exclude 欄位是否受插件支援不能只看 YAML，本次以 57 個實際 loc 為準。

## 外部連結稽核

來源中的外部地址分為社群／轉換、追蹤／字體／廣告、文章參考、編輯來源。以下為完整非本地 hostname 清單（同網域內不同頁見原碼），未執行表單送出或訂閱。URL 字串掃描與生成頁 anchor 的本地目標檢查完成；目前可接受 `.html` 主機別名推導，未發現確定缺檔的內部 anchor 目標。未做正式外連可達性保證。

| Host | 來源舉例 | 狀態／注意 |
| --- | --- | --- |
| `about.fb.com` | `_posts/2026-10-19-threads-no-traffic-shadowban.md` | 僅原碼盤點；未逐條網路請求 |
| `app.notion.com` | `_posts/2026-10-10-k-uncle-friends.md` | 僅原碼盤點；未逐條網路請求 |
| `blog.hootsuite.com` | `_posts/2026-10-29-threads-no-engagement-positioning.md` | 僅原碼盤點；未逐條網路請求 |
| `fonts.googleapis.com` | `assets/css/style.css` | 僅原碼盤點；未逐條網路請求 |
| `fonts.gstatic.com` | `free.html` | 僅原碼盤點；未逐條網路請求 |
| `forms.gle` | `_includes/head.html` | 未送出；需 sandbox／帳戶核實 |
| `help.instagram.com` | `_posts/2026-10-19-threads-no-traffic-shadowban.md` | 僅原碼盤點；未逐條網路請求 |
| `kenhai-n8n.hf.space` | `free.html` | 未送出；需 sandbox／帳戶核實 |
| `pagead2.googlesyndication.com` | `_includes/head.html` | 僅原碼盤點；未逐條網路請求 |
| `portaly.cc` | `_config.yml` | 僅原碼盤點；未逐條網路請求 |
| `schema.org` | `_includes/head.html` | 僅原碼盤點；未逐條網路請求 |
| `www.aboutads.info` | `privacy.md` | HTTP 連結，建議核實 HTTPS 替代；未改動 |
| `www.google.com` | `privacy.md` | 僅原碼盤點；未逐條網路請求 |
| `www.googletagmanager.com` | `_includes/head.html` | 僅原碼盤點；未逐條網路請求 |
| `www.instagram.com` | `_config.yml` | 僅原碼盤點；未逐條網路請求 |
| `www.socialmediatoday.com` | `_posts/2026-10-19-threads-no-traffic-shadowban.md` | 僅原碼盤點；未逐條網路請求 |
| `www.threads.com` | `_posts/2026-10-19-threads-no-traffic-shadowban.md` | 僅原碼盤點；未逐條網路請求 |
| `www.threads.net` | `README.html` | 僅原碼盤點；未逐條網路請求 |

主站 `runing9to5.com` 的 robots GET 與 GitHub API 均遭本環境政策拒絕；不能把 403 當成網站故障。Cloudflare 官方資料透過其 GitHub 原始文件唯讀取得。無 Search Console、GA4、n8n workflow 或 Forms 回應資料，索引／寄送／退訂／付款可用性皆未驗證。
