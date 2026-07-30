# OTA Learning Studio Website

A responsive multi-page tutoring website built in the **Guided Momentum** visual direction.

## Open the website

Open `index.html` in any modern browser. No installation or build step is required.

## What is included

- OTA Learning Studio homepage
- Cal.com free parent consultation booking
- Email-only contact
- Region pages for the UK, Switzerland/Europe, United States, Australia and Asia
- IGCSE revision article
- Searchable Learning Hub with free resources and a premium academic planner catalogue
- Four premium planner listings with launch prices and safe checkout placeholders
- Reusable `products.js` catalogue for adding future planners without rebuilding the page
- Digital Shop hub with three distinct collections: E-books, General Planners & Templates, and Academic Resources
- Reusable e-book and general-product catalogues with individual Selar checkout placeholders
- Compact responsive horizontal product cards with automatic eight-item numbered pagination
- Ten general planners and templates, including nine wellbeing, neurodivergence and recovery tools
- Reusable blog publishing system with individual SEO-ready article pages
- First article for Year 10 to Year 11 Foundation GCSE students
- About Us navigation with experience, qualifications and verified parent feedback
- Privacy information
- Search and social metadata, structured data, `sitemap.xml` and `robots.txt`
- Responsive layouts for desktop, tablet and mobile

## Important before publishing

The SEO files currently use `https://otalearningstudio.com` as the planned website address. If a different domain is purchased, replace that address everywhere in the project before launch. Update `sitemap.xml` and `robots.txt` as part of the same change.

The pricing section intentionally does not invent lesson prices. It lists the supported currencies and explains that the exact rate is confirmed after consultation. Add approved rates only after the business owner chooses them.

The testimonials page includes only genuine feedback already supplied to the project, with the parent’s name withheld for privacy. Add more quotations only after the wording is verified and public-use permission is confirmed.

## Files

- `index.html` — website content and structure
- `styles.css` — design and responsive layout
- `pages.css` — shared layouts for country pages, article and privacy page
- `learning-hub.html` — searchable free and premium resource directory
- `premium-planners.html` — premium planner catalogue and prices
- `products.js` and `products.css` — reusable planner data and product design
- `PRODUCT-INSTRUCTIONS.md` — simple instructions for adding future planners
- `shop.html` — the main digital shop and three-category directory
- `ebooks.html` — reusable e-book catalogue
- `planners-templates.html` — reusable general planners and templates catalogue
- `shop-products.js` and `shop.css` — editable shop data and responsive product styling
- `SHOP-INSTRUCTIONS.md` — instructions for adding future e-books, planners, templates and Selar links
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

To add another premium planner, follow `PRODUCT-INSTRUCTIONS.md`. Keep paid PDF files outside this public repository and place only product previews and secure checkout links on the website.

