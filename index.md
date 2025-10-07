<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>RUNING_9to5｜逃離朝九晚五，打造可持續的自媒體收入系統</title>
  <meta name="description" content="K叔｜不想上班的貓，協助上班族與內向創作者建立穩定輸出與個人品牌。提供自媒體變現教學、電子書販賣與一對一諮詢服務。">
  <meta name="keywords" content="自媒體變現, 自媒體經營, 電子書教學, 個人品牌, 一對一諮詢, 上班族斜槓">

  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "首頁", "item": "https://runing9to5.com" },
      { "@type": "ListItem", "position": 2, "name": "文章", "item": "https://runing9to5.com/articles/" }
    ]
  }
  </script>

  <!-- Author Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "K叔｜不想上班的貓",
    "description": "自媒體變現教練，協助上班族與內向創作者打造可持續的自媒體收入系統。",
    "url": "https://runing9to5.com",
    "sameAs": [
      "https://www.threads.net/@runing_9to5",
      "https://www.instagram.com/runing_9to5/"
    ],
    "knowsAbout": ["自媒體經營", "內容變現", "電子書製作", "個人品牌打造"]
  }
  </script>
</head>

<body>
<!-- SEO 短版 Hero 區 -->
<section class="hero" style="background:#dceeff; padding:40px;text-align:center;">
  <h1>Runing9TO5｜陪上班族與內向創作者，打造可持續的自媒體變現系統</h1>
  <h2>不露臉、 從零開始也能靠自媒體變現</h2>
  <p>從零粉絲到自媒體收入<br>
    我親身實踐成功案例，找我諮詢的粉絲也都做到<br>
    電子報完整整理操作流程<br>
   <a href="#subscribe" class="btn-external" style="margin-bottom:30px;">👉 現在就訂閱免費電子報領取《從零到變現：50 個自媒體小 Tips》</a>
  <br>
  <small>已有 100+ 上班族加入，開始打造自己的副業系統</small>
  </p>
 
</section>
<!-- FAQ 區 -->
  <section class="faq">
    <h2>常見問題</h2>
    <div class="faq-item">
      <h3>Q1. 我沒有粉絲，也能開始經營自媒體嗎？</h3>
      <p>可以。我的方法重點在「內容策略 × 產品設計」，幫助你用價值吸引受眾，而不是靠流量硬撐。</p>
    </div>
    <div class="faq-item">
      <h3>Q2. 電子書真的能變現嗎？</h3>
      <p>能。只要用正確的定位與價值前置方式，電子書是建立信任與收入的最佳入門產品。</p>
    </div>
    <div class="faq-item">
      <h3>Q3. 一對一諮詢能幫我什麼？</h3>
      <p>我會協助你釐清定位、產品策略、內容規劃，並給出具體行動建議，讓你不再只是「想開始」。</p>
    </div>
  </section>
<!-- SEO 長文區 -->
<section class="card-section animate-section" style="background:#f7f7f7;">
  <h2 class="slide-in">自媒體 × 斜槓 × 個人品牌｜從上班族到自由工作者</h2>
  <p class="slide-in">
    這個網站是 K叔的數位筆記本，專門整理 <b>自媒體經營、內容變現、斜槓副業</b> 的方法。<br><br>
    如果你是一位想要突破日常、卻又擔心沒有方向的上班族，這裡有最實用的筆記，陪你從「想開始」到「能做到」。<br>
    📌 你可以在這裡找到：  
  </p>
  <ul class="slide-in">
    <li>自媒體定位與經營策略</li>
    <li>內容創作與寫作輸出的方法</li>
    <li>斜槓副業的低成本啟動模式</li>
    <li>個人品牌養成與長期經營心法</li>
  </ul>
  <p class="slide-in">
    我相信，<b>自由不是辭職才開始，而是從現在就能累積的選擇權</b>。<br>
    👉  <a href="https://runing9to5.com/articles/">更多文章</a>
  </p>
</section>


<!-- 最新文章區 -->
<section class="card-section" style="background:#f7f7f7;">
  <h2>📚 最新文章</h2>

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
<section class="card-section animate-section" style="background:#FAFAFA;">
  <h2 class="slide-in">用戶回饋</h2>
  <p class="slide-in">讀者與學員的真實心得：</p>

  <div class="testimonial slide-in">
    <blockquote>「特別適合內向創作者 & 邊上班邊想經營內容的人讓你慢慢培養產出節奏、寫得順、跑得穩
打造出專屬自己的個人品牌~💪」
      <p>小花生，自媒體小編</p>
    </blockquote>
  </div>

  <div class="testimonial slide-in">
    <blockquote>「K叔電子報超讚！，讓我開始懂得怎麼規劃內容，感覺不再那麼迷茫。」
      <p>月行，Threads創作者</p>
    </blockquote>
  </div>

  <div class="testimonial slide-in">
    <blockquote>「這個人沒有太多花俏的行銷總讓我感覺像是在跟隔壁同事聊天一樣可以一起厭世、一起碎唸生活。」
      <p> TING J.， 叛逆工程師，自媒體新手</p>
    </blockquote>
  </div>
</section>

<!-- 電子報 -->
<section class="card-section" style="background:#dceeff;" id="subscribe">
  <h2>訂閱電子報</h2>
  <p>📬 輸入你的 Email，加入我們！領取《從零到變現：50 個自媒體小 Tips》</p>
  <div class="newsletter-box">
    <script async data-uid="49e70b7c7c" src="https://ken-66.kit.com/49e70b7c7c/index.js"></script>
  </div>
</section>

 <!-- 關於我區 -->
  <section class="about">
    <h2>👋 關於 K叔｜不想上班的貓</h2>
    <p>我是 RUNING_9to5 的創辦人，一位幫助上班族與創作者「逃離朝九晚五」的自媒體教練。我的服務包含：</p>
    <ul>
      <li>💡 <strong>自媒體變現教學</strong>：用內容打造收入系統。</li>
      <li>📘 <strong>電子書販賣策略</strong>：把經驗轉成被動收益。</li>
      <li>🧑‍💻 <strong>一對一諮詢</strong>：針對個人品牌的具體行動方案。</li>
    </ul>
    <p>我的文字不是想紅，而是想讓你找到屬於自己的出口。</p>
  </section>

<section class="card-section" style="background:#FAFAFA;">
  <h2>聯絡我 / 社群</h2>
  <p>Email：<a href="mailto:uncleKen@runing9to5.com">uncleKen@runing9to5.com</a></p>
  <p>
    <a href="https://www.threads.net/@runing_9to5" target="_blank">Threads</a> | 
    <a href="https://www.instagram.com/runing_9to5/" target="_blank">Instagram</a>
  </p>
</section>
 <footer>
    <p>© 2025 RUNING_9to5 ｜ 不想上班的貓 K叔</p>
  </footer>

<!-- JS 放在這裡 -->
<script>
document.addEventListener("DOMContentLoaded", function() {
  const sections = document.querySelectorAll(".animate-section");

  sections.forEach(section => {
    const cards = section.querySelectorAll(".slide-in");
    cards.forEach((card, i) => {
      card.classList.add(i % 2 === 0 ? "left" : "right");
    });
  });

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const cards = entry.target.querySelectorAll(".slide-in");
        cards.forEach((card, index) => {
          setTimeout(() => card.classList.add("show"), index * 180);
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  sections.forEach(section => observer.observe(section));
});
</script>
