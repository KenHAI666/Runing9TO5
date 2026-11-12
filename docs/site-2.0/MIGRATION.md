---
published: false
---
# 託管遷移、外部服務與回復計畫

Jekyll 靜態輸出具備遷移基礎。相容性結論依正式 GitHub Pages 產物與 Cloudflare 官方規格，Cloudflare 線上驗收排在 Phase 4。

## 已查閱官方資料（2026-11-06）

已查 Cloudflare 官方規格。指南的 Ruby 版本只是範例，Phase 4 以實際 CI 依賴和 build image 測試決定版本。

- [Jekyll framework guide](https://developers.cloudflare.com/pages/framework-guides/deploy-a-jekyll-site/)：Gemfile、Ruby 版本設定與 `_site` 輸出。
- [GitHub Pages Jekyll migration](https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/)：可沿用 github-pages gem；先建立獨立專案，再另決定自訂網域。
- [Build image](https://developers.cloudflare.com/pages/configuration/build-image/)：工具版本可設定，preview／production 必須一致鎖定。
- [Serving Pages](https://developers.cloudflare.com/pages/configuration/serving-pages/)：HTML 副檔名正規化；沒有根 404.html 時可能當 SPA，未知路由回首頁。
- [Custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)、[Previews](https://developers.cloudflare.com/pages/configuration/preview-deployments/)、[Deploy Hooks](https://developers.cloudflare.com/pages/configuration/deploy-hooks/)、[Rollbacks](https://developers.cloudflare.com/pages/configuration/rollbacks/)、[Limits](https://developers.cloudflare.com/pages/platform/limits/) 提供網域、存取、排程和回復規則。

## 相容性矩陣

| 面向 | 目前證據 | 遷移驗收門檻 |
| --- | --- | --- |
| Jekyll／Liquid | 無自定外掛，github-pages + minima | 相同 lockfile／Ruby 建置，所有插件確實載入 |
| assets／文章 | 靜態檔與明確 permalink | 完整公開路由逐條 diff，圖片／字型正常 |
| `.html` canonical | `/about.html` 與 `/contact.html` 為正式 canonical，無副檔名路徑也回 200 | 正規化不得造成 canonical 不同、迴圈或 redirect chain |
| canonical `/free` | Jekyll 實際寫出 `/free.html`，`/free/` 是 redirect | 預覽驗 `/free` 與 `.html` 正規化、text/html、200 與 canonical 一致 |
| jekyll-redirect-from | 產生 HTML refresh 頁，非 HTTP 301 | 測現有別名與未來 `_redirects` 衝突，避免 `/free/` 迴圈 |
| Sitemap／Feed | 插件 build-time 產生 | 舊 canonical 保留，預覽不進索引 |
| 404／舊 landing | GitHub 未知路徑回 404，repo 無根 404 頁；`/landing` 是 octet-stream | Cloudflare 根 `404.html`、未知路徑回真 404；`/landing` 試行單次 HTTP 跳到 `/free` |
| 訂閱／諮詢 | 外部服務，非 Pages 後端 | 預覽預設隔離；sandbox CORS／timeout／duplicate／429 測完 |
| 分析／廣告 | 正式 ID 寫在模板 | 預覽禁正式追蹤、禁廣告，避免資料污染 |
| 每日發布 | GitHub schedule 會重建 | Cloudflare Git push 觸發不會自行每天重建；另選排程 |

建置命令提案 `bundle exec jekyll build --trace`，輸出 `_site`，root 為 repository 根目錄；Ruby／Bundler／Jekyll 依鎖定結果設定，並在 Cloudflare 預覽確認建置。正式 Actions 依賴為 Ruby 3.2.11、github-pages 233、Jekyll 3.10.0；預覽先嘗試同版本，若 build image 無法重現，改由 CI 建置後 Direct Upload 作為候選。初次 Cloudflare 只用隔離專案及受保護的測試分支。

## 未來文章與排程

目前 `.github/workflows/jekyll-deploy.yml`：push main、workflow_dispatch、每日 `10 23 * * *`。台北時間為隔日 07:10。10/30–11/06 的 8 次排程都成功，實際於台北 10:07–11:54 啟動，比設定晚 2 小時 57 分至 4 小時 44 分。以歷史成功 run 作觀察基線，實際發布時限仍待 K叔決定。 [GitHub 排程規格](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

`future: false`、Asia/Taipei：未來文章需等到日期／時間到且有成功 rebuild；`_drafts` 不會自動移入 `_posts`。11/09 預定文目前不該出現在列表、feed 或 sitemap。

Phase 4 候選 A 為 GitHub 排程觸發 Cloudflare build hook，適合沿用 Git integration。候選 B 為 CI 定時建置、Direct Upload，適合需要固定建置環境與產物重用的情況。Cloudflare Git 專案與 Direct Upload 專案的設定需在選型時確認。Hook URL 或上傳憑證放環境 Secrets。排程須驗證重試、超過發布時限的告警、並行序列化與舊版產物防覆蓋。預覽演練採獨立工作流程。

## 路由決策

`/resources/` 已是免費頁別名，選項須核准：A 保持舊 redirect、資源中心暫用其他路徑；B 讓 `/resources/` 成為中心，明確承認舊書籤行為改變，保留 prominent `/free` CTA 並遷移追蹤。不能同時生成同一路徑的集合 index 與 redirect page。

Cloudflare 會將 HTML 檔路徑正規化為 extensionless。預覽先查能否保留目前的 canonical；若 `/contact.html`、`/about.html` 必須改為 extensionless，須由 K叔核准對照表，同步修改 canonical、OG、JSON-LD、sitemap 與內連。對 `/contact/`、`/free/`、`/landing` 及舊資源別名，優先驗證每條一跳到核准目的地。

## 分階段切換與回復

1. 由授權者保存目前 Pages 設定、環境規則、完整 DNS zone／TTL／DNSSEC、redirect、基線 commit 和成功 artifact。現有 apex NS 為 registrar-servers.com，公開 DNS 可見郵件 MX，`www` CNAME 指向 GitHub Pages。若以 Cloudflare Pages 綁 apex，依官方要求需 Cloudflare zone 及 nameserver；先核對 MX、SPF、DKIM、DMARC 與驗證記錄，避免網站切換影響郵件。
2. 在獨立 `pages.dev` 專案，以固定 lockfile 建置相同內容。確認預覽 `X-Robots-Tag: noindex`，並在外部可達前加 Access 或等效登入保護。Cloudflare 預覽預設有 noindex，仍需實測分支 alias、個別部署網址及專案主網址的保護。預覽關閉正式追蹤及表單提交。
3. 全路由、HTTP status、canonical、sitemap、Feed、404、訂閱 sandbox、手機、a11y、性能與排程驗證；正式站 read-only spot check 需網路允許。
4. 提交證據、差異與回復演練供 K叔核准；只有核准後才能新增 custom domain、DNS／nameserver、正式 Secrets 與正式排程切換。
5. 切換期保留 GitHub Pages 舊 artifact／設定，不同時讓兩邊排程產生不同版本；釐清唯一發布來源。
6. 任一 sitemap canonical 未如預期回傳 200、核心入口有轉址迴圈、經核准的訂閱驗收失敗或超過約定發布時限，即暫停新發布。若是 Cloudflare 產物問題，授權者先回復最近的已知正常 production 部署；若是主機或 DNS 問題，優先在當時具權威的 DNS zone 恢復 GitHub Pages 來源。必要時才按原記錄回復 NS／DNSSEC。依 TTL 檢查多個 resolver，並確認信箱相關記錄與 TLS。
7. 驗證 HTTPS apex／www、首頁、57 個基準 canonical（加上切換後合法新增項）、重要別名、free/contact/privacy、sitemap/feed/404、郵件 DNS 及核准的訂閱測試。經授權再恢復唯一排程，確認下一篇的建置與發布。

文件 PR 若需回復：關閉未合併 PR 即可；已合併則走 revert PR，不 reset main、不 force push。功能 PR 也採逐一 revert，不刪舊內容補救。

## 外部服務與費用（未核實不列固定金額）

| 服務 | 現況／用途 | 費用項目與待查事項 |
| --- | --- | --- |
| GitHub Pages / Actions | GitHub API 已確認 workflow 部署、HTTPS 與 main 部署限制 | 帳戶方案、Actions 額度／分鐘、儲存與 artifact 保留 |
| Cloudflare Pages | 尚未建立 | 官方 Free 公開限制為每月 500 次 build、同時 1 次、20,000 檔、單檔 25 MiB。這些是方案上限，帳戶資格、Access／Functions、計量和實際支出另核實。 [Cloudflare Limits](https://developers.cloudflare.com/pages/platform/limits/) |
| 網域／DNS | GitHub Pages 設定已確認正式域名，公開 DNS 仍以 registrar-servers.com 為權威 | 註冊續費、目前 DNS 供應商；不假定 Cloudflare 接管 |
| n8n / Hugging Face Space | 原碼 Webhook host 可見，未呼叫 | 主機運算、休眠冷啟動、備份、流量、可用性與安全維護 |
| Google Sheets／Resend／Kit | n8n 已發布配置可見儲存、首封／後續寄送與 Kit 更新 | Sheets 帳戶與 API 配額、Resend 寄件量、Kit 訂閱人數、寄件域名驗證與退訂維護，方案和實際用量由持有者核實 |
| Google Forms | 諮詢外連已存在，未送表 | 帳戶／Workspace、表單存取、資料保留；不等於有金流 |
| GA4 / GTM / Search Console | 前兩者 ID 存在，GSC 未見 | 帳戶權限、同意工具、分析維護；不猜已產生費用 |
| Google Fonts / AdSense | 原碼載入 | 字型隱私／效能；廣告審核與收益未核實 |
| 學院後端、DB、會員認證、金流、影片、Email | 都未選型 | 月費、交易手續費、稅務、儲存／轉碼／流量、備份／監控；Phase 5 另核准 |

沒有提供固定總成本，沒有購買或試用付費服務。
