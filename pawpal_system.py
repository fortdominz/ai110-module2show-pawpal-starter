from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    """Represents a pet care task."""
    title: str
    date: str
    time: str
    duration_minutes: int
    priority: str
    frequency: str
    completed: bool = False
    
    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet owned by an owner."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)
    
    def add_task(self, task: Task):
        """Add a task to the pet's task list."""
        self.tasks.append(task)
    
    def get_tasks(self) -> List[Task]:
        """Retrieve all tasks for the pet."""
        return self.tasks


@dataclass
class Owner:
    """Represents a pet owner."""
    name: str
    pets: List[Pet] = field(default_factory=list)
    
    def add_pet(self, pet: Pet):
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)
    
    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Orchestrates scheduling and management of pet care tasks."""
    
    def generate_schedule(self, owner: Owner) -> List[Task]:
        """Generate a complete schedule for the owner's pets sorted by priority then time."""
        all_tasks = owner.get_all_tasks()
        priority_order = {'urgent': 0, 'high': 1, 'medium': 2, 'low': 3}
        priority_value = lambda task: priority_order.get(task.priority.lower(), 4)
        
        def time_to_minutes(time_str: str) -> int:
            try:
                hours, minutes = map(int, time_str.split(':'))
                return hours * 60 + minutes
            except (ValueError, AttributeError):
                return 0
        
        sorted_tasks = sorted(all_tasks, key=lambda task: (priority_value(task), time_to_minutes(task.time)))
        return sorted_tasks
    
    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by their time attribute chronologically."""
        def time_to_minutes(time_str: str) -> int:
            try:
                hours, minutes = map(int, time_str.split(':'))
                return hours * 60 + minutes
            except (ValueError, AttributeError):
                return 0
        
        return sorted(tasks, key=lambda task: time_to_minutes(task.time))
    
    def filter_tasks(self, tasks: List[Task], criteria: dict) -> List[Task]:
        """Filter tasks by completed status or pet ownership."""
        filtered = tasks
        if 'completed' in criteria:
            filtered = [t for t in filtered if t.completed == criteria['completed']]
        return filtered
    
    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Return warning strings for any two tasks scheduled at the same time."""
        conflicts = []
        time_map = {}
        
        for task in tasks:
            time_key = f"{task.date} {task.time}"
            if time_key in time_map:
                conflict_msg = f"Conflict: '{task.title}' and '{time_map[time_key].title}' scheduled at {time_key}"
                conflicts.append(conflict_msg)
            else:
                time_map[time_key] = task
        
        return conflicts
    
    def build_explanation(self, tasks: List[Task]) -> str:
        """Return a readable string explaining the schedule order."""
        if not tasks:
            return "No tasks scheduled."
        
        explanation = "Schedule Overview:\n"
        for i, task in enumerate(tasks, 1):
            status = "✓" if task.completed else "○"
            explanation += f"{i}. [{status}] {task.title} - {task.date} at {task.time} ({task.duration_minutes} min, Priority: {task.priority})\n"
        
        return explanation
    
    def add_task(self, owner: Owner, pet: Pet, task: Task):
        """Add a task to a pet owned by the owner."""
        if pet in owner.pets:
            pet.add_task(task)
    
    def mark_task_complete(self, task: Task):
        """Mark a task as complete."""
        task.mark_complete()
    
    def edit_task(self, task: Task, updates: dict):
        """Edit an existing task with updates from a dictionary."""
        for key, value in updates.items():
            if hasattr(task, key):
                setattr(task, key, value)
    
    def remove_task(self, owner: Owner, pet: Pet, task: Task):
        """Remove a task from an owner's pet."""
        if pet in owner.pets and task in pet.tasks:
            pet.tasks.remove(task)
