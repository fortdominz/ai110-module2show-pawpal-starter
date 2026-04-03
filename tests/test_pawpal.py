from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date


def test_task_completion():
    task = Task(title="Checkup", date=date(2026, 4, 3), time="09:00", duration_minutes=15,
                priority="high", frequency="once")
    result = task.mark_complete()
    assert task.completed is True
    assert result is None


def test_pet_add_task():
    pet = Pet(name="Mochi", species="Dog")
    task = Task(title="Feeding", date=date(2026, 4, 3), time="08:00", duration_minutes=10,
                priority="medium", frequency="daily")
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1


def test_scheduler_sort_by_time():
    scheduler = Scheduler()
    task1 = Task(title="Walk", date=date(2026, 4, 3), time="14:30", duration_minutes=30,
                 priority="medium", frequency="once")
    task2 = Task(title="Feeding", date=date(2026, 4, 3), time="08:00", duration_minutes=10,
                 priority="high", frequency="once")
    task3 = Task(title="Medication", date=date(2026, 4, 3), time="12:00", duration_minutes=5,
                 priority="low", frequency="once")
    tasks = [(task1, "Mochi"), (task2, "Mochi"), (task3, "Mochi")]
    sorted_tasks = scheduler.sort_by_time(tasks)
    assert [task.time for task, _ in sorted_tasks] == ["08:00", "12:00", "14:30"]


def test_scheduler_detect_conflicts():
    scheduler = Scheduler()
    task1 = Task(title="Vet", date=date(2026, 4, 3), time="10:00", duration_minutes=30,
                 priority="high", frequency="once")
    task2 = Task(title="Grooming", date=date(2026, 4, 3), time="10:00", duration_minutes=60,
                 priority="medium", frequency="once")
    conflicts = scheduler.detect_conflicts([task1, task2])
    assert len(conflicts) == 1
    assert "Conflict" in conflicts[0]
    assert "Vet" in conflicts[0]
    assert "Grooming" in conflicts[0]


def test_pet_with_no_tasks_returns_empty_list():
    pet = Pet(name="Luna", species="Cat")
    assert pet.get_tasks() == []


def test_recurring_task_daily():
    task = Task(title="Feeding", date=date(2026, 4, 3), time="08:00", duration_minutes=10,
                priority="medium", frequency="daily")
    new_task = task.mark_complete()
    assert task.completed is True
    assert new_task is not None
    assert new_task.date == date(2026, 4, 4)
    assert new_task.completed is False
    assert new_task.title == task.title
    assert new_task.time == task.time
    assert new_task.duration_minutes == task.duration_minutes
    assert new_task.priority == task.priority
    assert new_task.frequency == task.frequency


def test_recurring_task_weekly():
    task = Task(title="Grooming", date=date(2026, 4, 3), time="10:00", duration_minutes=30,
                priority="low", frequency="weekly")
    new_task = task.mark_complete()
    assert task.completed is True
    assert new_task is not None
    assert new_task.date == date(2026, 4, 10)
    assert new_task.completed is False


def test_scheduler_detects_multiple_conflicts_for_same_slot():
    scheduler = Scheduler()
    task1 = Task(title="Vet", date=date(2026, 4, 3), time="10:00", duration_minutes=30,
                 priority="high", frequency="once")
    task2 = Task(title="Grooming", date=date(2026, 4, 3), time="10:00", duration_minutes=60,
                 priority="medium", frequency="once")
    task3 = Task(title="Training", date=date(2026, 4, 3), time="10:00", duration_minutes=45,
                 priority="low", frequency="once")
    conflicts = scheduler.detect_conflicts([task1, task2, task3])
    assert len(conflicts) == 3
    assert all("Conflict" in conflict for conflict in conflicts)


def test_generate_schedule_returns_empty_for_owner_with_no_pets():
    scheduler = Scheduler()
    owner = Owner(name="Alex")
    schedule = scheduler.generate_schedule(owner)
    assert schedule == []


def test_once_frequency_task_mark_complete_returns_none():
    task = Task(title="Vaccination", date=date(2026, 4, 3), time="11:00", duration_minutes=20,
                priority="high", frequency="once")
    result = task.mark_complete()
    assert task.completed is True
    assert result is None


def test_generate_schedule_handles_unknown_priority_without_crash():
    scheduler = Scheduler()
    owner = Owner(name="Jordan")
    task = Task(title="Playtime", date=date(2026, 4, 3), time="15:00", duration_minutes=15,
                priority="mystery", frequency="once")
    pet = Pet(name="Pip", species="Rabbit")
    pet.add_task(task)
    owner.add_pet(pet)
    schedule = scheduler.generate_schedule(owner)
    assert schedule == [task]


def test_filter_tasks_returns_empty_when_no_match():
    scheduler = Scheduler()
    task = Task(title="Feeding", date=date(2026, 4, 3), time="08:00", duration_minutes=10,
                priority="medium", frequency="daily")
    tasks = [(task, "Mochi")]
    filtered = scheduler.filter_tasks(tasks, {'pet_name': 'Nonexistent'})
    assert filtered == []
