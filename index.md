---
layout: default
title: K叔｜自媒體經營 × 斜槓生活 × 個人品牌
description: K叔的個人網站，分享自媒體經營技巧、斜槓副業方法與個人品牌建立，陪你從上班族到自由工作者。
keywords: 自媒體, 斜槓, 個人品牌, 內容變現, 上班族副業, K叔
---
<!-- SEO 短版 Hero 區 -->
<section class="hero" style="background:#dceeff; padding:40px;text-align:center;">
  <h1>不露臉、 從零開始也能靠自媒體變現</h1>
  <p>從零粉絲到自媒體收入<br>
    我親身實踐成功案例，找我諮詢的粉絲也都做到<br>
    電子報完整整理操作流程<br>
   <a href="#subscribe" class="btn-external" style="margin-bottom:30px;">👉 現在就訂閱免費電子報</a>
  <br>
  <small>已有 100+ 上班族加入，開始打造自己的副業系統</small>
  </p>
 
</section>

<!-- SEO 長文區 -->
<section class="card-section" style="background:#f7f7f7;">
  <h2>自媒體 × 斜槓 × 個人品牌｜從上班族到自由工作者</h2>
  <p>
  這個網站是 K叔的數位筆記本，專門整理 <b>自媒體經營、內容變現、斜槓副業</b> 的方法。<br><br>
  如果你是一位想要突破日常、卻又擔心沒有方向的上班族，這裡有最實用的筆記，陪你從「想開始」到「能做到」。<br>
  📌 你可以在這裡找到：  
  </p>
  <ul>
    <li>自媒體定位與經營策略</li>
    <li>內容創作與寫作輸出的方法</li>
    <li>斜槓副業的低成本啟動模式</li>
    <li>個人品牌養成與長期經營心法</li>
  </ul>
  <p>
  我相信，<b>自由不是辭職才開始，而是從現在就能累積的選擇權</b>。<br>
  👉 更多文章請見 <a href="https://runing9to5.com/articles/">文章</a>
  </p>
</section>     

<!-- 最新文章區 -->
<section class="card-section" style="background:#f7f7f7;">
  <h2>📌 最新文章</h2>

  {% for post in site.posts limit:3 %}
    <div class="card-section-1">
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p class="post-date">{{ post.date | date: "%Y-%m-%d" }}</p>
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncate:100 }}</p>
      <a href="{{ post.url }}" class="read-more">閱讀更多 →</a>
    </div>
  {% endfor %}

</section>



<!-- 用戶回饋區 -->
<section class="card-section" style="background:#FAFAFA;">
  <h2>用戶回饋</h2>
  <p>讀者與學員的真實心得：</p>

  <div class="testimonial">
    <blockquote>「特別適合內向創作者 & 邊上班邊想經營內容的人讓你慢慢培養產出節奏、寫得順、跑得穩
打造出專屬自己的個人品牌~💪」
    <p>小花生，自媒體小編</p>
</blockquote>
  </div>

  <div class="testimonial">
    <blockquote>「K叔電子報超讚！，讓我開始懂得怎麼規劃內容，感覺不再那麼迷茫。」
    <p>月行，Threads創作者</p>
      </blockquote>
  </div>

  <div class="testimonial">
    <blockquote>「這個人沒有太多花俏的行銷總讓我感覺像是在跟隔壁同事聊天一樣可以一起厭世、一起碎唸生活。」
    <p> TING J.， 叛逆工程師，自媒體新手</p>
      </blockquote>
  </div>
</section>

<section class="card-section" style="background:#dceeff;" id="subscribe">>
  <h2>訂閱電子報</h2>
  <p>📬 輸入你的 Email，加入我們！</p>
  <div class="newsletter-box">
    <script async data-uid="49e70b7c7c" src="https://ken-66.kit.com/49e70b7c7c/index.js"></script>
  </div>
</section>

<section class="card-section" style="background:#FAFAFA;">
  <h2>關於我</h2>
  <img src="/assets/images/me.jpeg" alt="我的大頭照" class="about-img">
  <p>嗨，我是 K叔，一隻不想上班的貓。<br>
     這裡記錄我如何經營自媒體、打造產品，並分享自由工作者的故事。</p>
</section>

<section class="card-section" style="background:#FAFAFA;">
  <h2>聯絡我 / 社群</h2>
  <p>Email：<a href="mailto:uncleKen@runing9to5.com">uncleKen@runing9to5.com</a></p>
  <p>
    <a href="https://www.threads.net/@runing_9to5" target="_blank">Threads</a> | 
    <a href="https://www.instagram.com/runing_9to5/" target="_blank">Instagram</a>
  </p>
</section>
