from dataclasses import dataclass, field, replace
from datetime import datetime, date, timedelta
from typing import Optional


def _parse_time(time_str: str) -> int:
    """Convert a time string like '8:00 AM' to minutes since midnight for comparison."""
    try:
        return int(datetime.strptime(time_str, "%I:%M %p").strftime("%H%M"))
    except ValueError:
        return 0


@dataclass
class Task:
    description: str
    time: str                                           # e.g. "8:00 AM"
    frequency: str                                      # "daily", "weekly", or "once"
    duration_minutes: int = 30
    completed: bool = False
    due_date: date = field(default_factory=date.today)  # which day this instance is for

    def mark_complete(self) -> None:
        self.completed = True
        if self.frequency == "daily":
            self.due_date = date.today() + timedelta(days=1)
        elif self.frequency == "weekly":
            self.due_date = date.today() + timedelta(weeks=1)

    def is_recurring(self) -> bool:
        return self.frequency in ("daily", "weekly")

    def next_occurrence(self) -> "Task":
        """Return a fresh incomplete copy using the due_date already set by mark_complete."""
        return replace(self, completed=False)


@dataclass
class Pet:
    name: str
    type: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_tasks(self) -> list[Task]:
        return self.tasks


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    # --- Sorting ---

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Sort a list of Task objects by their time attribute in HH:MM format."""
        return sorted(tasks, key=lambda t: datetime.strptime(t.time, "%I:%M %p"))

    def get_daily_plan(self) -> list[Task]:
        """All tasks sorted by start time."""
        return self.sort_by_time(self.owner.get_all_tasks())

    # --- Filtering ---

    def filter_by_pet(self, pet_name: str) -> list[Task]:
        """Tasks belonging to a specific pet."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                return sorted(pet.get_tasks(), key=lambda t: _parse_time(t.time))
        return []

    def filter_by_status(self, completed: bool) -> list[Task]:
        """Tasks matching the given completion status."""
        return [t for t in self.get_daily_plan() if t.completed == completed]

    # --- Completing tasks ---

    def complete_task(self, task: Task) -> Optional[Task]:
        """Mark a task complete. If it recurs, add the next occurrence to the same pet."""
        task.mark_complete()
        if not task.is_recurring():
            return None
        for pet in self.owner.pets:
            if task in pet.tasks:
                next_task = task.next_occurrence()
                pet.add_task(next_task)
                return next_task
        return None

    # --- Recurring tasks ---

    def get_recurring_tasks(self) -> list[Task]:
        """Tasks marked as daily or weekly that repeat automatically."""
        return [t for t in self.get_daily_plan() if t.is_recurring()]

    # --- Conflict detection ---

    def get_conflicts(self) -> list[tuple[Task, Task]]:
        """Return pairs of tasks whose time windows overlap."""
        plan = self.get_daily_plan()
        conflicts = []
        for i in range(len(plan)):
            for j in range(i + 1, len(plan)):
                a, b = plan[i], plan[j]
                a_start = _parse_time(a.time)
                a_end = a_start + a.duration_minutes
                b_start = _parse_time(b.time)
                b_end = b_start + b.duration_minutes
                if a_start < b_end and b_start < a_end:
                    conflicts.append((a, b))
        return conflicts

    def check_conflicts(self) -> list[str]:
        """Return a list of human-readable warning messages for any overlapping tasks."""
        warnings = []
        for a, b in self.get_conflicts():
            msg = (
                f"WARNING: '{a.description}' ({a.time}, {a.duration_minutes} min) "
                f"overlaps with '{b.description}' ({b.time}, {b.duration_minutes} min)."
            )
            warnings.append(msg)
        return warnings

    # --- Display ---

    def print_schedule(self) -> None:
        print(f"\n📅 Today's Schedule for {self.owner.name}")
        print("-" * 40)
        for task in self.get_daily_plan():
            status = "✅" if task.completed else "○"
            recur = f" [{task.frequency}]" if task.is_recurring() else ""
            print(f"  {status} {task.time}  {task.description}  ({task.duration_minutes} min){recur}")

        warnings = self.check_conflicts()
        if warnings:
            print()
            for msg in warnings:
                print(f"⚠️  {msg}")
        print()
