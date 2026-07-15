# OTA Tutoring Website

A responsive multi-page tutoring website built in the **Guided Momentum** visual direction.

## Open the website

Open `index.html` in any modern browser. No installation or build step is required.

## What is included

- OTA Tutoring homepage
- Cal.com free parent consultation booking
- Email-only contact
- Region pages for the UK, Switzerland/Europe, United States, Australia and Asia
- IGCSE revision article
- Searchable Learning Hub with free and planned premium resource categories
- Reusable blog publishing system with individual SEO-ready article pages
- First article for Year 10 to Year 11 Foundation GCSE students
- About Us navigation with experience, qualifications and verified parent feedback
- Privacy information
- Search and social metadata, structured data, `sitemap.xml` and `robots.txt`
- Responsive layouts for desktop, tablet and mobile

## Important before publishing

The SEO files currently use `https://www.otatutoring.com` as the planned website address. If a different domain is purchased, replace that address everywhere in the project before launch. Update `sitemap.xml` and `robots.txt` as part of the same change.

The pricing section intentionally does not invent lesson prices. It lists the supported currencies and explains that the exact rate is confirmed after consultation. Add approved rates only after the business owner chooses them.

The testimonials page includes only genuine feedback already supplied to the project, with the parent’s name withheld for privacy. Add more quotations only after the wording is verified and public-use permission is confirmed.

## Files

- `index.html` — website content and structure
- `styles.css` — design and responsive layout
- `pages.css` — shared layouts for country pages, article and privacy page
- `learning-hub.html` — searchable free and premium resource directory
- `testimonials.html` — verified parent feedback and review policy
- `blog.html` — automatically generated blog index
- `content/blog/` — the editable article files and reusable article template
- `generate_blog.py` and `BUILD_BLOG.bat` — automatic blog page and sitemap builder
- `BLOG-INSTRUCTIONS.md` — simple instructions for publishing future articles
- `blog.css` — responsive blog listing and article styling
- `script.js` — mobile navigation, accessible dropdowns, resource search and scroll effects
- `robots.txt` and `sitemap.xml` — search-engine discovery files
- `assets/` — favicon and social sharing image

To publish another article, follow `BLOG-INSTRUCTIONS.md`. Edit a copied Markdown template, then run `BUILD_BLOG.bat`; do not manually edit the generated article HTML.
