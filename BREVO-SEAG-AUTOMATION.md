# OTA SEAG Parents 2026 - Brevo setup

## Audience and entry point

- Brevo list: `OTA SEAG Parents 2026`
- List ID: `3`
- Trigger: contact is added to the list
- Signup page: `https://otalearningstudio.com/seag-revision-plan.html`
- Thank-you/download page: `https://otalearningstudio.com/seag-revision-plan-download.html`
- PDF: `https://otalearningstudio.com/assets/downloads/OTA-SEAG-2026-8-Week-Revision-Plan.pdf`
- Recommended confirmation: double opt-in
- Sender name: `Taiwo at OTA Learning Studio`
- Reply-to: a working OTA Learning Studio inbox

## Form fields

1. First name - required
2. Email address - required
3. Consent checkbox - required

Consent wording:

> Send me the free SEAG revision plan and helpful SEAG preparation emails from OTA Learning Studio. I understand that I can unsubscribe at any time.

After successful confirmation, redirect to the thank-you/download page above.

## Automation sequence

### Email 1 - immediately after confirmation

**Subject:** Your free SEAG 2026 8-week revision plan

**Preview text:** Your printable weekly plan, trackers and exam-week checklist are ready.

Hello {{ contact.FIRSTNAME | default: "there" }},

Here is your free **SEAG 2026 Final 8-Week Revision Plan for Parents**.

[Download the revision plan](https://otalearningstudio.com/seag-revision-plan-download.html)

Begin with the baseline snapshot. It will help you identify the English, Maths and timing gaps that deserve the most attention.

The aim is not to cram more work into every evening. It is to make each revision session more focused.

Warmly,

Taiwo
OTA Learning Studio

### Email 2 - wait 2 days

**Subject:** The first SEAG question to ask is not “What was the score?”

**Preview text:** Use mistakes to decide what your child should revise next.

Hello {{ contact.FIRSTNAME | default: "there" }},

When your child completes SEAG practice, the total score is only the starting point.

For every incorrect answer, ask which of these happened:

- **Knowledge gap:** the topic was not understood.
- **Technique error:** the knowledge was there, but the question was approached badly.
- **Careless error:** the correct method was known, but accuracy was lost.

Those three labels turn a disappointing paper into a practical teaching plan. The mistake tracker in your guide gives you a simple place to record the pattern.

If the same mistake keeps returning, it is no longer “just careless.” It deserves focused attention.

Warmly,

Taiwo

### Email 3 - wait 3 days

**Subject:** How to use a SEAG practice paper properly

**Preview text:** Completing the paper is only half of the work.

Hello {{ contact.FIRSTNAME | default: "there" }},

A full practice paper is useful when it changes what happens next.

After the paper:

1. Review every incorrect or guessed answer.
2. Group mistakes by topic and error type.
3. Choose the three weaknesses costing the most marks.
4. Re-teach those skills before completing another full paper.

Try to spend at least as much time reviewing the paper as your child spent completing it. Correction is where much of the learning happens.

[Read the full practice-paper guide](https://otalearningstudio.com/blog/seag-practice-papers-2026-how-parents-should-use-them.html)

Warmly,

Taiwo

### Email 4 - wait 3 days

**Subject:** Would a focused SEAG plan help your child?

**Preview text:** Tell me what is currently costing marks and we can discuss the next step.

Hello {{ contact.FIRSTNAME | default: "there" }},

If your child is working hard but the same English, Maths or timing problems keep returning, more random practice may not be the answer.

OTA Learning Studio provides personalised one-to-one online SEAG tutoring. We can use current practice-paper evidence to identify the gaps and build a focused lesson plan around the learner.

You are welcome to book a free parent consultation. There is no obligation to continue.

[Book a free consultation](https://otalearningstudio.com/seag-tutoring.html#consultation)

Warmly,

Taiwo
OTA Learning Studio

## Safeguards

- Send only to contacts who completed the consent checkbox.
- Keep the Brevo unsubscribe link in every email footer.
- Do not collect a child's name, school, scores or sensitive information in the signup form.
- Test the form and every automation email with an address not already in list 3 before publishing.
- Confirm that the sender domain and reply-to mailbox are working before activating the automation.
