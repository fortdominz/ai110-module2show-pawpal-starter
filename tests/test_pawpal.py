from pawpal_system import Task, Pet
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