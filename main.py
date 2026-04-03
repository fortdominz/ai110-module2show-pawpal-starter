from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date


def main():
    # Create owner and pets
    owner = Owner(name="Jordan")
    mochi = Pet(name="Mochi", species="Dog")
    luna = Pet(name="Cat", species="Cat")

    # Create tasks
    t1 = Task(title="Morning Walk", date=date(2026, 4, 3), time="07:00", duration_minutes=30,
              priority="high", frequency="daily")
    t2 = Task(title="Feeding", date=date(2026, 4, 3), time="08:00", duration_minutes=15,
              priority="medium", frequency="daily")
    t3 = Task(title="Medication", date=date(2026, 4, 3), time="08:00", duration_minutes=5,
              priority="urgent", frequency="once")
    t4 = Task(title="Evening Play", date=date(2026, 4, 3), time="18:30", duration_minutes=20,
              priority="low", frequency="weekly")

    # Assign tasks to pets
    mochi.add_task(t1)
    mochi.add_task(t2)
    luna.add_task(t3)
    luna.add_task(t4)

    # Add pets to owner
    owner.add_pet(mochi)
    owner.add_pet(luna)

    # Create scheduler and build schedule
    scheduler = Scheduler()
    schedule = scheduler.generate_schedule(owner)

    # Output schedule and conflicts
    print("Today's Schedule:\n")
    print(scheduler.build_explanation(schedule))

    print("Conflicts:\n")
    conflicts = scheduler.detect_conflicts(schedule)
    if conflicts:
        for c in conflicts:
            print(f"- {c}")
    else:
        print("No conflicts detected.")


if __name__ == '__main__':
    main()
