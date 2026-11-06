---
published: false
---
# QA｜Phase 0 證據與後續驗收

核對日為 2026-11-06（Asia/Taipei）。程式基線為 main `13dbdce7b730df5df0f9c591c41b956d4fc9bc92`。初版盤點與固定時鐘、訂閱 fetch stub 的測試細節保留於 [PR #40](https://github.com/KenHAI666/Runing9TO5/pull/40)。

## 證據與驗證範圍

| 檢查 | 結果 | 證據／範圍 |
| --- | --- | --- |
| 原始碼與既有盤點 | 52 篇文章、19 份草稿、2 layouts、5 includes、1 份站方 CSS、10 張圖片、無獨立 JS | Git 追蹤樹、文章 front matter 和建置輸出。另有 `_posts/post.html` 非標準文章檔。前次文章與模板基線至此次 main 的差異只有八份文件 |
| 正式建置／部署 | build、deploy 皆成功 | 11/06 台北 11:39 啟動的既有 [Actions run](https://github.com/KenHAI666/Runing9TO5/actions/runs/42157839818)，Ruby 3.2.11、github-pages 233、Jekyll 3.10.0、Minima 2.5.1 |
| 正式路由 | 80 個 artifact 檔案均可取回。138 個有對應檔案的 HTTP 路徑皆 200，回應內容逐 byte 相同 | 155 個 path 探測含實體檔、目錄路徑、已知別名、404 與待新增路由。另測 51 個文章的無斜線別名，都經單次 HTTP 轉址回原路徑 |
| Sitemap／Feed | 正式 sitemap 與 artifact 內容相同，57 個 loc 皆 200 且 canonical 相符。Atom feed 有 10 筆 | sitemap 51 篇＋6 頁。feed 是近期文章摘要；兩者皆未出現 docs、草稿或 11/09 待發布文章 |
| SEO／Schema | 62 個 HTML 各一 canonical，59 個 JSON-LD script 解析成功；privacy 雙 H1 | 語法與輸出稽核。正式索引率、Google Search Console、Rich Results eligibility、GTM／GA4 事件及 Cookie 行為未驗證 |
| 內外連結 | 產物中的既有站內片段未發現確定缺錨點；12 個去重後的公開外站 anchor 皆最終 200 | Google Ads 設定落到 Cookie 阻擋說明，列待複核。Forms 僅讀表單頁，社群 200 可能包含登入或動態載入 |
| 排程 | 10/30–11/06 的 8 次成功，台北 10:07–11:54 啟動 | 定義是 07:10，兩者有延差；本次唯讀查歷史。初版曾以固定時鐘跨過 11/09 00:00，確認下一篇只在到期後進入站點、feed、sitemap |
| 訂閱 | 讀到與前端端點相符的 n8n 已發布流程，確認節點及回應分支 | 不觸發 webhook、寄信、退訂或像素，也未讀名單、個別執行或試算表資料 |
| Phase 0 文件隔離 | 固定時鐘、本地基線與文件分支均輸出 80 檔，逐 byte 相同 | macOS Ruby 3.1.7、github-pages 232、Jekyll 3.10.0。測的是文件可見性與輸出等價，正式依賴版本以部署 run 為準 |
| Cloudflare | 官方文件查證及相容性矩陣 | Phase 4 再驗證實際 preview、HTTP 正規化、DNS 回復與排程 |

正式站抽測包含 sitemap、feed、robots、根頁與文章、樣式與圖檔，以及 `/free`、`/resources/`、`/contact`、`/landing`。結果詳見 [ROUTE-INVENTORY.md](ROUTE-INVENTORY.md)。

## 訂閱流程與錯誤處理

| 階段 | 已看到的配置 | 待驗證或修正 |
| --- | --- | --- |
| 前端輸入與提交 | 兩份表單只有非空檢查，Email 欄位用 text。JS 接管後送 JSON，提交期間停用按鈕。 | 將 JS 未載入、初始化失敗與鍵盤 Enter 納入測試。兩份 form 缺 method/action，瀏覽器原生 GET fallback 可能把姓名與 Email 帶進 URL。此項為靜態程式判定。 |
| n8n 接收 | 已發布配置判斷 Email 是否非空。無 Email 的分支為 400 JSON `success: false`。 | Email 正規化與格式驗證、CORS、同意、限流與防濫用以核准的 sandbox 驗證。 |
| 儲存與寄送 | 非空分支先寫 Google Sheets，再呼叫 Resend 寄 Day 0。正常回應為 200 JSON `success: true`。 | 寫入成功後若寄送失敗，重試可能重複留下資料或寄送。針對同址重複、並行、部分失敗及重試做冪等與補償測試。 |
| 瀏覽器結果 | `res.ok` 即換成成功文案。非 2xx 或 fetch reject 會恢復按鈕並 alert。 | 讀取 JSON、區分錯誤原因、加 timeout 與可存取狀態提示。現行流程中未見確認信／點擊確認步驟，前端應描述實際完成狀態。 |
| 後續交付 | 有排程寄送、Kit 更新、退訂及開信像素。程式用台北日期計算，排程節點設 09:00。 | n8n workflow 未顯式覆寫 timezone，需查 instance 時區與實際寄送時間。另由帳戶持有者查送達、退訂、資料保留及告知內容。 |

初版使用兩個表單各 7 個 fetch stub 情境，覆蓋空姓名、空 Email、200、500、網路拒絕、錯誤 Email 及 200 但邏輯失敗。200／false 是負向測試，實際配置的空 Email 分支回 400。收件、郵件供應商接受、信箱送達、退訂及 Kit 同步須分別驗收。

## 重現文件隔離

在獨立 checkout 用現有 Gemfile 的副本解析測試依賴，lockfile 放在 checkout 外。於基線與文件分支各自的 source 根目錄，用同一套 Ruby／Bundler 執行下列命令。將 `BUNDLE_GEMFILE` 指向 checkout 外的 Gemfile。額外 config 固定 `time: 2026-11-06 12:00:00 +0800`，指定 `repository: KenHAI666/Runing9TO5`，避開 build 時鐘造成的 CSS query 差異。

```sh
JEKYLL_ENV=production bundle exec jekyll build --trace \
  --config "_config.yml,$AUDIT_CLOCK_CONFIG" --destination "$AUDIT_OUTPUT"
diff -qr "$BASELINE_OUTPUT" "$DOCS_OUTPUT"
```

## 後續 PR 驗收

- [ ] 建立無正式 Secrets 或部署權限的 PR build-only；審查通過後另案啟用 main 必過檢查。
- [ ] 比對 80 個 artifact 檔與 57 個 canonical loc，檢查 feed、已知別名、日期邊界與草稿排除。
- [ ] 完成 320/375/768/1280px、200% zoom、鍵盤與螢幕閱讀器、reduced-motion／無 JS，記錄 axe 與 Lighthouse。
- [ ] 核對 canonical／OG／JSON-LD／單 H1 與可見內容；預覽加存取保護與 noindex，停用正式追蹤及表單提交。
- [ ] 訂閱 sandbox 覆蓋無 JS 不洩漏、資料格式、CORS、重複與並行、400/429/500、逾時、寫入後寄送失敗、送達及退訂。
- [ ] Cloudflare 核對 slash、.html、中文 percent encoding、404、redirect chain／loop、MIME、cache；演練 scheduled rebuild 與回復。
- [ ] 學院、會員與金流等 Phase 5 核准後再測。
