(() => {
  if (!document.querySelector('.consultation-modal')) {
    document.body.insertAdjacentHTML('beforeend', `
      <div class="consultation-modal" id="consultation" hidden>
        <button class="consultation-backdrop" type="button" data-consultation-close aria-label="Close consultation form"></button>
        <section class="consultation-panel" role="dialog" aria-modal="true" aria-labelledby="consultation-title" tabindex="-1">
          <header class="consultation-header">
            <div class="consultation-heading">
              <span class="consultation-whatsapp" aria-hidden="true">☎</span>
              <div><h2 id="consultation-title">Start your free consultation</h2><p>Tell me about the learner and I’ll reply on WhatsApp.</p></div>
            </div>
            <button class="consultation-close" type="button" data-consultation-close aria-label="Close consultation form">×</button>
          </header>
          <form class="consultation-form" data-consultation-form>
            <fieldset>
              <legend>What support are you looking for? <span>*</span></legend>
              <div class="choice-grid choice-grid-wide">
                <label><input type="radio" name="support" value="A free consultation" required><span>Free consultation</span></label>
                <label><input type="radio" name="support" value="A diagnostic assessment"><span>Diagnostic assessment</span></label>
                <label><input type="radio" name="support" value="Regular tutoring"><span>Regular tutoring</span></label>
              </div>
            </fieldset>
            <div class="consultation-field-row">
              <label>Country or region <span>*</span><input type="text" name="country" autocomplete="country-name" placeholder="e.g. United Kingdom" required></label>
              <label>Student’s year or grade <span>*</span><input type="text" name="year" placeholder="e.g. Year 10 / Grade 9" required></label>
            </div>
            <label>Curriculum or exam <span>*</span><input type="text" name="curriculum" placeholder="e.g. GCSE, IGCSE, IB, SAT" required></label>
            <fieldset data-subject-group>
              <legend>Which subject(s)? <span>*</span></legend>
              <div class="choice-grid">
                <label><input type="checkbox" name="subjects" value="Mathematics"><span>Mathematics</span></label>
                <label><input type="checkbox" name="subjects" value="English"><span>English</span></label>
                <label><input type="checkbox" name="subjects" value="Biology"><span>Biology</span></label>
                <label><input type="checkbox" name="subjects" value="Chemistry"><span>Chemistry</span></label>
                <label><input type="checkbox" name="subjects" value="Physics"><span>Physics</span></label>
                <label><input type="checkbox" name="subjects" value="General Science"><span>General Science</span></label>
                <label><input type="checkbox" name="subjects" value="Computer Science / Coding"><span>Computer Science / Coding</span></label>
                <label><input type="checkbox" name="subjects" value="SAT / admissions preparation"><span>SAT / Admissions</span></label>
                <label><input type="checkbox" name="subjects" value="Other"><span>Other</span></label>
              </div>
              <p class="consultation-error" data-subject-error hidden>Please select at least one subject.</p>
            </fieldset>
            <div class="consultation-field-row">
              <label>Parent or student name <span>*</span><input type="text" name="name" autocomplete="name" required></label>
              <label>WhatsApp phone number <span>*</span><input type="tel" name="phone" autocomplete="tel" placeholder="Include country code" required></label>
            </div>
            <label>Email address <span>*</span><input type="email" name="email" autocomplete="email" placeholder="you@example.com" required></label>
            <label>What would you like help with? <span>*</span><textarea name="message" rows="3" placeholder="Briefly describe the learner’s needs, difficulties or goals." required></textarea></label>
            <p class="consultation-privacy">Your details are used only to respond to this tutoring enquiry. WhatsApp will open with your message ready to send.</p>
            <button class="consultation-submit" type="submit"><span aria-hidden="true">◉</span> Continue to WhatsApp</button>
          </form>
        </section>
      </div>`);
  }

  const modal = document.querySelector('.consultation-modal');
  const panel = modal?.querySelector('.consultation-panel');
  const form = modal?.querySelector('[data-consultation-form]');
  const subjectError = modal?.querySelector('[data-subject-error]');
  const whatsappNumber = '2348079675840';
  let returnFocus = null;
  let started = false;

  if (!modal || !panel || !form) return;

  // A first enquiry should not require two contact channels or an exam board.
  ['phone', 'email', 'curriculum'].forEach((name) => {
    const field = form.elements.namedItem(name);
    if (!field) return;
    field.required = false;
    const label = field.closest('label');
    label.querySelector('span')?.remove();
    label.firstChild.textContent = label.firstChild.textContent.trim() + ' (optional) ';
  });
  form.querySelector('input[name="support"]').checked = true;
  const note = form.querySelector('.consultation-privacy');
  note.textContent = 'Next, WhatsApp opens with your message. Press Send there to contact Taiwo. Nothing is booked or paid for at this stage.';
  form.insertAdjacentHTML('afterend', '<section class="consultation-next" hidden aria-live="polite"><h3>Your message is ready</h3><p>You still need to press Send in WhatsApp. Taiwo will then discuss suitable lesson times and confirm the fee before you book.</p><button type="button" class="consultation-reopen">Open WhatsApp again</button><p>Prefer email? <button type="button" class="consultation-email">Send this enquiry by email</button></p></section>');
  const next = modal.querySelector('.consultation-next');
  const track = (name) => window.otaTrack?.(name, { enquiry_method: 'whatsapp' });
  form.addEventListener('input', () => {
    if (!started) { started = true; track('consultation_start'); }
  });

  const aside = document.querySelector('.post-aside');
  if (aside) {
    const base = window.location.pathname.includes('/blog/') ? '../' : '';
    aside.querySelector('p').textContent = 'Discuss the learner’s needs, suitable lesson times and the fee for paid online lessons with Taiwo. The consultation is free.';
    aside.insertAdjacentHTML('beforeend', '<p class="consultation-trust-links"><a href="' + base + 'index.html#about">Meet your tutor</a> · <a href="' + base + 'testimonials.html">Parent feedback</a></p>');
  }

  const openForm = (trigger) => {
    returnFocus = trigger;
    modal.hidden = false;
    document.body.classList.add('consultation-open');
    panel.focus();
    track('consultation_open');
  };

  const closeForm = () => {
    modal.hidden = true;
    document.body.classList.remove('consultation-open');
    returnFocus?.focus();
  };

  document.querySelectorAll('[data-consultation-open], a[href="#consultation"]').forEach((trigger) => {
    trigger.addEventListener('click', (event) => {
      event.preventDefault();
      openForm(trigger);
    });
  });

  modal.querySelectorAll('[data-consultation-close]').forEach((button) => {
    button.addEventListener('click', closeForm);
  });

  form.querySelectorAll('input[name="subjects"]').forEach((input) => {
    input.addEventListener('change', () => {
      subjectError.hidden = Boolean(form.querySelector('input[name="subjects"]:checked'));
    });
  });

  document.addEventListener('keydown', (event) => {
    if (modal.hidden) return;
    if (event.key === 'Escape') closeForm();
    if (event.key === 'Tab') {
      const controls = [...panel.querySelectorAll('a[href], button, input, textarea, select, [tabindex="0"]')].filter((el) => !el.disabled && el.getClientRects().length);
      const first = controls[0], last = controls[controls.length - 1];
      if (event.shiftKey && (document.activeElement === first || document.activeElement === panel)) { event.preventDefault(); last?.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first?.focus(); }
    }
  });

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const subjects = [...form.querySelectorAll('input[name="subjects"]:checked')].map((input) => input.value);
    subjectError.hidden = subjects.length > 0;
    if (!form.reportValidity() || !subjects.length) return;

    const data = new FormData(form);
    const lines = [
      'Hello OTA Learning Studio, I would like to make a tutoring enquiry.',
      '',
      `Name: ${data.get('name')}`,
      `Phone number: ${data.get('phone')}`,
      `Email: ${data.get('email')}`,
      `Country/region: ${data.get('country')}`,
      `Support needed: ${data.get('support')}`,
      `Student year/grade: ${data.get('year')}`,
      `Curriculum/exam: ${data.get('curriculum')}`,
      `Subject(s): ${subjects.join(', ')}`,
      `Learner's needs/goals: ${data.get('message')}`
    ];

    const enquiry = lines.filter((line) => !/^(Phone number|Email|Curriculum\/exam): (null)?$/.test(line)).join('\n');
    const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(enquiry)}`;
    next.querySelector('.consultation-reopen').onclick = () => window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
    next.querySelector('.consultation-email').onclick = () => window.open('mailto:taiwo@otalearningstudio.com?subject=Tutoring%20enquiry&body=' + encodeURIComponent(enquiry), '_blank', 'noopener,noreferrer');
    next.hidden = false;
    track('consultation_handoff');
    window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
    next.scrollIntoView({ block: 'nearest' });
  });
})();
