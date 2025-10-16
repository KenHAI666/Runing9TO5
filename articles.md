---
layout: default
title: 文章
description: K叔的文章頁，分享自媒體經營、斜槓生活與個人品牌心得
keywords: 自媒體, 文章, 經營心得, K叔
permalink: /articles/
---

<!-- 導覽列間距 -->
<div style="height:70px;"></div>

<div class="card-section" style="background:#e8f6ff; padding:20px; border-radius:10px;">
  <h1>📚 文章列表</h1>

  <!-- 🔹 固定內容卡片 -->
<div class="card-section" style="margin-top:30px;">
  <div class="card" style="background:#fff6e8; padding:20px; border-radius:10px; margin-bottom:20px;">
    <h2>自媒體起手式</h2>
    <p>先想清楚你要幫誰，然後設計內容策略，才能有效變現。</p>
  </div>
</div>

  <!-- 🔹 分類篩選 -->
  <div id="category-menu" style="margin:20px 0;">
    <strong style="margin-right:10px;">篩選分類：</strong>
    <button onclick="filterCategory('all', this)" class="category-btn active">全部</button>
    {% assign categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq %}
    {% for category in categories %}
      {% if category != "" %}
      <button onclick="filterCategory('{{ category | strip }}', this)" class="category-btn">
        {{ category | strip }}
      </button>
      {% endif %}
    {% endfor %}
  </div>


  <!-- 🔹 一般文章 -->
  <div id="articles-list">
    {% assign regular_posts = site.posts | reject: "pinned", true | sort: "date" | reverse %}
    {% for post in regular_posts %}
    <div class="card" 
         data-category="{{ post.categories | join: ',' }}"
         style="border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px; background:#fff; box-shadow:0 2px 5px rgba(0,0,0,0.05); transition: all 0.3s;">
      <h2 style="margin-top:0;">
        <a href="{{ post.url | relative_url }}" style="text-decoration:none; color:#333;">
          {{ post.title }}
        </a>
      </h2>
      <p style="color:#555; line-height:1.6;">
        {{ post.content | strip_html | truncate: 100 }}
      </p>
      <small style="color:#999; font-size:0.9em;">
        🏷️ {{ post.categories | join: ", " }} ｜ 📅 {{ post.date | date: "%Y-%m-%d" }}
      </small>
    </div>
    {% endfor %}
  </div>
</div>


<!-- 🔹 CSS 美化 -->
<style>
.category-btn {
  background: #f5f5f5;
  border: none;
  border-radius: 20px;
  padding: 6px 14px;
  margin: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}
.category-btn:hover {
  background: #ffeed9;
  color: #e67e22;
}
.category-btn.active {
  background: #e67e22;
  color: white;
}
.card:hover {
  transform: translateY(-3px);
  box-shadow:0 4px 10px rgba(0,0,0,0.1);
}
.pinned-card {
  border-width: 2px;
  background: #fffbea;
}
</style>

<!-- 🔹 JS 篩選功能 -->
<script>
function filterCategory(category, btn) {
  const cards = document.querySelectorAll("#pinned-articles .card, #articles-list .card");

  // 切換 active 狀態
  document.querySelectorAll("#category-menu .category-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");

  // 顯示/隱藏文章
  cards.forEach(card => {
    const cats = card.dataset.category.split(",");
    if (category === "all" || cats.includes(category)) {
      card.style.display = "block";
    } else {
      card.style.display = "none";
    }
  });
}
</script>

<!-- 🔹 JSON-LD 結構化資料 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{{ page.title }}",
  "author": {
    "@type": "Person",
    "name": "K叔｜不想上班的貓"
  },
  "publisher": {
    "@type": "Organization",
    "name": "RUNING_9to5"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{ page.url | relative_url }}"
  },
  "datePublished": "{{ page.date | date: "%Y-%m-%d" }}"
}
</script>
