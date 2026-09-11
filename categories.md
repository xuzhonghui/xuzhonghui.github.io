---
layout: default
title: 文章分类
---

# 文章分类

{% for category in site.categories %}
## {{ category[0] }}

<ul>
{% for post in category[1] %}
    <li>
    <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    <small>{{ post.date | date: "%Y-%m-%d" }}</small>
    </li>
{% endfor %}
</ul>
{% endfor %}