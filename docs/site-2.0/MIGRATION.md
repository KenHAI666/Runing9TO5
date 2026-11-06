---
published: false
---
# 託管遷移、外部服務與回復計畫

結論：Jekyll 靜態輸出具備遷移基礎，尚未證明 Cloudflare 線上相容。Phase 0 沒有建立 Pages 專案、預覽、DNS 或部署。正式站仍維持原設定。

## 已查閱官方資料（2026-11-06）

官方網站直接讀取受網路政策拒絕，以下透過 Cloudflare 官方 `cloudflare/cloudflare-docs` production 分支取得；文件可能變動，實作前重查，不以舊指南的預設 Ruby 版本作保證。

- [Jekyll framework guide](https://developers.cloudflare.com/pages/framework-guides/deploy-a-jekyll-site/)：Gemfile、Ruby 版本設定與 `_site` 輸出。
- [GitHub Pages Jekyll migration](https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/)：可沿用 github-pages gem；先建立獨立專案，再另決定自訂網域。
- [Build image](https://developers.cloudflare.com/pages/configuration/build-image/)：工具版本可設定，preview／production 必須一致鎖定。
- [Serving Pages](https://developers.cloudflare.com/pages/configuration/serving-pages/)：HTML 副檔名正規化；沒有根 404.html 時可能當 SPA，未知路由回首頁。
- 原始文件：[jekyll](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/pages/framework-guides/deploy-a-jekyll-site.mdx)、[migration](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/pages/migrations/migrating-jekyll-from-github-pages.mdx)、[serving](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/pages/configuration/serving-pages.mdx)。

## 相容性矩陣

| 面向 | 目前證據 | 遷移驗收門檻 |
| --- | --- | --- |
| Jekyll／Liquid | 無自定外掛，github-pages + minima | 相同 lockfile／Ruby 建置，所有插件確實載入 |
| assets／文章 | 靜態檔與明確 permalink | 完整公開路由逐條 diff，圖片／字型正常 |
| `.html` canonical | about/contact 等預設輸出 html | 正規化不得造成 canonical 不同、迴圈或 redirect chain |
| canonical `/free` | Jekyll 實際寫出 `/free.html`，`/free/` 是 redirect | 預覽驗 `/free` 與 `.html` 正規化、text/html、200 與 canonical 一致 |
| jekyll-redirect-from | 產生 HTML refresh 頁，非 HTTP 301 | 測現有別名與未來 `_redirects` 衝突，避免 `/free/` 迴圈 |
| Sitemap／Feed | 插件 build-time 產生 | 舊 canonical 保留，預覽不進索引 |
| 404 | repo 無根 404 | 新增真正 404 page，未知路由不得回 200 首頁 |
| 訂閱／諮詢 | 外部服務，非 Pages 後端 | 預覽預設隔離；sandbox CORS／timeout／duplicate／429 測完 |
| 分析／廣告 | 正式 ID 寫在模板 | 預覽禁正式追蹤、禁廣告，避免資料污染 |
| 每日發布 | GitHub schedule 會重建 | Cloudflare Git push 觸發不會自行每天重建；另選排程 |

建置命令提案 `bundle exec jekyll build --trace`，輸出 `_site`，root 為 repository 根目錄；Ruby／Bundler／Jekyll 依鎖定結果設定，不能把本地 Ruby 3.3 驗證等同現 CI Ruby 3.2 已驗證。初次 Cloudflare 只用獨立 preview 專案，不接正式域名與正式部署分支。

## 未來文章與排程

目前 `.github/workflows/jekyll-deploy.yml`：push main、workflow_dispatch、每日 `10 23 * * *`。台北時間為隔日 07:10，非午夜；排程可能延遲，不能承諾精準 07:10。`future: false`、Asia/Taipei：未來文章需等到日期／時間到且有成功 rebuild；`_drafts` 不會自動移入 `_posts`。11/09 預定文目前不該出現在列表、feed 或 sitemap。

Phase 4 可提案保留 GitHub 排程做 Cloudflare build hook，或另核准 Worker Cron／CI 上傳。build hook URL 視為機密放 Secrets、不進公開 repo；須處理時區、失敗警報、重試、並行與回復。不得為了測試而觸發現在正式 workflow_dispatch。新版 PR 應分開 build-only 與 deploy，避免 review branch 寫正式 Pages。

## 路由決策

`/resources/` 已是免費頁別名，選項須核准：A 保持舊 redirect、資源中心暫用其他路徑；B 讓 `/resources/` 成為中心，明確承認舊書籤行為改變，保留 prominent `/free` CTA 並遷移追蹤。不能同時生成同一路徑的集合 index 與 redirect page。

Cloudflare 可能 `/contact.html` → `/contact`，現有 `/contact/` HTML redirect 又指回 `/contact.html`；必須先測最終 canonical 與 slash 路徑，選定一次跳轉矩陣。禁止全站一律補 slash 的 blanket redirect。

## 分階段切換與回復

1. 核准前只保存提案；先匯出目前 Pages 設定、DNS records/TTL、網域驗證、redirect、基線 commit 與成功 artifact，由授權者安全保存。
2. 獨立預覽：固定 lockfile、相同內容建置，加入 noindex header／robots disallow／必要 access protection，不把預覽 URL 提交 sitemap；robots disallow 本身不能保證不被索引。
3. 全路由、HTTP status、canonical、sitemap、Feed、404、訂閱 sandbox、手機、a11y、性能與排程驗證；正式站 read-only spot check 需網路允許。
4. 提交證據、差異與回復演練供 K叔核准；只有核准後才能新增 custom domain、DNS／nameserver、正式 Secrets 與正式排程切換。
5. 切換期保留 GitHub Pages 舊 artifact／設定，不同時讓兩邊排程產生不同版本；釐清唯一發布來源。
6. 若核心路由 404／迴圈、canonical 大量錯誤、訂閱交付失敗或排程漏發：停止新發布；由授權者恢復舊 DNS/Pages 設定與已知正常 artifact，保留事故證據。DNS 回復受原 TTL 影響，不能保證立即生效。
7. 驗證首頁、至少新舊文章各一、所有重要別名、free/contact/privacy、sitemap/feed/404 與經核准的訂閱測試後結案。

文件 PR 若需回復：關閉未合併 PR 即可；已合併則走 revert PR，不 reset main、不 force push。功能 PR 也採逐一 revert，不刪舊內容補救。

## 外部服務與費用（未核實不列固定金額）

| 服務 | 現況／用途 | 費用項目與待查事項 |
| --- | --- | --- |
| GitHub Pages / Actions | 現部署 YAML 可見，帳戶設定未取得 | 帳戶方案、Actions 額度／分鐘、儲存與 artifact 保留 |
| Cloudflare Pages | 尚未建立 | 建置次數／並行、流量／資產限制、Functions／Access 費用，待帳戶方案核實 |
| 網域／DNS | 原碼設定 runing9to5.com，無 CNAME 檔 | 註冊續費、目前 DNS 供應商；不假定 Cloudflare 接管 |
| n8n / Hugging Face Space | 原碼 Webhook host 可見，未呼叫 | 主機運算、休眠冷啟動、備份、流量、可用性與安全維護 |
| 寄信供應商 | repo 無後端證據；隱私頁提 Kit 不構成已串接證據 | 訂閱人數、寄件量、網域驗證、退訂與 double opt-in，需流程持有者確認 |
| Google Forms | 諮詢外連已存在，未送表 | 帳戶／Workspace、表單存取、資料保留；不等於有金流 |
| GA4 / GTM / Search Console | 前兩者 ID 存在，GSC 未見 | 帳戶權限、同意工具、分析維護；不猜已產生費用 |
| Google Fonts / AdSense | 原碼載入 | 字型隱私／效能；廣告審核與收益未核實 |
| 學院後端、DB、會員認證、金流、影片、Email | 都未選型 | 月費、交易手續費、稅務、儲存／轉碼／流量、備份／監控；Phase 5 另核准 |

沒有提供固定總成本，沒有購買或試用付費服務。
