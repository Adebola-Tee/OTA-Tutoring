// Keep the Blog as a visible primary-navigation item on every page.
// Some older page templates place it inside the Learning Hub dropdown;
// normalise that markup without touching any blog content or generated pages.
document.querySelectorAll('[data-menu]').forEach((navigation) => {
  const directBlogLink = [...navigation.children].find(
    (child) => child.matches?.('a') && child.textContent.trim() === 'Blog'
  );
  const learningHubDropdown = [...navigation.querySelectorAll('[data-dropdown]')].find(
    (dropdown) => dropdown.querySelector('[data-dropdown-button]')?.textContent.includes('Learning Hub')
  );
  const nestedBlogLink = learningHubDropdown
    ? [...learningHubDropdown.querySelectorAll('.dropdown-menu a')].find((link) =>
        link.getAttribute('href')?.endsWith('blog.html')
      )
    : null;

  if (nestedBlogLink) nestedBlogLink.remove();
  if (directBlogLink) return;

  const blogLink = document.createElement('a');
  blogLink.href = nestedBlogLink?.getAttribute('href') || 'blog.html';
  blogLink.textContent = 'Blog';

  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  if (currentPage === 'blog.html' || window.location.pathname.includes('/blog/')) {
    blogLink.setAttribute('aria-current', 'page');
  }

  if (learningHubDropdown) {
    learningHubDropdown.after(blogLink);
    return;
  }

  const learningHubLink = [...navigation.children].find(
    (child) => child.matches?.('a') && child.textContent.trim() === 'Learning Hub'
  );
  if (learningHubLink) learningHubLink.after(blogLink);
  else navigation.querySelector('.nav-cta')?.before(blogLink);
});

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

const storyCarousel = document.querySelector('[data-story-carousel]');
const storyCards = [...document.querySelectorAll('[data-story-card]')];
const storyDots = document.querySelector('[data-story-dots]');
const storyStatus = document.querySelector('[data-story-status]');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let activeStory = 0;
let storyTimer;

const showStory = (index, announce = true) => {
  if (!storyCards.length) return;
  activeStory = (index + storyCards.length) % storyCards.length;
  storyCards.forEach((card, cardIndex) => {
    const isActive = cardIndex === activeStory;
    card.classList.toggle('is-active', isActive);
    card.setAttribute('aria-hidden', String(!isActive));
  });
  storyDots?.querySelectorAll('button').forEach((dot, dotIndex) => {
    const isActive = dotIndex === activeStory;
    dot.classList.toggle('is-active', isActive);
    dot.setAttribute('aria-current', isActive ? 'true' : 'false');
  });
  if (announce && storyStatus) {
    const name = storyCards[activeStory].querySelector('footer strong')?.textContent;
    storyStatus.textContent = `Showing ${name}'s learning progress, ${activeStory + 1} of ${storyCards.length}.`;
  }
};

const stopStoryTimer = () => window.clearInterval(storyTimer);
const startStoryTimer = () => {
  stopStoryTimer();
  if (!storyCards.length || reduceMotion.matches) return;
  storyTimer = window.setInterval(() => showStory(activeStory + 1, false), 5200);
};

if (storyCards.length && storyDots) {
  storyCards.forEach((card, index) => {
    const name = card.querySelector('footer strong')?.textContent || `Story ${index + 1}`;
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.setAttribute('aria-label', `Show ${name}'s progress`);
    dot.addEventListener('click', () => {
      showStory(index);
      startStoryTimer();
    });
    storyDots.append(dot);
  });
  showStory(0, false);
  startStoryTimer();
}

document.querySelector('[data-story-previous]')?.addEventListener('click', () => {
  showStory(activeStory - 1);
  startStoryTimer();
});
document.querySelector('[data-story-next]')?.addEventListener('click', () => {
  showStory(activeStory + 1);
  startStoryTimer();
});
storyCarousel?.addEventListener('mouseenter', stopStoryTimer);
storyCarousel?.addEventListener('mouseleave', startStoryTimer);
storyCarousel?.addEventListener('focusin', stopStoryTimer);
storyCarousel?.addEventListener('focusout', startStoryTimer);
reduceMotion.addEventListener?.('change', startStoryTimer);

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
