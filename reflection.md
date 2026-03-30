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
  I have asked ai to modify bit of my methods where it had create some unique variables where it had some stuff missing.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
  Time was the most import where it is most specific about data about schedule where it's required then those other are lower priority.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
  tradeoff is that schedule war abotu the conflict without fixing it, but it keeps the overlapping tasks in the plan.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used claude for debugging, refactoring after I had completed where it had fixed a bit of code and refactored completely, but at start I had used it for brainstorming.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
  I didn't accept AI where it tried to cplmete the whole things, but It felt incorrect where I had to ask it to test it had strugged and rewrote the code.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
  I had tested the create, checking overlap, other test.
  **b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
  I had done a bit of test edges case where including multiple where it had pass those test, but I a bit confidence it works and it worked based on my test.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I feel the creating a flowchat and having ai create an overview of the class was helpful it created a good way of creating this project.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
  I had exam, but if not I could have spend more time thinking deeply.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
  I feel AI is good at taking our thoughts and look at over notes and creating some amazing code, but if our notes are bad then it will be bad.
