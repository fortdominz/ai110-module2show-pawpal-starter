from pawpal_system import Task, Pet


def test_task_completion():
    task = Task(title="Checkup", date="2026-04-03", time="09:00", duration_minutes=15,
                priority="high", frequency="once")
    task.mark_complete()
    assert task.completed is True


def test_pet_add_task():
    pet = Pet(name="Mochi", species="Dog")
    task = Task(title="Feeding", date="2026-04-03", time="08:00", duration_minutes=10,
                priority="medium", frequency="daily")
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1