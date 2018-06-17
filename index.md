---
layout: home
---

<div class="index-content blog">
    <div class="section">
        <ul class="artical-cate">
            <li class="on"><a href="/"><span>Blog</span></a></li>
            <!-- <li style="text-align:center"><a href="/Notes"><span>Notes</span></a></li> -->
<!--             <li style="text-align:right"><a href="/Stories"><span>Stories</span></a></li>
 -->        </ul>

        <div class="cate-bar"><span id="cateBar"></span></div>

        <ul class="artical-list">
        {% for post in site.categories.blog %}
            <li>
                <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
                <div class="title-desc">{{ post.description }}</div>
                <div class="entry-date">{{ page.date|date:"%Y-%m-%d" }}</div>
                <div id="content">
    <div class="entry">
        <h1 class="entry-title"><a href="{{ page.url }}" title="{{ page.title }}">{{ page.title }}</a></h1>
        <p class="entry-date">{{ page.date|date:"%Y-%m-%d" }}</p>
        {{ content }}
        <br>    
    </div>
            </li>
        {% endfor %}
        </ul>
    </div>
    <div class="aside">
    </div>

</div>
 