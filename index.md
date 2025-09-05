---
layout: default
title: K叔｜不想上班的貓
---

# 歡迎來到 K叔的個人網站 🐱

> 系統化經營自媒體｜用最懶人的方式，把自媒體經營變成可持續的斜槓收入

---

## 關於我

<img src="{{ '/assets/images/me.jpeg' | relative_url }}" 
     alt="我的大頭照" 
     class="about-img" 
     onerror="this.onerror=null;this.src='data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22150%22 height=%22150%22><rect width=%22100%25%22 height=%22100%25%22 fill=%22%23ececec%22/><text x=%2250%25%22 y=%2255%25%22 font-size=%2236%22 text-anchor=%22middle%22 fill=%22%23666%22>K叔</text></svg>';"> 

大家好，我是 K叔，一個不想上班的貓，但喜歡用內容創作打造斜槓收入。  
這裡分享我的自媒體經營、個人品牌建立心得，以及懶人斜槓技巧。

---

## 最新文章

{% for post in site.posts limit:5 %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}

---

## 訂閱電子報

<div class="newsletter-box">
  <h3>不想錯過 K叔的斜槓秘訣？</h3>
  <form action="https://你的convertkit表單網址" method="post" class="newsletter-form">
    <input type="email" name="email_address" placeholder="輸入你的 Email" required>
    <button type="submit">訂閱</button>
  </form>
</div>

---

## 聯絡我

- Threads: [@your_account](https://www.threads.net/@your_account)  
- Email: 透過網站聯絡表單  

---

Made with ❤️ by K叔
