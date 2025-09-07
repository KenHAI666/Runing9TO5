---
layout: default
title: 文章
description: K叔的文章頁，分享自媒體經營、斜槓生活與個人品牌心得
keywords: 自媒體, 文章, 經營心得, K叔
permalink: /articles/
---

<div class="card-section" style="background:#e8f6ff; padding:20px; border-radius:10px;">
  <h1>📚 文章列表</h1>

  <!-- 🔹 分類篩選 -->
  <div id="category-menu" style="margin:20px 0;">
    <strong style="margin-right:10px;">篩選分類：</strong>
    <button onclick="filterCategory('all')" class="category-btn active">全部</button>
    {% assign categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq %}
    {% for category in categories %}
      {% if category != "" %}
      <button onclick="filterCategory('{{ category | strip }}')" class="category-btn">
        {{ category | strip }}
      </button>
      {% endif %}
    {% endfor %}
  </div>

  <!-- 🔹 動態文章卡片 -->
  <div id="articles-list">
    {% assign sorted_posts = site.posts | sort: "date" | reverse %}
    {% for post in sorted_posts %}
    <div class="card" 
         data-category="{{ post.categories | join: ' ' }}"
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

<!-- 🔹 固定內容卡片 -->
<div class="card-section" style="margin-top:30px;">
  <div class="card" style="background:#fff6e8; padding:20px; border-radius:10px; margin-bottom:20px;">
    <h2>自媒體起手式</h2>
    <p>先想清楚你要幫誰，然後設計內容策略，才能有效變現。</p>
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
</style>

<!-- 🔹 JS 篩選功能 -->
<script>
function filterCategory(category) {
  const cards = document.querySelectorAll("#articles-list .card");
  const buttons = document.querySelectorAll(".category-btn");

  buttons.forEach(btn => btn.classList.remove("active"));
  const activeBtn = Array.from(buttons).find(btn => 
    btn.textContent.trim() === category || (category === "all" && btn.textContent.trim() === "全部")
  );
  if (activeBtn) activeBtn.classList.add("active");

  cards.forEach(card => {
    if (category === 'all' || card.dataset.category.includes(category)) {
      card.style.display = 'block';
    } else
