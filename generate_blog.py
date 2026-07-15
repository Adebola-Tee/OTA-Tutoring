#!/usr/bin/env python3
"""Build OTA Tutoring's blog from simple Markdown content files."""

from __future__ import annotations

import html
import json
import math
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content" / "blog"
OUTPUT_DIR = ROOT / "blog"
SITE_URL = "https://www.otatutoring.com"
BOOKING_URL = "https://cal.com/taiwo-oloyede-wmeart/free-parent-consultation"
EMAIL = "taiwooloyede49@gmail.com"


@dataclass
class Post:
    slug: str
    title: str
    seo_title: str
    description: str
    published: date
    category: str
    author: str
    keywords: str
    featured: bool
    body_markdown: str
    body_html: str
    read_minutes: int

    @property
    def url(self) -> str:
        return f"{SITE_URL}/blog/{self.slug}.html"

    @property
    def display_date(self) -> str:
        return self.published.strftime("%d %B %Y").lstrip("0")


def parse_front_matter(path: Path) -> tuple[dict[str, str], str]:
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not raw.startswith("---\n"):
        raise ValueError(f"{path.name}: the file must begin with ---")
    parts = raw.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError(f"{path.name}: the opening information must end with ---")

    metadata: dict[str, str] = {}
    for line in parts[0][4:].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"{path.name}: invalid information line: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip().lower()] = value.strip().strip('"').strip("'")
    return metadata, parts[1].strip()


def inline_markdown(text: str) -> str:
    safe = html.escape(text, quote=True)
    safe = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"(?<!\*)\*(.+?)\*(?!\*)", r"<em>\1</em>", safe)

    def link(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        if target.lower().startswith("javascript:"):
            return label
        return f'<a href="{target}">{label}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, safe)


def render_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue

        if line.startswith("### "):
            output.append(f"<h3>{inline_markdown(line[4:])}</h3>")
            index += 1
            continue
        if line.startswith("## "):
            output.append(f"<h2>{inline_markdown(line[3:])}</h2>")
            index += 1
            continue
        if line.startswith("# "):
            output.append(f"<h2>{inline_markdown(line[2:])}</h2>")
            index += 1
            continue
        if line == "---":
            output.append("<hr />")
            index += 1
            continue
        if line.startswith("> "):
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("> "):
                quote_lines.append(lines[index].strip()[2:])
                index += 1
            output.append(f"<blockquote>{inline_markdown(' '.join(quote_lines))}</blockquote>")
            continue
        if line.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("- "):
                items.append(f"<li>{inline_markdown(lines[index].strip()[2:])}</li>")
                index += 1
            output.append(f"<ul>{''.join(items)}</ul>")
            continue
        if re.match(r"\d+\.\s", line):
            items = []
            while index < len(lines) and re.match(r"\d+\.\s", lines[index].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[index].strip())
                items.append(f"<li>{inline_markdown(item)}</li>")
                index += 1
            output.append(f"<ol>{''.join(items)}</ol>")
            continue

        paragraph = [line]
        index += 1
        while index < len(lines) and lines[index].strip():
            next_line = lines[index].strip()
            if next_line.startswith(("# ", "## ", "### ", "> ", "- ")) or re.match(r"\d+\.\s", next_line) or next_line == "---":
                break
            paragraph.append(next_line)
            index += 1
        output.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")

    return "\n".join(output)


def load_posts() -> list[Post]:
    posts: list[Post] = []
    for path in sorted(CONTENT_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        metadata, body = parse_front_matter(path)
        if metadata.get("draft", "false").lower() in {"true", "yes", "1"}:
            continue

        required = ["title", "description", "date", "category"]
        missing = [key for key in required if not metadata.get(key)]
        if missing:
            raise ValueError(f"{path.name}: missing {', '.join(missing)}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", path.stem):
            raise ValueError(f"{path.name}: use only lowercase letters, numbers and hyphens in the filename")
        try:
            published = datetime.strptime(metadata["date"], "%Y-%m-%d").date()
        except ValueError as error:
            raise ValueError(f"{path.name}: date must use YYYY-MM-DD") from error

        word_count = len(re.findall(r"\b[\w’'-]+\b", body))
        posts.append(
            Post(
                slug=path.stem,
                title=metadata["title"],
                seo_title=metadata.get("seo_title", metadata["title"]),
                description=metadata["description"],
                published=published,
                category=metadata["category"],
                author=metadata.get("author", "Taiwo Oloyede"),
                keywords=metadata.get("keywords", ""),
                featured=metadata.get("featured", "false").lower() in {"true", "yes", "1"},
                body_markdown=body,
                body_html=render_markdown(body),
                read_minutes=max(1, math.ceil(word_count / 200)),
            )
        )
    return sorted(posts, key=lambda post: (post.published, post.title), reverse=True)


def brand(prefix: str) -> str:
    return f'''<a class="brand" href="{prefix}index.html" aria-label="OTA Tutoring home"><span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 40 40"><path d="M7 29.5V12.8c4.8-2 9.1-1.3 13 2.2v17.1c-3.9-3.5-8.2-4.4-13-2.6Z"/><path d="M33 29.5V12.8c-4.8-2-9.1-1.3-13 2.2v17.1c3.9-3.5 8.2-4.4 13-2.6Z"/><path d="M20 15v17"/></svg></span><span><strong>OTA Tutoring</strong><small>Guided learning. Lasting progress.</small></span></a>'''


def header(prefix: str) -> str:
    return f'''<header class="site-header" data-header><div class="container nav-wrap">{brand(prefix)}<button class="menu-button" type="button" aria-expanded="false" aria-controls="primary-navigation" data-menu-button><span class="sr-only">Open menu</span><span></span><span></span><span></span></button><nav id="primary-navigation" class="primary-nav" aria-label="Primary navigation" data-menu><a href="{prefix}index.html">Home</a><a href="{prefix}index.html#services">Services</a><a href="{prefix}index.html#regions">Regions</a><a href="{prefix}index.html#approach">Approach</a><a href="{prefix}index.html#pricing">Pricing</a><div class="nav-dropdown" data-dropdown><button class="nav-dropdown-toggle" type="button" aria-expanded="false" aria-haspopup="true" aria-current="page" data-dropdown-button>Learning Hub <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m4 6 4 4 4-4"/></svg></button><div class="dropdown-menu"><a href="{prefix}learning-hub.html#free-resources"><strong>Free Resources</strong><small>Guides, articles and worksheets</small></a><a href="{prefix}learning-hub.html#premium-resources"><strong>Premium Resources</strong><small>Learning plans and revision packs</small></a><a href="{prefix}blog.html" aria-current="page"><strong>Blog Articles</strong><small>Advice for learners and parents</small></a><a href="{prefix}learning-hub.html#resource-search"><strong>Search Resources</strong><small>Find support by subject or exam</small></a></div></div><div class="nav-dropdown" data-dropdown><button class="nav-dropdown-toggle" type="button" aria-expanded="false" aria-haspopup="true" data-dropdown-button>About Us <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m4 6 4 4 4-4"/></svg></button><div class="dropdown-menu"><a href="{prefix}index.html#about"><strong>Meet Taiwo</strong><small>Your international online tutor</small></a><a href="{prefix}index.html#proof"><strong>Experience &amp; Qualifications</strong><small>Background and teaching credentials</small></a><a href="{prefix}testimonials.html"><strong>Testimonials</strong><small>Verified feedback from families</small></a></div></div><a class="nav-cta" href="{BOOKING_URL}">Book a Free Call</a></nav></div></header>'''


def footer(prefix: str) -> str:
    return f'''<footer class="site-footer"><div class="container footer-top"><div class="footer-brand">{brand(prefix)}</div><nav aria-label="Footer navigation"><a href="{prefix}index.html#services">Services</a><a href="{prefix}learning-hub.html">Learning Hub</a><a href="{prefix}blog.html">Blog</a><a href="{prefix}testimonials.html">Testimonials</a><a href="{prefix}privacy.html">Privacy</a><a href="mailto:{EMAIL}">Email</a></nav></div><div class="container footer-bottom"><p>© <span data-year></span> OTA Tutoring.</p><p>International online tutoring.</p></div></footer>'''


def post_card(post: Post, featured: bool = False) -> str:
    classes = "blog-card reveal"
    if featured:
        classes += " featured-post"
    search = html.escape(f"{post.title} {post.description} {post.category} {post.keywords}", quote=True)
    return f'''<article class="{classes}" data-blog-item data-search="{search}"><a class="blog-card-visual" href="blog/{post.slug}.html" aria-label="Read {html.escape(post.title, quote=True)}"><span>OTA TUTORING</span><strong>{html.escape(post.category)}</strong><i aria-hidden="true">✦</i></a><div class="blog-card-copy"><div class="blog-meta"><span>{html.escape(post.category)}</span><time datetime="{post.published.isoformat()}">{post.display_date}</time><span>{post.read_minutes} min read</span></div><h2><a href="blog/{post.slug}.html">{html.escape(post.title)}</a></h2><p>{html.escape(post.description)}</p><a class="text-link" href="blog/{post.slug}.html">Read article →</a></div></article>'''


def build_blog_index(posts: list[Post]) -> str:
    featured_post = next((post for post in posts if post.featured), posts[0] if posts else None)
    cards = "\n".join(post_card(post, featured=post is featured_post) for post in posts)
    if not cards:
        cards = '<p class="blog-empty">No articles have been published yet.</p>'
    schema = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "OTA Tutoring Blog",
        "url": f"{SITE_URL}/blog.html",
        "description": "Practical learning and exam advice for international learners and their parents.",
        "publisher": {"@type": "EducationalOrganization", "name": "OTA Tutoring", "url": f"{SITE_URL}/"},
        "blogPost": [
            {"@type": "BlogPosting", "headline": post.title, "url": post.url, "datePublished": post.published.isoformat()}
            for post in posts
        ],
    }
    return f'''<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Read practical GCSE, IGCSE, SAT and international-school learning advice for students and parents from OTA Tutoring." />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <meta name="theme-color" content="#14213f" />
    <link rel="canonical" href="{SITE_URL}/blog.html" />
    <link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="OTA Tutoring" />
    <meta property="og:title" content="Learning Advice for Students and Parents | OTA Tutoring Blog" />
    <meta property="og:description" content="Clear, practical articles about GCSE preparation, study habits and confident learning." />
    <meta property="og:url" content="{SITE_URL}/blog.html" />
    <meta property="og:image" content="{SITE_URL}/assets/ota-social-preview.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <title>GCSE, IGCSE &amp; Study Advice Blog | OTA Tutoring</title>
    <link rel="stylesheet" href="styles.css" />
    <link rel="stylesheet" href="pages.css" />
    <link rel="stylesheet" href="blog.css" />
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
  </head>
  <body class="subpage blog-page">
    <a class="skip-link" href="#main-content">Skip to content</a>
    {header("")}
    <main id="main-content">
      <section class="page-hero blog-hero"><div class="container page-hero-grid"><div class="page-hero-copy reveal"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="learning-hub.html">Learning Hub</a><span>/</span><span>Blog</span></nav><p class="eyebrow"><span></span> OTA Tutoring blog</p><h1>Clear advice for calmer, more confident learning.</h1><p>Practical articles for students and parents navigating GCSE, IGCSE, international curricula, exams and everyday learning.</p></div><aside class="page-hero-card reveal"><span>Written from real teaching</span><h2>Useful ideas you can actually apply.</h2><p>Each article turns common learning problems into simple, realistic next steps for families and students.</p><a class="text-link" href="learning-hub.html">Explore the Learning Hub →</a></aside></div></section>
      <section class="blog-search"><div class="container"><label for="blog-search-input"><span>Search blog articles</span><input id="blog-search-input" type="search" placeholder="Search GCSE, summer, revision…" autocomplete="off" data-blog-search /></label></div></section>
      <section class="page-section"><div class="container"><div class="hub-section-heading reveal"><div><p class="eyebrow"><span></span> Latest articles</p><h2>Support for the next step.</h2></div><p>New articles are added regularly to help students maintain progress and prepare with less pressure.</p></div><div class="blog-grid" data-blog-list>{cards}</div><p class="blog-empty" hidden data-blog-empty>No article matches that search yet.</p></div></section>
      <section class="page-cta"><div class="container page-cta-inner"><div><h2>Need advice for one particular learner?</h2><p>Book a free parent consultation to discuss the learner’s current level, curriculum and most useful next step.</p></div><a class="button button-mint" href="{BOOKING_URL}">Book a Free Call →</a></div></section>
    </main>
    {footer("")}
    <script src="script.js"></script>
  </body>
</html>
'''


def build_post_page(post: Post) -> str:
    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post.title,
        "description": post.description,
        "datePublished": post.published.isoformat(),
        "dateModified": post.published.isoformat(),
        "author": {"@type": "Person", "name": post.author},
        "publisher": {"@type": "EducationalOrganization", "name": "OTA Tutoring", "url": f"{SITE_URL}/"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": post.url},
        "image": f"{SITE_URL}/assets/ota-social-preview.png",
        "keywords": post.keywords,
        "inLanguage": "en-GB",
    }
    return f'''<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{html.escape(post.description, quote=True)}" />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <meta name="author" content="{html.escape(post.author, quote=True)}" />
    <meta name="theme-color" content="#14213f" />
    <link rel="canonical" href="{post.url}" />
    <link rel="icon" href="../assets/favicon.svg" type="image/svg+xml" />
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="OTA Tutoring" />
    <meta property="og:title" content="{html.escape(post.title, quote=True)}" />
    <meta property="og:description" content="{html.escape(post.description, quote=True)}" />
    <meta property="og:url" content="{post.url}" />
    <meta property="og:image" content="{SITE_URL}/assets/ota-social-preview.png" />
    <meta property="article:published_time" content="{post.published.isoformat()}" />
    <meta property="article:section" content="{html.escape(post.category, quote=True)}" />
    <meta name="twitter:card" content="summary_large_image" />
    <title>{html.escape(post.seo_title)} | OTA Tutoring</title>
    <link rel="stylesheet" href="../styles.css" />
    <link rel="stylesheet" href="../pages.css" />
    <link rel="stylesheet" href="../blog.css" />
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
  </head>
  <body class="subpage blog-post-page">
    <a class="skip-link" href="#main-content">Skip to content</a>
    {header("../")}
    <main id="main-content">
      <article>
        <header class="post-hero"><div class="container post-hero-inner"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span>/</span><a href="../blog.html">Blog</a><span>/</span><span>{html.escape(post.category)}</span></nav><p class="eyebrow"><span></span> {html.escape(post.category)}</p><h1>{html.escape(post.title)}</h1><div class="post-meta"><span>By {html.escape(post.author)}</span><time datetime="{post.published.isoformat()}">{post.display_date}</time><span>{post.read_minutes} min read</span></div></div></header>
        <div class="container post-layout"><div class="blog-prose">{post.body_html}<div class="post-end-note"><span aria-hidden="true">✦</span><p><strong>Keep the momentum going.</strong> A simple, consistent routine can make returning to school feel much more manageable.</p></div></div><aside class="post-aside"><span class="live-pill">Free parent consultation</span><h2>Would personalised support help?</h2><p>Discuss the learner’s current level, curriculum and goals with OTA Tutoring.</p><a class="button button-primary" href="{BOOKING_URL}">Book a Free Call →</a><a class="aside-back-link" href="../blog.html">← Back to all articles</a></aside></div>
      </article>
      <section class="page-cta"><div class="container page-cta-inner"><div><h2>Support that begins with the learner’s real needs.</h2><p>Lessons are personalised, international and designed to build understanding as well as confidence.</p></div><a class="button button-mint" href="{BOOKING_URL}">Choose a time →</a></div></section>
    </main>
    {footer("../")}
    <script src="../script.js"></script>
  </body>
</html>
'''


def update_sitemap(posts: list[Post]) -> None:
    path = ROOT / "sitemap.xml"
    sitemap = path.read_text(encoding="utf-8")
    start = "  <!-- BLOG_POSTS_START -->"
    end = "  <!-- BLOG_POSTS_END -->"
    if start not in sitemap or end not in sitemap:
        raise ValueError("sitemap.xml is missing the blog post markers")
    entries = "\n".join(
        f"  <url><loc>{post.url}</loc><lastmod>{post.published.isoformat()}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>"
        for post in posts
    )
    replacement = f"{start}\n{entries}\n{end}" if entries else f"{start}\n{end}"
    sitemap = re.sub(re.escape(start) + r".*?" + re.escape(end), replacement, sitemap, flags=re.DOTALL)
    path.write_text(sitemap, encoding="utf-8")


def main() -> None:
    posts = load_posts()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_page in OUTPUT_DIR.glob("*.html"):
        old_page.unlink()
    for post in posts:
        (OUTPUT_DIR / f"{post.slug}.html").write_text(build_post_page(post), encoding="utf-8")
    (ROOT / "blog.html").write_text(build_blog_index(posts), encoding="utf-8")
    update_sitemap(posts)
    noun = "article" if len(posts) == 1 else "articles"
    print(f"Blog updated successfully: {len(posts)} {noun} published.")
    print("Open blog.html to check the result.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(f"Blog build stopped: {error}") from error
