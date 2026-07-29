const plannerProducts = [
  {
    title: 'Student Study Planner',
    price: '£4.99',
    description: 'A practical everyday planner for building a clear and manageable study routine.',
    image: 'assets/planners/student-study-planner.svg',
    features: ['13 printable pages', 'Weekly timetable and study-hour tracking', 'Daily targets, topic tracking and reflection'],
    checkoutUrl: ''
  },
  {
    title: 'Exam Preparation Planner',
    price: '£5.99',
    description: 'A focused system for organising revision, tracking mock scores and preparing calmly for exam day.',
    image: 'assets/planners/exam-preparation-planner.svg',
    features: ['13 printable pages', 'Exam countdown and subject revision plans', 'Mock score, weak-topic and confidence tracking'],
    checkoutUrl: ''
  },
  {
    title: 'Ultimate High School Academic Planner',
    price: '£7.99',
    description: 'A complete academic organisation toolkit covering daily, weekly and monthly planning.',
    image: 'assets/planners/ultimate-high-school-academic-planner.svg',
    features: ['12 printable pages', 'Monthly, weekly and daily planning', 'Assignments, projects, habits and progress tracking'],
    checkoutUrl: ''
  },
  {
    title: '90-Day Academic Reset Planner',
    price: '£8.99',
    description: 'A structured 12-week improvement system for students who feel behind, disorganised or underperforming.',
    image: 'assets/planners/90-day-academic-reset-planner.svg',
    features: ['14 printable pages', 'Baseline audit and 12-week roadmap', 'Recovery plans, accountability and confidence sprint'],
    checkoutUrl: ''
  }
];

const productGrid = document.querySelector('[data-product-grid]');
if (productGrid) {
  const productsPerPage = 8;
  const totalPages = Math.ceil(plannerProducts.length / productsPerPage);
  let currentPage = 1;
  const escapeHtml = (value) => String(value).replace(/[&<>'"]/g, (character) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' })[character]);
  const bundleMarkup = '<article class="bundle-card"><div><span class="product-category">Best value bundle</span><h2>Complete Academic Planner Collection</h2><p>All four planners together for study, exams, organisation and long-term academic improvement.</p></div><div class="bundle-price"><strong>£19.99</strong><span>Save £7.97 compared with buying separately</span></div></article>';
  const pagination = document.createElement('nav');
  pagination.className = 'product-pagination';
  pagination.setAttribute('aria-label', 'Academic product pages');
  productGrid.insertAdjacentElement('afterend', pagination);

  const productMarkup = (product) => {
    const action = product.checkoutUrl
      ? `<a class="button button-primary product-action" href="${escapeHtml(product.checkoutUrl)}" rel="noopener">Buy now</a>`
      : '<span class="button button-primary product-action is-disabled" aria-disabled="true">Purchase setup coming soon</span>';
    return `<article class="product-card reveal visible" data-resource-item>
      <div class="product-cover"><img src="${escapeHtml(product.image)}" alt="Cover of ${escapeHtml(product.title)}" loading="lazy" /></div>
      <div class="product-copy"><span class="product-category">Printable academic planner</span><h2>${escapeHtml(product.title)}</h2><p>${escapeHtml(product.description)}</p>
      <ul class="product-features">${product.features.map((feature) => `<li>${escapeHtml(feature)}</li>`).join('')}</ul>
      <div class="product-price">${escapeHtml(product.price)}<small>Digital PDF · instant delivery after checkout is connected</small></div>${action}</div>
    </article>`;
  };

  const renderPage = () => {
    const firstProduct = (currentPage - 1) * productsPerPage;
    productGrid.innerHTML = plannerProducts.slice(firstProduct, firstProduct + productsPerPage).map(productMarkup).join('') + (currentPage === totalPages ? bundleMarkup : '');
    pagination.hidden = totalPages <= 1;
    pagination.innerHTML = totalPages <= 1 ? '' : `<button type="button" data-page="prev" ${currentPage === 1 ? 'disabled' : ''} aria-label="Previous academic product page">← Previous</button>${Array.from({ length: totalPages }, (_, index) => {
      const page = index + 1;
      return `<button type="button" data-page="${page}" ${page === currentPage ? 'aria-current="page"' : ''} aria-label="Academic product page ${page}">${page}</button>`;
    }).join('')}<button type="button" data-page="next" ${currentPage === totalPages ? 'disabled' : ''} aria-label="Next academic product page">Next →</button>`;
  };

  pagination.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-page]');
    if (!button || button.disabled) return;
    const requestedPage = button.dataset.page;
    currentPage = requestedPage === 'prev' ? currentPage - 1 : requestedPage === 'next' ? currentPage + 1 : Number(requestedPage);
    renderPage();
    productGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  renderPage();
  document.querySelector('[data-product-count]').textContent = `${plannerProducts.length} planners`;
}
