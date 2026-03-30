from pawpal_system import Task, Pet


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
