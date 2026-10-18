---
layout: default
title: 文章列表｜K叔自媒體經營筆記
description: 這裡整理了 K叔關於自媒體經營、Threads 經營、內容變現與個人品牌的實戰心得。
keywords: 自媒體, 文章, 經營心得, K叔, 內容變現
permalink: /articles/
---

<div class="nav-spacer"></div>

<section class="card-section">
  
  <h1 style="text-align: center; color: #3B5B7A; margin-bottom: 30px;">📚 K叔的數位筆記本</h1>

  {% assign pinned_posts = site.posts | where: "pinned", true | sort: "date" | reverse %}
  {% for post in pinned_posts %}
  <article class="card-section-1" style="border-left: 5px solid #C48E64; margin-bottom: 20px;">
    <p style="margin: 0 0 10px; color: #C48E64; font-weight: 600;">置頂文章</p>
    <h2 style="margin: 0 0 15px; font-size: 1.4em;">
      <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #3B5B7A;">{{ post.title }}</a>
    </h2>
    <p style="color: #555; line-height: 1.6;">{{ post.description | escape }}</p>
    <a href="{{ post.url | relative_url }}" class="btn-external">閱讀文章</a>
  </article>
  {% endfor %}

  <div class="card-section-1" style="border-left: 5px solid #C48E64; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; cursor: pointer;" onclick="window.location.href='/free';">
    <div>
      <h2 style="margin: 0 0 10px 0; color: #C48E64; font-size: 1.5em;">📄 免費領取《自媒體變現三大核心心法》</h2>
      <p style="margin: 0; color: #555;">先自己看看卡在哪。<br>免費 PDF＋歡迎信＋8 天內容診斷信，每天看一個問題就好。</p>
    </div>
    <a href="/free" class="btn-external" style="background-color: #C48E64; border-color: #C48E64; margin-top:0;">免費領取 →</a>
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
    {% assign regular_posts = site.posts | sort: "date" | reverse %}
    {% for post in regular_posts %}
    {% unless post.pinned %}
    
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
    {% endunless %}
    {% endfor %}
  </div>

  <script>
    function filterCategory(category, btn) {
      const cards = document.querySelectorAll('.article-card');
      const buttons = document.querySelectorAll('.category-btn');
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      cards.forEach(card => {
        const cats = card.dataset.category.split(',');
        if (category === 'all' || cats.includes(category)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>

</section>
