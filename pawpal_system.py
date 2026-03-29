class Pet:
    def __init__(self, name: str, age: int, type: str, breed: str = ""):
        self.name = name
        self.age = age
        self.type = type
        self.breed = breed
        self.special_needs: list[str] = []

    def update_info(self, name: str, age: int, type: str) -> None:
        pass

    def get_details(self) -> dict:
        pass

    def add_special_need(self, need: str) -> None:
        pass


class Task:
    def __init__(self, task_id: str, type: str, pet_name: str, duration_minutes: int, priority: str):
        self.task_id = task_id
        self.type = type
        self.pet_name = pet_name
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.status = "pending"
        self.scheduled_time: str = ""
        self.notes: str = ""

    def mark_completed(self) -> None:
        pass

    def reschedule(self, new_time: str) -> None:
        pass

    def get_details(self) -> dict:
        pass

    def is_overdue(self) -> bool:
        pass


class Owner:
    def __init__(self, name: str, email: str, available_minutes_per_day: int, pet: Pet):
        self.name = name
        self.email = email
        self.available_minutes_per_day = available_minutes_per_day
        self.pet = pet
        self.preferences: list[str] = []

    def get_info(self) -> dict:
        pass

    def set_available_time(self, minutes: int) -> None:
        pass

    def add_preference(self, pref: str) -> None:
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.tasks: list[Task] = []
        self.total_available_minutes = owner.available_minutes_per_day

    def generate_schedule(self) -> list[Task]:
        pass

    def add_task(self, task: Task) -> None:
        pass

    def edit_task(self, task_id: str, updates: dict) -> None:
        pass

    def remove_task(self, task_id: str) -> None:
        pass

    def get_daily_plan(self) -> list[Task]:
        pass

    def explain_plan(self) -> str:
        pass

    def get_unscheduled_tasks(self) -> list[Task]:
        pass
