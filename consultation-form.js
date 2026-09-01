(() => {
  const modal = document.querySelector('.consultation-modal');
  const panel = modal?.querySelector('.consultation-panel');
  const form = modal?.querySelector('[data-consultation-form]');
  const subjectError = modal?.querySelector('[data-subject-error]');
  const whatsappNumber = '2348079675840';
  let returnFocus = null;

  if (!modal || !panel || !form) return;

  const openForm = (trigger) => {
    returnFocus = trigger;
    modal.hidden = false;
    document.body.classList.add('consultation-open');
    panel.focus();
  };

  const closeForm = () => {
    modal.hidden = true;
    document.body.classList.remove('consultation-open');
    returnFocus?.focus();
  };

  document.querySelectorAll('[data-consultation-open]').forEach((trigger) => {
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
    if (event.key === 'Escape' && !modal.hidden) closeForm();
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

    const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(lines.join('\n'))}`;
    window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
  });
})();
