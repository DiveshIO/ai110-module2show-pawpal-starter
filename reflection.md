# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The app lets a user enter basic owner + pet info, add/edit tasks (with duration and priority), generate a daily schedule based on constraints and priorities, and display the plan with reasoning.

- Briefly describe your initial UML design.
  - User enters their own info (name, available time per day, preferences)
  - User enters pet info (name, age, type/breed)
  - User adds/edits tasks with at least a duration and priority level
  - A scheduler generates a daily plan respecting constraints
  - The plan is displayed with an explanation of the choices made

- What classes did you include, and what responsibilities did you assign to each?

See [class_diagram.md](class_diagram.md) for the full UML class diagram.

**Class responsibilities:**

- **Owner** — holds user identity and constraints (how much time they have per day, their preferences). Acts as the entry point for the app.
- **Pet** — stores all pet information including special needs (medication, dietary restrictions) that the scheduler must respect.
- **Task** — a single care activity with a type (walk, feed, meds, grooming), duration, priority level (high/medium/low), and status (pending/completed/rescheduled).
- **Scheduler** — the core logic class. Takes the owner's available time and the full task list, sorts by priority, fits tasks within the time budget, and produces an ordered daily plan with reasoning.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
