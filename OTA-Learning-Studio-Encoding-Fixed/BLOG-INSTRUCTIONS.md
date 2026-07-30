# How to publish a new blog article

You do not need to design another HTML page. The website will create it for you.

## For every new article

1. Open the `content` folder, then open `blog`.
2. Copy `_template.md` and paste the copy in the same folder.
3. Rename the copy using lowercase words separated by hyphens. Example: `how-to-prepare-for-gcse-maths.md`.
4. Open the copied file and replace the sample title, shorter Google title, description, date, category, keywords and article text.
5. Change `draft: true` to `draft: false` when the article is ready.
6. Save the file.
7. Return to the main `ota-tutoring` folder and double-click `BUILD_BLOG.bat`.
8. Open `blog.html` in your browser to check the Blog page.

The builder automatically:

- creates the complete article page;
- adds the article to `blog.html`;
- gives the article its own SEO-friendly URL;
- adds the title, description, author, date and structured data;
- updates `sitemap.xml`.

Do not edit the generated files inside the `blog` folder. Make corrections in the article’s `.md` file and run `BUILD_BLOG.bat` again.

## Writing options inside an article

- Normal paragraphs can be typed normally.
- A section heading begins with `##` followed by one space.
- A smaller heading begins with `###` followed by one space.
- A bullet point begins with `-` followed by one space.
- Bold text is placed between two asterisks on both sides: `**important text**`.

The filename must not contain spaces, capital letters or special characters. Hyphens are used only in the filename and website address, not in the visible article title.

