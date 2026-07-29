# How to add another premium planner

The planner catalogue is controlled from `products.js`.

1. Export the customer version as a PDF, but do not place that paid PDF in this public GitHub repository.
2. Create a product cover image and save it inside `assets/planners/`.
3. Open `products.js`.
4. Copy one complete product block inside `plannerProducts`.
5. Change its title, price, description, image path and features.
6. Paste the secure checkout link between the quotation marks after `checkoutUrl:`.
7. Save the file and refresh `premium-planners.html`.

When `checkoutUrl` is empty, the website automatically displays “Purchase setup coming soon”. Once a secure checkout link is added, it automatically becomes a working “Buy now” button.

Paid PDFs must be delivered by the checkout platform after payment. Uploading the full PDFs directly to this public repository would allow anyone to download them without paying.
