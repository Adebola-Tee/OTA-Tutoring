# How to add e-books, planners and templates

The two shop catalogues are controlled from `shop-products.js`.

## Add an e-book

1. Upload the complete e-book PDF to Selar and create its product page.
2. Save only the cover preview inside `assets/products/`. Do not place the complete paid PDF in this public website folder.
3. Open `shop-products.js`.
4. Copy one complete product block inside the `ebooks` list.
5. Change the title, price, description, cover path and features.
6. Paste the unique Selar product link between the quotation marks after `checkoutUrl:`.
7. Save the file and refresh `ebooks.html`.

## Add a general planner or template

Follow the same steps, but copy a product block inside the `general` list and refresh `planners-templates.html`.

When `checkoutUrl` is empty, the website displays “Purchase setup coming soon”. Once the Selar link is added, the button automatically changes to “Buy on Selar”. Every product must have its own Selar link.

The catalogue automatically displays eight products per desktop page in two columns and four rows. If you add more than eight products, numbered page buttons and Previous/Next controls appear automatically. You do not need to edit the pagination.

