---
layout: default
title: 文章
description: K叔的文章頁，分享自媒體經營、斜槓生活與個人品牌心得
keywords: 自媒體, 文章, 經營心得, K叔
permalink: /articles/
---

<div class="card-section" style="background:#e8f6ff;">
<h1>文章列表</h1>
<div class="card-section">
  <ul>
{% assign sorted_posts = site.posts | sort: "date" | reverse %}
{% for post in sorted_posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span style="color: #888;">{{ post.date | date: "%Y-%m-%d" }}</span>
  </li>
{% endfor %}
</ul>
  </div>
<div class="card-section">
  <h2>自媒體起手式</h2>
  <p>先想清楚你要幫誰，然後設計內容策略，才能有效變現。</p>
</div>

<div class="card-section">
  <h2>內容產出系統化</h2>
  <p>靈感不是靠運氣，而是靠固定流程與規劃。</p>
</div>

<div class="card-section">
  <h2>Threads 經營誤區</h2>
  <p>避免寫了沒人看的文章，重點是設定目標受眾和解決問題。</p>
</div>
