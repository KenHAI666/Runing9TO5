---
layout: default
title: 文章列表｜K叔自媒體經營筆記
description: 這裡整理了 K叔關於自媒體經營、內容變現、斜槓生活與個人品牌的實戰心得。
keywords: 自媒體, 文章, 經營心得, K叔, 內容變現
permalink: /articles/
---

<div style="height:70px;"></div>

<section class="card-section">
  
  <h1 style="text-align: center; color: #3B5B7A; margin-bottom: 30px;">📚 K叔的數位筆記本</h1>

  <div class="card-section-1" style="border-left: 5px solid #C48E64; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; cursor: pointer;" onclick="window.location.href='/resources';">
    <div>
      <h2 style="margin: 0 0 10px 0; color: #C48E64; font-size: 1.5em;">🔥 從零到變現：系統化經營指南</h2>
      <p style="margin: 0; color: #555;">別只是寫身體健康的。這套電子書教你如何設計內容策略，把流量變成收入。</p>
    </div>
    <a href="/resources" class="btn-external" style="background-color: #C48E64; border-color: #C48E64; margin-top:0;">查看詳情 →</a>
  </div>


  <div id="category-menu" style="margin: 30px 0; text-align: center;">
    <strong style="margin-right:10px; color: #3B5B7A;">篩選主題：</strong>
    <button onclick="filterCategory('all', this)" class="category-btn active">全部文章</button>
    {% assign categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq %}
    {% for category in categories %}
      {% if category != "" %}
      <button onclick="filterCategory('{{ category | strip }}', this)" class="category-btn">
        {% assign category_name = category | strip %}
        {% case category_name %}
          {% when "content-strategy" %}自媒體策略
          {% when "personal-growth" %}個人成長
          {% when "side-hustle" %}副業斜槓
          {% else %}{{ category_name }}
        {% endcase %}
      </button>
      {% endif %}
    {% endfor %}
  </div>


  <div id="articles-list">
    {% assign regular_posts = site.posts | reject: "pinned", true | sort: "date" | reverse %}
    {% for post in regular_posts %}
    
    <div class="card-section-1 article-card" 
         data-category="{{ post.categories | join: ',' }}"
         onclick="window.location.href='{{ post.url | relative_url }}';"
         style="cursor: pointer; margin-bottom: 20px; transition: all 0.3s;">
         
      <h2 style="margin-top:0; font-size: 1.4em;">
        <a href="{{ post.url | relative_url }}" style="text-decoration:none; color:#3B5B7A;">
          {{ post.title }}
        </a>
      </h2>
      
      <p style="color:#555; line-height:1.6; margin: 15px 0;">
        {{ post.content | strip_html | truncate: 80 }}
      </p>
      
      <div style="border-top: 1px dashed #ddd; padding-top: 10px; margin-top: 15px; display: flex; justify-content: space-between; align-items: center; color:#888; font-size: 0.9em;">
        <span>🏷️
          {% for category in post.categories %}
            {% case category %}
              {% when "content-strategy" %}自媒體策略
              {% when "personal-growth" %}個人成長
              {% when "side-hustle" %}副業斜槓
              {% else %}{{ category }}
            {% endcase %}{% unless forloop.last %}, {% endunless %}
          {% endfor %}
        </span>
        <span>📅 {{ post.date | date: "%Y-%m-%d" }}</span>
      </div>
      
    </div>
    {% endfor %}
  </div>

</section>


<style>
/* 分類按鈕樣式 */
.category-btn {
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 20px;
  padding: 8px 16px;
  margin: 4px;
  cursor: pointer;
  font-size: 14px;
  color: #555;
  transition: all 0.2s;
  font-family: "Noto Sans TC", sans-serif;
}

.category-btn:hover {
  background: #e8f6ff;
  color: #3B5B7A;
  border-color: #3B5B7A;
}

/* 選中狀態 (使用品牌藍) */
.category-btn.active {
  background: #3B5B7A;
  color: white;
  border-color: #3B5B7A;
  box-shadow: 0 2px 5px rgba(59, 91, 122, 0.3);
}

/* 文章卡片懸停效果 (沿用全站樣式，這裡做微調) */
.article-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}

.article-card:hover h2 a {
    color: #C48E64 !important; /* 標題變色 */
}
</style>

<script>
function filterCategory(category, btn) {
  const cards = document.querySelectorAll("#articles-list .article-card");

  // 切換 active 狀態
  document.querySelectorAll("#category-menu .category-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");

  // 顯示/隱藏文章
  cards.forEach(card => {
    // 兼容處理：有些分類可能有空格，做一下清理
    const cats = card.dataset.category.split(",").map(c => c.trim());
    
    if (category === "all" || cats.includes(category)) {
      card.style.display = "block";
      // 添加一個小動畫讓出現更自然
      card.style.opacity = 0;
      setTimeout(() => card.style.opacity = 1, 50);
    } else {
      card.style.display = "none";
    }
  });
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "headline": "{{ page.title }}",
  "description": "{{ page.description }}",
  "url": "{{ page.url | absolute_url }}",
  "publisher": {
    "@type": "Organization",
    "name": "RUNING_9to5",
    "logo": {
      "@type": "ImageObject",
      "url": "https://runing9to5.com/assets/images/logo.png"
    }
  }
}
</script>
