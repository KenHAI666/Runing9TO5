# 2027 文案課預售名單網站｜部署與收件設定

## 網址與狀態
- 本檔位於 `writing-2027/index.html`，GitHub Pages 合併部署後預定為 `https://runing9to5.com/writing-2027/`。
- **目前只有前端網站已完成；名單接收端尚未設定，不能把這個網址當成已啟用的登記頁公開。**
- 前端在接收端未設定時會明確顯示「沒有儲存資料」，不會顯示假的提交成功。
- 這是「預售優先通知／興趣登記」，並非開放購買、收取訂金或承諾開課時程。

## 必做：為課程另建名單接收端
現有官網 `free.html` 使用 `https://kenhai-n8n.hf.space/webhook/subscribe`，那是舊免費資源收件流程，**不可直接用在這個預售頁**。

建議建立 n8n 新 workflow：
1. Webhook Trigger：POST，專用 path 例如 `writing-2027-prelaunch`。
2. 校驗 `email`、`consent===true`、`interested_in==='2027_copywriting_course'`，限制輸入長度／頻率，去重；公開來源只允許 `https://runing9to5.com`（含 CORS 預檢）。
3. 用 n8n 伺服器端的 Kit 憑證建立或更新訂閱者，套專用標籤 `writing2027-prelaunch-interest`。既有電子報讀者只新增課程意願標籤，不進舊免費資源序列。
4. 只有在 Kit 接受新訂閱／標籤寫入成功後，Respond to Webhook 才回 HTTP 200 JSON `{"success":true}`；否則回錯誤或 `{"success":false}`。如果需要雙重訂閱確認，要另外確認 Kit 實際訂閱狀態。
5. 將公開 Webhook URL 填入本頁底部 `const PRELAUNCH_WEBHOOK_URL='';`。不可把 Kit API 密鑰或 n8n API 密鑰放進網頁。
6. 確認個資使用目的已寫進 `/privacy/`，並安排退訂與刪除資料的處理方式。

## 資料格式
表單會 POST JSON：
```json
{
  "email": "reader@example.com",
  "name": "暱稱",
  "writing_blocker": "topic",
  "lead_source": "writing_2027_presale_page",
  "interested_in": "2027_copywriting_course",
  "consent": true,
  "consent_text_version": "2026-11-21-v1",
  "submitted_at": "2026-11-21T09:00:00Z",
  "landing_page": "https://runing9to5.com/writing-2027/",
  "utm": {
    "utm_source": "newsletter",
    "utm_medium": "email",
    "utm_campaign": "2027_writing_presale"
  }
}
```
`writing_blocker` 選項：`topic`、`structure`、`ai_voice`、`improve` 或空字串。

## 上線前驗收
- [ ] 完成專屬 n8n workflow 和 Kit 標籤／確認信
- [ ] 在前端設定正式 Webhook URL，CORS 正常
- [ ] 測試新 Email 寄入後可在 Kit 找到帶有預售標籤的聯絡人
- [ ] 測試既有訂閱者加入標籤後不會被重複送舊序列信
- [ ] 測試重複提交／無效 Email／取消勾選／後端回應錯誤
- [ ] 由完成 Kit 確認的人數計算有效名單；GA4 的 `presale_lead_submit` 只在後端明確確認成功後觸發
- [ ] 確認隱私政策與 Email 退訂流程
- [ ] 確認 GitHub Pages 實際網址可開啟、手機畫面正常
- [ ] 核對後再將 `robots` 從 `noindex,nofollow` 改成 `index,follow`（如需搜尋收錄）

## 電子報正式連結（僅部署且測試通過後使用）
`https://runing9to5.com/writing-2027/?utm_source=newsletter&utm_medium=email&utm_campaign=2027_writing_presale`

這個專案只建立「預售有興趣的名單」，不代替 Claude 要編寫的課程、四堂正課收費、免費 7 天 10 篇自動寄送。