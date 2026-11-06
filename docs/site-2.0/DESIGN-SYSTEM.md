---
published: false
---
# 設計系統｜Phase 1 規格草案

以既有溫暖米白、深藍、暖棕為起點；暖金為候選，尚未實作／核准。

| 語意 token（提案） | 值 | 用途 |
| --- | --- | --- |
| color.background | `#F5F0EA` | 奶油白底，沿用 --bg |
| color.surface | `#FAF8F5` | 卡片，沿用 --bg-card |
| color.surface-alt | `#EDE8E0` | 分區 |
| color.text | `#1A2540` | 主文字 |
| color.text-secondary | `#3D4F6E` | 次文字 |
| color.primary | `#2D4A7A` | 深海藍、主按鈕 |
| color.primary-hover | `#1E3560` | hover／active |
| color.accent | `#9E7048` | 既有暖棕，保留相容 token |
| color.gold | `#D6AC54` | 待核准暖金，限裝飾或配深色文字 |
| color.focus | `#1E3560` | 3px outline + 3px offset |

`#8896AA` 現有 muted 色不可直接視為合格內文色；Phase 1 需量測實際背景對比並調深。金色不可配白字作普通文字按鈕。一般字 4.5:1、大字與必要 UI 邊界 3:1，以 WCAG 2.2 AA 為驗收目標。

## 字體、尺寸與版面

保留 Noto Sans TC／Noto Serif TC 品牌方向，提供 system-ui／serif fallback；Phase 1 不新增字體服務。避免 CSS @import 阻塞，是否自託管另評估字型授權與容量。內文至少 16px、行高 1.75–1.9；長文容器約 42–50rem；間距採 4/8/12/16/24/32/48/64px，圓角 6/10px。移動版從 320px 開始，480/768/1024px 為驗證點，不依特定手機品牌。

## 元件契約

- Header：保留 logo 與現有目的地；nav 有 aria-label、目前頁 aria-current；button 控制收合選單。支援 Enter/Space、Escape 關閉並回焦點，resize 後狀態一致，無 JS 可見主要連結。
- Footer：年度自動更新，保留隱私與訂閱入口，避免被包在文章 main 內；不新增未核准服務連結。
- Button：連結用 a、操作用 button；primary/secondary/text 三種變體及 hover/focus/disabled/loading；觸控目標至少 44×44 CSS px，不只靠顏色傳達狀態。
- Card：有標題連結、描述、可選分類；整卡可點也要有鍵盤等價方式，不嵌套互動元素；圖片有 alt、尺寸、非首屏才 lazy。
- Article：單一有意義 H1、連續 heading、清楚連結、清單／引用／程式碼／表格橫捲。既有 HTML 卡片正文與純 Markdown 都要回歸，不能機械添加第二個 H1。
- Form（此階段只定規格）：可見 label、type=email、autocomplete、錯誤與成功 live region、保留輸入、提交防重與焦點管理。修正 Webhook 流程需另 PR，不混進視覺改版。
- FAQ／動畫：aria-expanded/controls 與面板 hidden 一致；prefers-reduced-motion 下移除平滑捲動與 reveal 位移，無 JS 仍可讀內容。

## Phase 1 驗收矩陣

首頁、文章列表、舊 HTML 長文、新 Markdown 長文、關於、諮詢、隱私、免費頁皆納入回歸；免費頁先截圖／盤點重複 tokens，不擅自改表單契約。320/375/768/1280px，200% zoom，鍵盤 Tab／Shift+Tab／Escape，文字放大與 reduced-motion。檢查固定導覽不遮標題，表格僅自身橫捲，無整頁溢出，focus 不被遮擋。

效能為待驗收預算：主要頁 Lighthouse mobile performance/accessibility 目標 90+；field CWV 目標 LCP≤2.5s、INP≤200ms、CLS≤0.1（第 75 百分位，需真實資料）。目前沒有跑瀏覽器稽核，這些不是現況分數或成效承諾。先取得 baseline，再對每 PR 比較。
