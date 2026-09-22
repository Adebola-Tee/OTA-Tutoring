from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle
)

OUT = "output/pdf/OTA-SEAG-2026-8-Week-Revision-Plan.pdf"
LOGO = "assets/ota-learning-studio-logo-2026.png"

NAVY = colors.HexColor("#14213F")
INK = colors.HexColor("#26334F")
MUTED = colors.HexColor("#617089")
LAV = colors.HexColor("#766FD4")
LAV_SOFT = colors.HexColor("#E9E7FA")
MINT = colors.HexColor("#BCEBDC")
MINT_DARK = colors.HexColor("#3D8D76")
PEACH = colors.HexColor("#F2B69D")
CREAM = colors.HexColor("#FAF9F6")
LINE = colors.HexColor("#DFE3EB")
WHITE = colors.white

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Kicker", fontName="Helvetica-Bold", fontSize=8.5, leading=11,
                          textColor=LAV, spaceAfter=7, uppercase=True, letterSpacing=1.2))
styles.add(ParagraphStyle(name="TitleBig", fontName="Helvetica-Bold", fontSize=29, leading=33,
                          textColor=NAVY, spaceAfter=13))
styles.add(ParagraphStyle(name="Titlex", fontName="Helvetica-Bold", fontSize=21, leading=25,
                          textColor=NAVY, spaceAfter=9))
styles.add(ParagraphStyle(name="H2x", fontName="Helvetica-Bold", fontSize=14, leading=18,
                          textColor=NAVY, spaceBefore=5, spaceAfter=6))
styles.add(ParagraphStyle(name="H3x", fontName="Helvetica-Bold", fontSize=10.5, leading=14,
                          textColor=NAVY, spaceAfter=3))
styles.add(ParagraphStyle(name="Bodyx", fontName="Helvetica", fontSize=9.3, leading=14,
                          textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name="Small", fontName="Helvetica", fontSize=7.7, leading=11,
                          textColor=MUTED))
styles.add(ParagraphStyle(name="Box", fontName="Helvetica", fontSize=8.6, leading=12.5,
                          textColor=INK))
styles.add(ParagraphStyle(name="White", fontName="Helvetica", fontSize=9, leading=13,
                          textColor=WHITE))
styles.add(ParagraphStyle(name="WhiteTitle", fontName="Helvetica-Bold", fontSize=18, leading=22,
                          textColor=WHITE, spaceAfter=6))
styles.add(ParagraphStyle(name="CenterSmall", parent=styles["Small"], alignment=TA_CENTER))


def P(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def checkbox(text):
    return P("&#9744;&nbsp;&nbsp;" + text, "Box")


def bullet(text):
    return P("<font color='#766FD4'>&#8226;</font>&nbsp;&nbsp;" + text, "Box")


def card(title, body, bg=WHITE, stripe=MINT):
    t = Table([[P(title, "H3x")], [P(body, "Box")]], colWidths=[79*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("LINEBEFORE", (0, 0), (0, -1), 4, stripe),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def two_cards(left, right):
    t = Table([[left, right]], colWidths=[82*mm, 82*mm], hAlign="LEFT")
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (0, -1), 3*mm), ("LEFTPADDING", (1, 0), (1, -1), 3*mm)]))
    return t


def header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.line(18*mm, 283*mm, 192*mm, 283*mm)
        canvas.setFont("Helvetica-Bold", 7.5)
        canvas.setFillColor(NAVY)
        canvas.drawString(18*mm, 287*mm, "OTA LEARNING STUDIO")
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(192*mm, 287*mm, "SEAG 2026 | 8-Week Revision Plan")
        canvas.line(18*mm, 14*mm, 192*mm, 14*mm)
        canvas.drawString(18*mm, 9*mm, "otalearningstudio.com")
        canvas.drawRightString(192*mm, 9*mm, str(doc.page))
    canvas.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                      topMargin=18*mm, bottomMargin=18*mm, title="SEAG 2026 Final 8-Week Revision Plan for Parents",
                      author="Taiwo Oloyede, OTA Learning Studio")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates([PageTemplate(id="all", frames=frame, onPage=header_footer)])

story = []

# Cover
story += [Spacer(1, 8*mm), Image(LOGO, width=40*mm, height=40*mm), Spacer(1, 5*mm),
          P("FREE PARENT GUIDE", "Kicker"),
          P("SEAG 2026 Final<br/>8-Week Revision Plan", "TitleBig"),
          P("A calm, practical week-by-week plan to strengthen English, Maths, timing and confidence before test day.", "Bodyx"),
          Spacer(1, 4*mm)]
cover = Table([
    [P("PAPER 1", "Kicker"), P("PAPER 2", "Kicker")],
    [P("Saturday<br/><b>14 November 2026</b>", "H2x"), P("Saturday<br/><b>21 November 2026</b>", "H2x")],
], colWidths=[82*mm, 82*mm])
cover.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LAV_SOFT), ("BACKGROUND", (1, 0), (1, -1), colors.HexColor("#DFF7F0")),
    ("BOX", (0, 0), (-1, -1), .7, LINE), ("INNERGRID", (0, 0), (-1, -1), .7, WHITE),
    ("LEFTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 10),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
]))
story += [cover, Spacer(1, 8*mm),
          P("Prepared by <b>Taiwo Oloyede</b><br/>OTA Learning Studio | Guided learning. Lasting progress.", "Bodyx"),
          Spacer(1, 8*mm)]
note = Table([[P("Use this guide as a flexible structure, not a pressure schedule. Adjust the workload to your child's needs, school commitments and wellbeing.", "White")]], colWidths=[164*mm])
note.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), NAVY), ("LEFTPADDING", (0,0), (-1,-1), 14),
                           ("RIGHTPADDING", (0,0), (-1,-1), 14), ("TOPPADDING", (0,0), (-1,-1), 12),
                           ("BOTTOMPADDING", (0,0), (-1,-1), 12)]))
story += [note, PageBreak()]

# Start here
story += [P("START HERE", "Kicker"), P("A strong eight weeks begins with clarity.", "Titlex"),
          P("The goal is not to make your child complete the greatest number of questions. It is to find the patterns behind lost marks, teach the missing skill and practise until the better method becomes familiar."),
          Spacer(1, 2*mm),
          two_cards(card("1. Diagnose", "Use a mixed English and Maths task. Record the reason for each error, not only the score.", LAV_SOFT, LAV),
                    card("2. Prioritise", "Choose the three weaknesses costing the most marks. These become the main revision targets.", colors.HexColor("#EAF8F4"), MINT_DARK)),
          Spacer(1, 4*mm),
          two_cards(card("3. Practise", "Use short, focused sessions. Include correction time so mistakes become useful evidence.", colors.HexColor("#FFF4EE"), PEACH),
                    card("4. Review", "At the end of each week, note what improved, what remains difficult and what to change next.", CREAM, NAVY)),
          Spacer(1, 7*mm), P("Your baseline snapshot", "H2x"),
          P("Complete this before Week 1. It will make the rest of the plan much more focused."),
          Table([
              [P("Area", "H3x"), P("Current confidence (1-5)", "H3x"), P("Evidence / notes", "H3x")],
              [P("English comprehension", "Box"), P("1  2  3  4  5", "Box"), P("", "Box")],
              [P("Vocabulary, grammar and spelling", "Box"), P("1  2  3  4  5", "Box"), P("", "Box")],
              [P("Number, fractions and percentages", "Box"), P("1  2  3  4  5", "Box"), P("", "Box")],
              [P("Problem-solving and reasoning", "Box"), P("1  2  3  4  5", "Box"), P("", "Box")],
              [P("Timing and answer-sheet accuracy", "Box"), P("1  2  3  4  5", "Box"), P("", "Box")],
          ], colWidths=[58*mm, 48*mm, 58*mm], rowHeights=[11*mm, 15*mm, 15*mm, 15*mm, 15*mm, 15*mm],
             style=TableStyle([("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), WHITE),
                               ("GRID", (0,0), (-1,-1), .6, LINE), ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                               ("LEFTPADDING", (0,0), (-1,-1), 8)])), PageBreak()]

weeks = [
    ("WEEK 1", "Find the gaps", "Use a mixed diagnostic task and build a mistake list.",
     ["English: comprehension, inference, vocabulary, grammar, spelling and punctuation.",
      "Maths: number, fractions, decimals, percentages, measures, shape, money, data and reasoning."],
     "Write why each answer was wrong: knowledge gap, technique error or careless error."),
    ("WEEK 2", "Strengthen core Maths", "Prioritise accurate methods before speed.",
     ["Re-teach the two weakest number topics.", "Add short word problems and ask: What do I know? What must I find? Which operation fits?"],
     "Aim for 3 focused Maths sessions, each followed by correction."),
    ("WEEK 3", "Build stronger English", "Slow the reading down before trying to speed it up.",
     ["Practise retrieval, inference, vocabulary in context and evidence selection.", "Require a return to the passage: answers should come from the text, not memory."],
     "Keep a vocabulary bank with meaning, synonym and one original sentence."),
    ("WEEK 4", "Mix English and Maths", "Train the mental switch between subjects.",
     ["Try 20 minutes English + 20 minutes Maths + 10 minutes correcting.", "Circle recurring errors. A repeated 'careless mistake' is now a revision target."],
     "Complete one mixed session under gentle time pressure."),
]
story += [P("WEEKS 1-4", "Kicker"), P("Repair the foundations first.", "Titlex"),
          P("Keep sessions short enough for your child to stay attentive. A useful session ends with an understood correction, not exhaustion."), Spacer(1, 2*mm)]
for label, title, aim, tasks, parent in weeks:
    data = [[P(label, "Kicker"), P(title, "H2x")], [P("Focus", "H3x"), P(aim, "Box")],
            [P("Actions", "H3x"), Table([[bullet(x)] for x in tasks], colWidths=[126*mm], style=TableStyle([("LEFTPADDING",(0,0),(-1,-1),0)]))],
            [P("Parent check", "H3x"), P(parent, "Box")]]
    t = Table(data, colWidths=[30*mm, 134*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (0,-1), CREAM), ("BACKGROUND", (0,0), (-1,0), LAV_SOFT),
                           ("GRID", (0,0), (-1,-1), .5, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"),
                           ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
                           ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6)]))
    story += [KeepTogether(t), Spacer(1, 4*mm)]
story += [PageBreak()]

weeks2 = [
    ("WEEK 5", "Introduce serious timed practice", "Improve decisions under time pressure, not frantic rushing.",
     ["Practise leaving a difficult question and returning later.", "Reserve checking time and rehearse accurate answer-sheet transfer."],
     "Notice whether time is lost through reading, method choice, calculations or hesitation."),
    ("WEEK 6", "Complete a full practice paper", "Recreate test conditions and analyse the result properly.",
     ["No help, interruptions or stopped clock during the paper.", "Review every error and label it: knowledge, technique or careless."],
     "Spend at least as much time reviewing as completing the paper."),
    ("WEEK 7", "Target the three biggest weaknesses", "Do not restart the whole curriculum.",
     ["Use evidence from Weeks 1-6 to choose three priorities.", "Keep some mixed practice while concentrating most time on those weaknesses."],
     "Check that scores are improving because errors are changing, not because questions are familiar."),
    ("WEEK 8", "Sharpen technique and protect confidence", "Reduce volume; keep skills active and routines calm.",
     ["Use short mixed tasks, light review and early nights.", "Rehearse moving on, checking calmly and recovering after a difficult question."],
     "Do not suddenly double revision hours. Confidence and rest matter now."),
]
story += [P("WEEKS 5-8", "Kicker"), P("Move from practice to performance.", "Titlex"),
          P("The final month is about applying known skills accurately under realistic conditions, then using the evidence to make precise adjustments."), Spacer(1, 2*mm)]
for label, title, aim, tasks, parent in weeks2:
    data = [[P(label, "Kicker"), P(title, "H2x")], [P("Focus", "H3x"), P(aim, "Box")],
            [P("Actions", "H3x"), Table([[bullet(x)] for x in tasks], colWidths=[126*mm], style=TableStyle([("LEFTPADDING",(0,0),(-1,-1),0)]))],
            [P("Parent check", "H3x"), P(parent, "Box")]]
    t = Table(data, colWidths=[30*mm, 134*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (0,-1), CREAM), ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#DFF7F0")),
                           ("GRID", (0,0), (-1,-1), .5, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"),
                           ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
                           ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6)]))
    story += [KeepTogether(t), Spacer(1, 4*mm)]
story += [PageBreak()]

# Weekly timetable
story += [P("YOUR WEEKLY ROUTINE", "Kicker"), P("A repeatable plan beats random revision.", "Titlex"),
          P("Choose realistic session lengths. For many pupils, 35-50 focused minutes is more productive than a long unfocused evening."),
          Spacer(1, 3*mm)]
schedule = [
    [P("Day", "H3x"), P("Suggested focus", "H3x"), P("Completed", "H3x"), P("Notes", "H3x")],
    [P("Monday", "Box"), P("Weak Maths topic", "Box"), P("&#9744;", "Box"), P("", "Box")],
    [P("Tuesday", "Box"), P("English comprehension + vocabulary", "Box"), P("&#9744;", "Box"), P("", "Box")],
    [P("Wednesday", "Box"), P("Mixed English and Maths", "Box"), P("&#9744;", "Box"), P("", "Box")],
    [P("Thursday", "Box"), P("Maths problem-solving", "Box"), P("&#9744;", "Box"), P("", "Box")],
    [P("Friday", "Box"), P("Light review or rest", "Box"), P("&#9744;", "Box"), P("", "Box")],
    [P("Weekend", "Box"), P("Timed practice + corrections", "Box"), P("&#9744;", "Box"), P("", "Box")],
]
t = Table(schedule, colWidths=[27*mm, 60*mm, 24*mm, 53*mm], rowHeights=[12*mm]+[21*mm]*6)
t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), WHITE),
                       ("GRID", (0,0), (-1,-1), .6, LINE), ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                       ("LEFTPADDING", (0,0), (-1,-1), 8)]))
story += [t, Spacer(1, 7*mm),
          P("The 10-minute correction rule", "H2x"),
          P("At the end of every session, spend at least 10 minutes correcting. Ask your child to explain the correct method aloud. If they cannot explain it simply, the correction is not complete."),
          two_cards(card("Keep", "One method or habit that worked well this week.", colors.HexColor("#EAF8F4"), MINT_DARK),
                    card("Change", "One recurring error to address next week.", colors.HexColor("#FFF4EE"), PEACH)), PageBreak()]

# Mistake tracker
story += [P("MISTAKE TRACKER", "Kicker"), P("Turn every error into a next step.", "Titlex"),
          P("Use one row per useful mistake. The final column matters most: it records what your child will do differently next time."), Spacer(1, 3*mm)]
tracker = [[P("Date / task", "H3x"), P("Question / topic", "H3x"), P("Error type", "H3x"), P("Why it happened", "H3x"), P("My better action", "H3x")]]
for _ in range(8):
    tracker.append([P("", "Box"), P("", "Box"), P("Knowledge /<br/>Technique /<br/>Careless", "Small"), P("", "Box"), P("", "Box")])
t = Table(tracker, colWidths=[25*mm, 35*mm, 27*mm, 38*mm, 39*mm], rowHeights=[13*mm]+[23*mm]*8)
t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), WHITE),
                       ("GRID", (0,0), (-1,-1), .6, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"),
                       ("LEFTPADDING", (0,0), (-1,-1), 6), ("TOPPADDING", (0,0), (-1,-1), 6)]))
story += [t, PageBreak()]

# Progress dashboard
story += [P("WEEKLY PROGRESS", "Kicker"), P("Look for movement, not perfection.", "Titlex"),
          P("Complete one row every weekend. A small, steady improvement is evidence that the plan is working."), Spacer(1, 3*mm)]
dash = [[P("Week", "H3x"), P("English accuracy", "H3x"), P("Maths accuracy", "H3x"), P("Timing", "H3x"), P("Top improvement", "H3x"), P("Next priority", "H3x")]]
for n in range(1, 9):
    dash.append([P(str(n), "H3x"), P("_____ %", "Box"), P("_____ %", "Box"), P("On time / over", "Small"), P("", "Box"), P("", "Box")])
t = Table(dash, colWidths=[13*mm, 29*mm, 29*mm, 27*mm, 33*mm, 33*mm], rowHeights=[12*mm]+[17*mm]*8)
t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), WHITE),
                       ("BACKGROUND", (0,1), (0,-1), LAV_SOFT), ("GRID", (0,0), (-1,-1), .6, LINE),
                       ("VALIGN", (0,0), (-1,-1), "MIDDLE"), ("ALIGN", (0,1), (0,-1), "CENTER"),
                       ("LEFTPADDING", (0,0), (-1,-1), 6)]))
story += [t, Spacer(1, 7*mm),
          P("Three questions for the weekly review", "H2x"),
          two_cards(card("What improved?", "Name a specific skill, habit or question type.", LAV_SOFT, LAV),
                    card("What repeated?", "Identify the error pattern that still needs teaching.", colors.HexColor("#FFF4EE"), PEACH)),
          Spacer(1, 3*mm), card("What changes next week?", "Choose one practical adjustment: a topic, a method, a shorter session, more correction or a timed task.", colors.HexColor("#EAF8F4"), MINT_DARK), PageBreak()]

# Exam week
story += [P("EXAM-WEEK CHECKLIST", "Kicker"), P("Protect calm, routine and confidence.", "Titlex"),
          P("The final days are not the time to prove how much work has been done. They are the time to help your child arrive rested, organised and ready to think clearly."),
          Spacer(1, 3*mm)]
left = Table([[checkbox(x)] for x in [
    "Confirm the assessment centre and travel plan.", "Check arrival instructions and required items.",
    "Use short review sessions only.", "Finish full-paper practice early enough to recover.",
    "Prepare clothing and materials the night before."
]], colWidths=[78*mm], style=TableStyle([("BACKGROUND",(0,0),(-1,-1),CREAM), ("BOX",(0,0),(-1,-1),.6,LINE),
                                         ("INNERGRID",(0,0),(-1,-1),.4,LINE), ("LEFTPADDING",(0,0),(-1,-1),9),
                                         ("TOPPADDING",(0,0),(-1,-1),9), ("BOTTOMPADDING",(0,0),(-1,-1),9)]))
right = Table([[checkbox(x)] for x in [
    "Keep bedtime and breakfast familiar.", "Avoid discussing scores immediately before the paper.",
    "Remind your child to move on from a stubborn question.", "After Paper 1, praise effort and reset for Paper 2.",
    "Keep adult anxiety away from the child."
]], colWidths=[78*mm], style=TableStyle([("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#EAF8F4")), ("BOX",(0,0),(-1,-1),.6,LINE),
                                         ("INNERGRID",(0,0),(-1,-1),.4,LINE), ("LEFTPADDING",(0,0),(-1,-1),9),
                                         ("TOPPADDING",(0,0),(-1,-1),9), ("BOTTOMPADDING",(0,0),(-1,-1),9)]))
story += [two_cards(left, right), Spacer(1, 8*mm),
          P("A useful sentence to rehearse", "H2x"),
          Table([[P("If one question feels difficult, I can stay calm, make a sensible choice and move on. One question does not decide my whole paper.", "WhiteTitle")]], colWidths=[164*mm],
                style=TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY), ("LEFTPADDING",(0,0),(-1,-1),14),
                                  ("RIGHTPADDING",(0,0),(-1,-1),14), ("TOPPADDING",(0,0),(-1,-1),15),
                                  ("BOTTOMPADDING",(0,0),(-1,-1),15)])),
          Spacer(1, 8*mm), P("Parent note", "H2x"),
          P("Your child does not need to feel perfectly confident. They need a familiar routine, practical strategies and the reassurance that they can recover when something feels hard."), PageBreak()]

# CTA and sources
story += [P("WHEN YOU WANT A CLEARER PLAN", "Kicker"), P("Focused support for your child's actual gaps.", "Titlex"),
          P("OTA Learning Studio provides personalised online SEAG English and Maths tutoring for P7 pupils. Lessons can focus on comprehension, vocabulary, grammar, number skills, reasoning, timed practice and exam technique."),
          Spacer(1, 3*mm),
          two_cards(card("Free parent consultation", "Tell us what is currently difficult. We will discuss the learner's needs and the most useful next step.", LAV_SOFT, LAV),
                    card("One-to-one online lessons", "Focused teaching, practice and feedback built around one learner rather than a generic worksheet sequence.", colors.HexColor("#EAF8F4"), MINT_DARK)),
          Spacer(1, 7*mm),
          Table([[P("BOOK A FREE CONSULTATION", "Kicker")], [P("otalearningstudio.com/seag-tutoring.html", "WhiteTitle")],
                 [P("Or email taiwo@otalearningstudio.com", "White")]], colWidths=[164*mm],
                style=TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY), ("LEFTPADDING",(0,0),(-1,-1),14),
                                  ("RIGHTPADDING",(0,0),(-1,-1),14), ("TOPPADDING",(0,0),(-1,-1),9),
                                  ("BOTTOMPADDING",(0,0),(-1,-1),9)])),
          Spacer(1, 9*mm), P("Important information", "H2x"),
          P("This independent revision guide is provided by OTA Learning Studio and is not produced, endorsed or approved by SEAG or GL Assessment. Assessment details can change. Parents should confirm current dates, format, registration and arrangements using official SEAG guidance."),
          Spacer(1, 4*mm), P("Official sources checked 18 September 2026", "H2x"),
          bullet("SEAG Guidance: seagni.co.uk/guidance"),
          bullet("SEAG FAQs (2026 dates, eligibility, official practice materials and outcomes): seagni.co.uk/guidance/faqs"),
          Spacer(1, 8*mm), P("© 2026 OTA Learning Studio. For personal family use only. Do not resell or redistribute.", "Small")]

doc.build(story)
print(OUT)
