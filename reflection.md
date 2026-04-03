# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

My initial UML design consists of four classes: Task, Pet, Owner, and Scheduler.


- What classes did you include, and what responsibilities did you assign to each?

Task is responsible for representing a single care activity. It stores the title, date, time, duration, priority, frequency, and completion status of an activity. Its only method is mark_complete() which flips its status to done.

Pet is responsible for representing an animal belonging to the owner. It stores the pet's name, species, and a list of tasks assigned to it. It can add a new task via add_task() and return its task list via get_tasks().

Owner is responsible for representing the user of the app. It stores the owner's name and a list of their pets. It can add a new pet via add_pet() and retrieve all tasks across all pets via get_all_tasks().

Scheduler is the brain of the system and holds no data of its own. It is responsible for all actions performed on the schedule: adding, editing, removing, and completing tasks, as well as sorting tasks by time, filtering them, detecting conflicts, generating the daily plan, and explaining the reasoning behind it.



**b. Design changes**

- Did your design change during implementation?

Yes


- If yes, describe at least one change and why you made it.

After asking Copilot to review the skeleton, I accepted the suggestion to add a pet parameter to Scheduler.add_task() and Scheduler.remove_task() since without it those methods wouldn't know which pet to assign the task to. I also noted that filter_tasks() needed a clearer criteria parameter. I rejected suggestions like adding id fields, timestamps, and persistence as they are beyond the scope of this project.





---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?

The scheduler considers priority (urgent, high, medium, low) and time (HH:MM format).


- How did you decide which constraints mattered most?

I decided priority matters most because a medication task should always appear before a play session regardless of what time it's scheduled.



**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

The scheduler only checks for exact time matches when detecting conflicts, for example, two tasks both at 07:00. It does not account for overlapping durations, meaning a 30-minute task at 07:00 and a task at 07:15 would not be flagged as a conflict even though they overlap. 


- Why is that tradeoff reasonable for this scenario?

This tradeoff is reasonable for this project because exact time matching is simpler to implement and still catches the most obvious scheduling mistakes.





---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used Copilot Chat to generate class skeletons from my UML design, flesh out method logic, generate the demo script, and create test cases.


- What kinds of prompts or questions were most helpful?

The most helpful prompts were ones that gave Copilot specific context about what each method should do rather than vague requests.



**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.

When Copilot reviewed my class skeletons, it suggested adding id fields to Task, Pet, and Owner, timestamps like created_at and updated_at, and a tasks_cache on the Scheduler for performance. I rejected these suggestions because they added unnecessary complexity for a project of this scope.


- How did you evaluate or verify what the AI suggested?

I evaluated them by asking whether each suggestion was required for the core scheduling features... if it wasn't, I left it out. I also kept urgent as a fourth priority level that Copilot added to generate_schedule() because it made the scheduler more realistic for medication or emergency tasks.





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
