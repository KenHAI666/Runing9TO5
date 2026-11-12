---
published: false
---
# 公開內容資料模型｜提案 v1

保留 `_posts` 及每篇現有 permalink；新集合使用 front matter，不放會員或交易資料。所有範例為示意，非已上架商品或已確認商業方案。

## 共用欄位與驗證

| 欄位 | 型別／規則 | 必填 |
| --- | --- | --- |
| schema_version | integer，初版 1 | 新內容是 |
| id | string，跨集合唯一、穩定英文 kebab-case | 是 |
| title / description | 非空純文字；輸出 escape，JSON 用 jsonify | 是 |
| slug | 唯一 kebab-case，不允許 slash、`..`、保留字 | 是 |
| permalink | 站內絕對路徑；跨文章／頁面／別名唯一 | 是 |
| status | draft / coming_soon / active / retired | 是 |
| published | boolean；draft 必須 false，其他依上架核准 | 是 |
| audience / outcomes | string[]；不允許無法證明的成效保證 | 是 |
| image / image_alt | 站內存在檔案、非裝飾圖必有 alt | 可選 |
| categories / tags | 已定義 taxonomy ID[]；中文 label 另存 | 可選 |
| related_ids | 既存公開內容 ID[]，排除自身與 draft | 可選 |
| updated_at | ISO 8601 日期／時間，含時區或統一台北規則 | 是 |
| cta | label + kind + url；coming_soon 可 null | 可選 |
| seo | 可選 title/description/image 覆寫，不接受任意 JS | 可選 |

CTA kind 僅 internal/external/inquiry。internal 必須命中公開路由；external/inquiry 只接受經審核的 https URL，不允許 javascript/data/credential userinfo。外連新分頁有 noopener noreferrer。預覽禁止觸發正式訂閱／交易。

Jekyll 不會自動執行上述 schema；Phase 3 必須實作驗證器與負向測試後才能宣稱資料受控。`status` 不會自動隱藏頁面，必須與 `published`、集合輸出及索引／sitemap 規則一起驗證。

## 分類與文章

初期保留 content-strategy／personal-growth／side-hustle 以及其他既有分類，不大量改名導致內連或篩選失效。`_data/taxonomy.yml` 擬保存 id、label、description、sort_order。現有文章 title/date/last_modified_at/lang/description/categories/tags/permalink/image/author/pinned/source_date/source_type/source_url 均保留；source_url 不必公開顯示。不要以檔名重新生成舊 URL。

## 資源 Resource

額外欄位：format（pdf/template/checklist/link）、delivery（subscription/external_download）、asset_url（可空）、subscription_flow_id（公開流程識別，不是 webhook secret）。訂閱型交付沿用 `/free`；`asset_url` 只用於已核准公開下載的資產。登記、同意、寄送狀態與開信紀錄留在受控流程。`/resources/` 衝突先解決。

## 工具 Tool

額外欄位：tool_kind（static/external）、tool_url、requires_account（boolean）、data_handling_summary、availability（planned/available/unavailable）。不預設工具已可用；外部工具需核實連結、資料去向、手機支援與服務條款。

## 商品／服務 Offering

數位商品先使用共用 offering 模型與 kind=digital_product；是否新增 `/products/` 集合或放入 resources 目錄，交由 K叔確認，不擅自擴大 IA。

服務額外欄位：kind（consulting/service/digital_product）、delivery_mode、duration_minutes（可空）、scope_in/scope_out、inquiry_url、price（可空）。

```yaml
schema_version: 1
id: example-consulting
slug: example-consulting
permalink: /services/example-consulting/
title: 待核准服務示例
description: 僅供結構討論，不代表可購買。
status: draft
published: false
audience: [已有商品或服務的個人品牌]
outcomes: [釐清下一步方向]
updated_at: '2026-11-06'
kind: consulting
price: null
cta: null
```

price 若核准：`amount_minor` 為非負整數（最小貨幣單位）、`currency` 為 ISO 4217、`tax_display`／`billing_basis`／`verified_at` 明定。null 顯示「洽詢／待公布」只在文案核准後使用，不能自動輸出 NT$0。正式頁目前列有 NT$1,000／60 分鐘。新頁上架前由 K叔確認實際價格、交付範圍與預約入口。金流 URL 僅經商家確認後加入，不保存 merchant secret 或訂單 ID。

## 課程 Course

額外欄位：level、prerequisites[]、syllabus[]（module title / public summary）、delivery_mode、duration_label（可空）、instructor_ids[]、enrollment_status（not_open/waitlist/open/closed）、academy_url（可空）、price（可空）。

規則：open 需另案核准的報名入口；無證據不填額定名額、學生數、評分或證書。Course／Offer JSON-LD 只對真實且公開可見資訊輸出。章節影片、簽章播放 URL、學員名單、學習進度、帳號和付款狀態不進 repository、前端索引或 analytics。

## 驗證器規格

正向：有效資料可 render、內連存在、金額／幣別成對。負向：重複 ID／permalink／redirect alias、無效 enum、缺必填、draft 被索引、空價格轉 0、外部非 https、asset 不存在、related_ids 無效、洩漏敏感欄位均須 CI 失敗。先支援舊文章欄位再逐批補資料，不讓 schema 升級阻斷原內容建置。
