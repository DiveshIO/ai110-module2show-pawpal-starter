from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete_changes_status():
    task = Task("Morning walk", "8:00 AM", "daily")
    assert task.completed == False
    task.mark_complete()
    assert task.completed == True


def test_add_task_increases_pet_task_count():
    pet = Pet("Buddy", "dog", 3)
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task("Feeding", "7:00 AM", "daily"))
    assert len(pet.get_tasks()) == 1


def test_sorting_returns_tasks_in_chronological_order():
    pet = Pet("Buddy", "dog", 3)
    pet.add_task(Task("Vet visit",     "10:00 AM", "once"))
    pet.add_task(Task("Morning walk",  "7:00 AM",  "daily"))
    pet.add_task(Task("Evening walk",  "6:00 PM",  "daily"))
    pet.add_task(Task("Feeding",       "8:00 AM",  "daily"))

    owner = Owner("Dibi")
    owner.add_pet(pet)
    plan = Scheduler(owner).get_daily_plan()

    times = [t.time for t in plan]
    assert times == ["7:00 AM", "8:00 AM", "10:00 AM", "6:00 PM"]


def test_completing_daily_task_creates_next_day_occurrence():
    pet = Pet("Buddy", "dog", 3)
    walk = Task("Morning walk", "7:00 AM", "daily")
    pet.add_task(walk)

    owner = Owner("Dibi")
    owner.add_pet(pet)
    next_task = Scheduler(owner).complete_task(walk)

    assert next_task is not None
    assert next_task.completed == False
    assert next_task.due_date == date.today() + timedelta(days=1)


def test_conflict_detection_flags_overlapping_tasks():
    pet = Pet("Buddy", "dog", 3)
    pet.add_task(Task("Morning walk", "7:00 AM", "daily", duration_minutes=30))
    pet.add_task(Task("Feeding",      "7:00 AM", "daily", duration_minutes=10))

    owner = Owner("Dibi")
    owner.add_pet(pet)
    warnings = Scheduler(owner).check_conflicts()

    assert len(warnings) == 1
    assert "Morning walk" in warnings[0]
    assert "Feeding" in warnings[0]
