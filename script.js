const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('[data-menu-button]');
const menu = document.querySelector('[data-menu]');
const dropdowns = [...document.querySelectorAll('[data-dropdown]')];

const updateHeader = () => header?.classList.toggle('scrolled', window.scrollY > 14);
updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });

const closeMenu = () => {
  menuButton?.setAttribute('aria-expanded', 'false');
  menu?.classList.remove('open');
  document.body.classList.remove('menu-open');
  dropdowns.forEach((dropdown) => {
    dropdown.classList.remove('open');
    dropdown.querySelector('[data-dropdown-button]')?.setAttribute('aria-expanded', 'false');
  });
  if (dropdowns.some((dropdown) => dropdown.contains(document.activeElement))) {
    document.activeElement?.blur();
  }
};

menuButton?.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!isOpen));
  menu?.classList.toggle('open', !isOpen);
  document.body.classList.toggle('menu-open', !isOpen);
});

menu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
dropdowns.forEach((dropdown) => {
  const button = dropdown.querySelector('[data-dropdown-button]');
  button?.addEventListener('click', (event) => {
    event.stopPropagation();
    const willOpen = !dropdown.classList.contains('open');
    dropdowns.forEach((otherDropdown) => {
      otherDropdown.classList.remove('open');
      otherDropdown.querySelector('[data-dropdown-button]')?.setAttribute('aria-expanded', 'false');
    });
    dropdown.classList.toggle('open', willOpen);
    button.setAttribute('aria-expanded', String(willOpen));
  });
});

document.addEventListener('click', () => {
  dropdowns.forEach((dropdown) => {
    dropdown.classList.remove('open');
    dropdown.querySelector('[data-dropdown-button]')?.setAttribute('aria-expanded', 'false');
  });
  if (dropdowns.some((dropdown) => dropdown.contains(document.activeElement))) {
    document.activeElement?.blur();
  }
});

window.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') closeMenu();
});

const revealObserver = 'IntersectionObserver' in window
  ? new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.12 }
    )
  : null;

document.querySelectorAll('.reveal').forEach((element) => {
  if (revealObserver) revealObserver.observe(element);
  else element.classList.add('visible');
});

document.querySelectorAll('[data-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});

const resourceSearch = document.querySelector('[data-resource-search]');
const resourceItems = [...document.querySelectorAll('[data-resource-item]')];
const noResourceResults = document.querySelector('[data-resource-empty]');

resourceSearch?.addEventListener('input', () => {
  const query = resourceSearch.value.trim().toLowerCase();
  let visibleCount = 0;

  resourceItems.forEach((item) => {
    const searchableText = `${item.textContent} ${item.dataset.search || ''}`.toLowerCase();
    const isVisible = !query || searchableText.includes(query);
    item.hidden = !isVisible;
    if (isVisible) visibleCount += 1;
  });

  if (noResourceResults) noResourceResults.hidden = visibleCount > 0;
});

const blogSearch = document.querySelector('[data-blog-search]');
const blogItems = [...document.querySelectorAll('[data-blog-item]')];
const noBlogResults = document.querySelector('[data-blog-empty]');

blogSearch?.addEventListener('input', () => {
  const query = blogSearch.value.trim().toLowerCase();
  let visibleCount = 0;

  blogItems.forEach((item) => {
    const searchableText = `${item.textContent} ${item.dataset.search || ''}`.toLowerCase();
    const isVisible = !query || searchableText.includes(query);
    item.hidden = !isVisible;
    if (isVisible) visibleCount += 1;
  });

  if (noBlogResults) noBlogResults.hidden = visibleCount > 0;
});
