---
published: false
---
# QA｜Phase 0 證據與後續驗收

日期：2026-11-06（Asia/Taipei）；基線 `b951dfc0657ff43e2edc8f4468cfec4de0d8268b`；分支 `docs/site-2.0-phase-0`。此文件區分本次實測、已確認缺口、未執行與後續計畫。文件不是正式部署或外部服務可用性的保證。

## 本次執行結果

| 檢查 | 結果 | 證據／限制 |
| --- | --- | --- |
| 原始碼／資料盤點 | 通過 | 全部文字來源讀取、metadata／標題／連結掃描；52 篇、19 草稿、2 layouts、5 includes、1 CSS、10 圖片；無獨立 JS |
| 原始 YAML | 通過 | 文章／草稿／頁面 front matter 均可解析 |
| Ruby／Bundler 安裝 | 通過 | 本機原無 Ruby、無 sudo；官方 APT 簽章索引驗證後解壓工具於 checkout 外，Ruby 3.3.8／Bundler 2.5.22 |
| Gemfile 依賴安裝 | 通過 | 原 Gemfile 副本於外部驗證目錄；github-pages 233、Jekyll 3.10.0；未改 repository Gemfile 或新增 lockfile |
| RubyGems 連線 | 已診斷／修正本地設定 | index.rubygems.org 被拒；使用政策已允許的官方 www.rubygems.org mirror 成功，未停用 TLS／checksum |
| Jekyll 基線 build | 通過 | 在 source 根目錄執行，以固定台北 11/06 12:00 建置，80 個輸出、51 篇文章 |
| 文件分支 build | 通過 | 8 份文件 `published:false` 不輸出，和固定時鐘基線 80 檔逐 byte 相同（最終檢查） |
| HTML canonical | 通過 | 62 份 HTML 各 1 canonical；含 redirect 與 landing；未驗證正式 HTTP 正規化 |
| JSON-LD | 語法通過 | 59 個 script 可 JSON parse；51 BlogPosting，其他類型見路由文件；未跑 Google Rich Results／Schema 遠端 validator |
| Sitemap | 通過 | XML 可解析、57 個正式站 loc，51 文章＋6 主頁；無 docs／draft／未來文章 |
| 未來發布邊界 | 通過 | 時鐘 11/08 23:59:59 +08:00：51 篇；11/09 00:00:01：52 篇，新增 ai-copywriting-human-review，feed/sitemap 同步；兩次皆無草稿 |
| 本地 HTTP | 通過 | 臨時靜態伺服器讀全部 80 檔，均 200 且內容相同；free.html MIME=text/html，未知路由 404；不代表正式／Cloudflare 也相同 |
| 本地站內目標 | 未發現確定缺檔 | 檢查生成 anchor 的本地檔／index／.html 候選；無副檔名別名取決於正式主機，未測所有 fragment anchor |
| 訂閱離線模擬 | 通過 14 個觀察情境 | 每個表單：空姓名、空 email、200、500、網路 reject、無效 email、200 邏輯失敗 body。測試確認現況，非宣稱缺陷已修 |
| Python 語法 | 通過 | 3 個 scripts AST parse；未啟動 Flask |
| Notion 匯入 fixture | 通過 | dry-run＋寫入 checkout 外 output-dir；核對 permalink/layout；無 git 或正式資料操作 |
| 文件／Git 邊界 | 通過 | 僅八個 docs/site-2.0 Markdown；既有程式、文章、設定、workflow、lockfile 未變；清除本次 Sass cache |
| Cloudflare 研究 | 通過來源查閱 | 官方 cloudflare-docs production 分支四份文件；沒有建立預覽或線上驗證 |
| 正式站／外連逐條可達性 | 未執行完成 | 正式 robots GET 被環境網路政策拒絕 403，不是判定正式站故障；未點表單、未呼叫 webhook |
| PR API | 阻擋 | 既有 GitHub 認證的 gh api 與 curl API 都被環境拒絕；未要求或新增 token。分支推送與審核方式以交付訊息為準 |

第一次程式化基線 build 在錯誤工作目錄出現 layout read warning，該輸出未當作合格證據；改在 source 根目錄重建後無該 warning。Ruby 3.3 本地成功不等同現有 CI Ruby 3.2 已實跑；Phase 1 必須對齊版本。

## 訂閱流程與錯誤處理稽核

現況：hero／底部兩個 form → trim／非空檢查 → disabled 按鈕 → POST `{name,email}` JSON 到既有 n8n → HTTP ok 則替換 form zone；非 2xx 或 reject 會恢復按鈕並 alert。Content-Type application/json 跨來源需要 OPTIONS/CORS，後端設定不在 repo，未驗證。

離線測試使用 Node vm、最小 DOM stub 與替換 fetch，沒有任何網路呼叫。每個 form 各 7 情境，共 14：

1. 空姓名阻擋、focus 姓名；空 email 阻擋、focus email。
2. 200：傳正確 JSON、顯示訂閱成功。
3. 500 與 fetch reject：恢復可送狀態、顯示失敗。
4. **確認缺陷**：not-an-email 仍送出（type=text、無格式驗證）。
5. **契約缺口**：即使 200 回應 body 表示 success:false，也顯示成功；尚未證實真實後端使用此 body 契約。

尚缺：AbortController／timeout（未完成請求可能一直 disabled）、可見 label、type=email／autocomplete、錯誤 inline/live region、確認信待確認狀態、防 bot／限流／冪等／重複訂閱策略。後三項需查後端，不因前端缺碼就推論後端不存在。成功送出、已寄信、已確認訂閱與免費檔案交付必須分開驗收。

未做 CORS preflight、實際寄信／退訂、n8n availability 或重複訂閱測試，因會接觸正式流程且沒有 sandbox 授權。後續只用 K叔核准的測試端點與專用測試信箱。

## 現況缺口與非故障

- privacy 有 2 個 H1，description 採全站 fallback；其他 HTML H1 分布見 ROUTE-INVENTORY。
- GA4/GTM 同存是重複追蹤風險，未取得 GTM 容器，不能斷言已重複計量。
- Service／Offer 的既有 NT$1,000、InStock 需商業確認，不能直接擴散到新模型。
- 未發現根 404；本地 Python 的 404 不代表 Cloudflare 會回真 404。
- `/free.html` 確實存在，canonical 是 `/free`；不得報成 404。`/resources/` 是既有 redirect，不能當未占用路徑。
- 流程中未執行 Flask `/publish`，其直接 main push 為靜態程式證據；沒有測試推送正式分支。

## 重現本次驗證

本機工具、Gemfile 副本、鎖定解析與測試 helper 保存在 `/workspace/site2-tooling/`、`/workspace/site2-validation/`，都在 Git checkout 外，不是網站部署資產。工具不保證已在新工作階段快照還原；本次沒有發布雲端環境版本。

```sh
cd /workspace/Runing9TO5
. /workspace/site2-tooling/activate.sh
export BUNDLE_APP_CONFIG=/workspace/site2-validation/bundle-config
export BUNDLE_GEMFILE=/workspace/site2-validation/Gemfile
bundle check
bundle exec ruby /workspace/site2-validation/build-audit.rb /workspace/Runing9TO5 /workspace/site2-validation/docs-site /workspace/site2-validation/docs-routes.json 2026-11-06T12:00:00+08:00
node /workspace/site2-validation/check-subscription.cjs
python3 /workspace/site2-validation/audit-output.py
```

`audit-output.py` 檢查 baseline-site；build-audit 必須從對應 source 根目錄執行。一般新開發者先裝與 CI 對齊的 Ruby/Bundler，在 checkout 外複製 Gemfile、安裝依賴並指定 BUNDLE_GEMFILE；正式 lockfile 由另一個經審核 PR 納入。每個雲端任務已隔離，沿用 checkout，除非使用者明確要求，不另建 worktree。

## 後續 PR 的必要 QA（未執行）

- [ ] PR build-only 成功、權限最小化、無正式 Secrets／deploy。
- [ ] 已公開 80 個輸出與 sitemap loc 差異審核，未來／草稿保持不公開。
- [ ] 320/375/768/1280px、200% zoom、鍵盤與螢幕閱讀器、reduced-motion／無 JS；axe 與 Lighthouse 記錄基準。
- [ ] Canonical／OG／JSON-LD／單 H1／描述與可見內容一致，預覽 noindex 且不送正式追蹤。
- [ ] 訂閱 sandbox：成功／待確認、重複、無效資料、500、429、逾時、離線、CORS，確認不洩漏 PII。
- [ ] Cloudflare HTTP 路由矩陣：含 slash、.html、中文 percent encoding、unknown 404、redirect chain／loop、MIME／cache。
- [ ] 經核准排程在台北日期邊界發布、監控與回復演練。
- [ ] 真實金流／會員／學院測試另待 Phase 5 技術與商業核准。
