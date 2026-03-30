from pawpal_system import Task, Pet, Owner, Scheduler

owner = Owner("Dibi")

# Buddy has two tasks starting at the same time (same-pet conflict)
buddy = Pet("Buddy", "dog", 3)
buddy.add_task(Task("Morning walk", "7:00 AM", "daily",  duration_minutes=30))
buddy.add_task(Task("Feeding",      "7:00 AM", "daily",  duration_minutes=10))  # conflicts with walk

# Ted has a task that overlaps with one of Buddy's (cross-pet conflict)
ted = Pet("Ted", "cat", 5)
ted.add_task(Task("Feeding",   "7:15 AM", "daily",  duration_minutes=10))  # overlaps Buddy's walk
ted.add_task(Task("Vet visit", "10:00 AM", "once",  duration_minutes=60))

owner.add_pet(buddy)
owner.add_pet(ted)

scheduler = Scheduler(owner)
scheduler.print_schedule()

# Also show warnings on their own so they're easy to inspect
print("--- Conflict warnings ---")
warnings = scheduler.check_conflicts()
if warnings:
    for w in warnings:
        print(w)
else:
    print("No conflicts found.")
