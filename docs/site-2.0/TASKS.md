---
published: false
---
# 分階段任務與審核閘門

Phase 0 已整理為文件審查。每個後續 PR 都須附路由差異、驗收及回復方式。正式操作與帳戶設定需另核准。

## Phase 0

- [x] 取得 main 基線，建立文件分支，列舉並讀取文字來源、內容 metadata 與圖片大小。
- [x] 八份指定文件：目標、架構、設計、資料、路由、遷移、任務、QA。
- [x] 沿用 fetch stub 結果，唯讀核對已發布 n8n 節點、錯誤回應與寄送依賴。
- [x] 核對正式 artifact、路由／外連、排程歷史及 Pages／main 保護狀態。
- [x] 查閱 Cloudflare 官方來源，記錄路由與排程相容性風險。
- [ ] K叔審閱、接受 Phase 0 結論並另行核准 Phase 1。

## Phase 1 精確任務（核准後依序 PR）

| 任務／PR | 檔案範圍（建議） | 驗收 | 依賴 |
| --- | --- | --- | --- |
| P1-01 建置基線與 PR 安全 | Gemfile/Gemfile.lock、.ruby-version、.github/workflows/jekyll-pr.yml、scripts/server.py、README.md、scripts/READ ME | 與正式 CI Ruby 一致；PR 無部署權限及正式 secrets；匯出／寫文到分支並人工開 PR；快照比對 57 個 canonical 與所有別名 | K叔核准啟動 Phase 1、BUILD-01/GOV-01；PR check 出現後另核准 main protection |
| P1-02 Tokens | 新 tokens.css、style.css、default.html | 現有 var 相容；色彩／spacing／focus tokens；對比量測與 mobile 截圖 | 配色核准、P1-01 |
| P1-03 Header/Footer | 現 header/footer、navigation.js、components.css、default.html | skip link、aria-current、鍵盤／Escape／focus、無 JS 連結、320px 不溢出；入口不變 | P1-02 |
| P1-04 Buttons/Cards | ui/button.html、ui/card.html、components.css、選定既有頁 | 真 link/button 語意，44px 觸控、focus/loading/disabled、heading 連結；先轉一頁再漸進 | P1-02 |
| P1-05 文章版型 | post.html/default.html、components.css | 舊 HTML／Markdown 各至少兩篇、單 H1、表格橫捲、CTA/相關文章正常、URL/SEO 不變 | P1-04 |
| P1-06 動態與視覺回歸 | CSS/JS、測試配置、QA 報告 | reduced-motion、無 JS 可讀、320/375/768/1280、200% zoom、鍵盤與 axe/Lighthouse baseline | P1-03–05 |

FORM-03 優先安排獨立的表單安全 PR，驗證無 JS 時資料無法進 URL。FORM-01/02 的回應契約和 sandbox 寄送、ANALYTICS-01、ADS-01、PRIV-01 與 privacy layout 各列獨立審查範圍。`free.html` 不因抽共用元件而改動 Webhook；需要接觸訂閱互動時先核准 sandbox 與契約。

Phase 1 完成門檻：路由、canonical、sitemap/feed、原訂閱入口無意外改變；必要建置與內容驗證通過；沒有新增重大 a11y 問題；文件與截圖可審，K叔確認才接 Phase 2。

## 後續階段

- Phase 2：首頁資訊架構、`/start/`；taxonomy adapter；靜態搜尋 JSON（不含未公開內容）、分類／無結果／無 JS；保留現有 `/articles/`。
- Phase 3：先解決 `/resources/` 決策；collections/schema 驗證器、目錄／詳情模板；僅使用核准商品資訊與真實入口；沒有支付或會員功能。
- Phase 4：依 MIGRATION gate 建立隔離預覽、完整路由 HTTP 矩陣、排程與回復演練；再提正式切換，不與其他階段捆綁批准。
- Phase 5：另交技術／商業選型 PRD；會員／訂單／金流／影片／進度系統獨立審核後才實作。

## 授權清單

| 決策／操作 | 本次狀態 | 誰需確認 |
| --- | --- | --- |
| 進入 Phase 1、採用設計候選 | 未核准 | K叔 |
| 新增資源中心並改既有 resources 別名 | 未核准 | K叔（入口與 SEO） |
| 現有服務價格／時長／上架、數位商品與課程方案 | 原碼僅供盤點 | K叔（商業） |
| n8n sandbox、正式流程／信件／CORS／退訂變更 | 未執行 | 流程持有者 + K叔 |
| Analytics 容器權限／追蹤同意策略 | 待帳戶驗證 | 帳戶管理者 + K叔 |
| GitHub branch protection、Pages／Actions 設定 | 已確認 main 無保護、Pages 僅 main；任何改動待核准 | repo 管理者 |
| Cloudflare App 授權、預覽、付費方案、正式網域／DNS／排程 | 未執行 | 帳戶管理者 + K叔 |
| 學院／金流／訂單／退款／個資政策 | 未選型 | K叔及相關專業人員 |

只要求與各階段有關的決策；Phase 0 不要求提供正式金鑰或將 secrets 放聊天。審核提交狀態見 QA-CHECKLIST，文件完成不代表 PR 已獲核准。
