const shopCatalogues = {
  ebooks: [
    {
      title: 'Where the World Grows Quiet',
      price: '£7.99',
      description: 'A restorative journey through rain, trees, rivers, sunrise, sunset and the quiet wisdom of the natural world.',
      image: 'assets/products/where-the-world-grows-quiet-cover.png',
      features: ['60-page digital e-book', 'Nature, reflection and emotional restoration', 'Written by Taiwo Oloyede'],
      checkoutUrl: ''
    },
    {
      title: 'Her Own Money',
      price: '£20.00',
      description: 'A practical guide to building financial dignity, earning power and the freedom to make important life decisions without fear or complete dependence.',
      image: 'assets/products/her-own-money-cover.png',
      features: ['92-page digital e-book', 'Financial confidence, choices and independence', 'Includes worksheets, scripts and a 90-day action plan'],
      checkoutUrl: ''
    },
    {
      title: 'Rebuilding Her After Heartbreak',
      price: '£15.00',
      description: 'A compassionate guide to healing, rediscovering yourself and finding peace after rejection, divorce or betrayal.',
      image: 'assets/products/rebuilding-her-after-heartbreak-cover.png',
      features: ['46-page digital e-book', 'Emotional first aid and healing journal', 'Includes a 30-day rebuilding plan'],
      checkoutUrl: ''
    },
    {
      title: 'The Woman Who No Longer Shrinks',
      price: '£15.00',
      description: 'A practical guide for women ready to stop people-pleasing, establish healthy boundaries and speak confidently without guilt.',
      image: 'assets/products/the-woman-who-no-longer-shrinks-cover.png',
      features: ['44-page digital e-book', 'Practical boundary scripts and exercises', 'Includes a 30-day return-to-yourself plan'],
      checkoutUrl: ''
    },
    {
      title: 'Visible, Valuable and Unapologetic',
      price: '£15.00',
      description: 'A field guide to overcoming imposter syndrome, communicating your value and building unmistakable professional authority.',
      image: 'assets/products/visible-valuable-and-unapologetic-cover.png',
      features: ['48-page digital e-book', 'Career scripts, dashboards and field guides', 'Includes a 90-day visibility campaign'],
      checkoutUrl: ''
    }
  ],
  general: [
    {
      title: 'ADHD Daily Brain Dump & Priority Planner',
      price: '£8.99',
      description: 'A gentle planning system for clearing mental clutter, choosing priorities and moving through the day with less overwhelm.',
      image: 'assets/products/adhd-daily-brain-dump-planner-cover.png',
      features: ['24 printable planning pages', 'Brain dump, priority and task-sorting tools', 'Focus, routine, reflection and self-care pages'],
      checkoutUrl: ''
    },
    {
      title: 'Shadow Work Journal & Healing Planner',
      price: '£9.99',
      description: 'A guided journal for self-reflection, emotional honesty, healing patterns and rebuilding with greater awareness.',
      image: 'assets/products/shadow-work-journal-healing-planner-cover.png',
      features: ['27 printable pages', 'Shadow prompts and emotional-pattern trackers', 'Boundaries, triggers, forgiveness and growth tools'],
      checkoutUrl: ''
    },
    {
      title: 'Therapy Session Notes & Progress Tracker',
      price: '£9.99',
      description: 'A calm system for recording therapy sessions, tracking emotional progress and organising personal growth between appointments.',
      image: 'assets/products/therapy-session-notes-progress-tracker-cover.png',
      features: ['25 printable pages', 'Session notes, goals and mood tracking', 'Progress reviews and reflection prompts'],
      checkoutUrl: ''
    },
    {
      title: 'Neurodivergent Business Owner Planner',
      price: '£9.99',
      description: 'A supportive business planner for entrepreneurs who need flexible systems that work with their brain, energy and capacity.',
      image: 'assets/products/neurodivergent-business-owner-planner-cover.png',
      features: ['24 printable pages', 'Energy-aware planning and task batching', 'Client, content, money and business review tools'],
      checkoutUrl: ''
    },
    {
      title: 'Nervous System Reset Tracker',
      price: '£9.99',
      description: 'A gentle tracker for noticing stress patterns, building grounding routines and supporting steadier everyday rhythms.',
      image: 'assets/products/nervous-system-reset-tracker-cover.png',
      features: ['24 printable pages', 'Stress, capacity and grounding trackers', 'Body-awareness and calming routine prompts'],
      checkoutUrl: ''
    },
    {
      title: 'Inner Child Healing Workbook & Planner',
      price: '£9.99',
      description: 'A reflective workbook for exploring old emotional patterns, reconnecting with unmet needs and practising gentler self-support.',
      image: 'assets/products/inner-child-healing-workbook-planner-cover.png',
      features: ['24 printable pages', 'Guided reflection and reparenting exercises', 'Progress, needs and emotional-safety planning'],
      checkoutUrl: ''
    },
    {
      title: 'Depression Recovery Tracker & Self-Care Planner',
      price: '£9.99',
      description: 'A softly structured planner for tracking mood, routines, support and small steps during recovery.',
      image: 'assets/products/depression-recovery-tracker-self-care-planner-cover.png',
      features: ['24 printable pages', 'Mood, routine and self-care tracking', 'Small-step planning and support reminders'],
      checkoutUrl: ''
    },
    {
      title: 'Grief & Loss Processing Journal',
      price: '£9.99',
      description: 'A gentle guided journal for moving through grief with space for memories, emotions, rituals, reflection and healing.',
      image: 'assets/products/grief-loss-processing-journal-cover.png',
      features: ['28 printable pages', 'Memory, emotion and support prompts', 'Ritual, reflection and continuing-bond exercises'],
      checkoutUrl: ''
    },
    {
      title: 'Autism Sensory & Routine Daily Planner',
      price: '£9.99',
      description: 'A supportive daily planner for tracking sensory needs, routines, transitions and regulation with greater predictability.',
      image: 'assets/products/autism-sensory-routine-daily-planner-cover.png',
      features: ['27 printable pages', 'Sensory profile and routine planning', 'Transition, regulation and overwhelm tracking'],
      checkoutUrl: ''
    },
    {
      title: 'Burnout Recovery Planner',
      price: '£9.99',
      description: 'A practical recovery planner for reducing overload, restoring capacity and rebuilding sustainable routines without pressure.',
      image: 'assets/products/burnout-recovery-planner-cover.png',
      features: ['24 printable pages', 'Burnout, energy and boundary tracking', 'Rest, recovery and realistic routine planning'],
      checkoutUrl: ''
    }
  ]
};

const catalogueRoot = document.querySelector('[data-catalogue]');
if (catalogueRoot) {
  const catalogueName = document.body.dataset.catalogue;
  const products = shopCatalogues[catalogueName] || [];
  const productsPerPage = 8;
  const totalPages = Math.ceil(products.length / productsPerPage);
  let currentPage = 1;
  const escapeHtml = (value) => String(value).replace(/[&<>'"]/g, (character) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' })[character]);

  const pagination = document.createElement('nav');
  pagination.className = 'catalogue-pagination';
  pagination.setAttribute('aria-label', 'Product pages');
  catalogueRoot.insertAdjacentElement('afterend', pagination);

  const productMarkup = (product) => {
    const action = product.checkoutUrl
      ? `<a class="button button-primary catalogue-action" href="${escapeHtml(product.checkoutUrl)}" target="_blank" rel="noopener">Buy on Selar</a>`
      : '<span class="button button-primary catalogue-action is-disabled" aria-disabled="true">Purchase setup coming soon</span>';
    return `<article class="catalogue-card reveal visible">
      <div class="catalogue-cover"><img src="${escapeHtml(product.image)}" alt="Cover of ${escapeHtml(product.title)}" loading="lazy" /></div>
      <div class="catalogue-copy"><span class="product-kicker">Digital product</span><h2>${escapeHtml(product.title)}</h2><p>${escapeHtml(product.description)}</p>
      <ul class="catalogue-features">${product.features.map((feature) => `<li>${escapeHtml(feature)}</li>`).join('')}</ul>
      <div class="catalogue-price">${escapeHtml(product.price)}<small>Secure payment and delivery through Selar</small></div>${action}</div>
    </article>`;
  };

  const renderPage = () => {
    const firstProduct = (currentPage - 1) * productsPerPage;
    catalogueRoot.innerHTML = products.slice(firstProduct, firstProduct + productsPerPage).map(productMarkup).join('');
    pagination.hidden = totalPages <= 1;
    pagination.innerHTML = totalPages <= 1 ? '' : `<button type="button" data-page="prev" ${currentPage === 1 ? 'disabled' : ''} aria-label="Previous product page">← Previous</button>${Array.from({ length: totalPages }, (_, index) => {
      const page = index + 1;
      return `<button type="button" data-page="${page}" ${page === currentPage ? 'aria-current="page"' : ''} aria-label="Product page ${page}">${page}</button>`;
    }).join('')}<button type="button" data-page="next" ${currentPage === totalPages ? 'disabled' : ''} aria-label="Next product page">Next →</button>`;
  };

  pagination.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-page]');
    if (!button || button.disabled) return;
    const requestedPage = button.dataset.page;
    currentPage = requestedPage === 'prev' ? currentPage - 1 : requestedPage === 'next' ? currentPage + 1 : Number(requestedPage);
    renderPage();
    catalogueRoot.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  renderPage();

  const count = document.querySelector('[data-catalogue-count]');
  if (count) count.textContent = `${products.length} product${products.length === 1 ? '' : 's'}`;
}
