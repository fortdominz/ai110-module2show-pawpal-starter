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
        pass


@dataclass
class Pet:
    """Represents a pet owned by an owner."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)
    
    def add_task(self, task: Task):
        """Add a task to the pet's task list."""
        pass
    
    def get_tasks(self) -> List[Task]:
        """Retrieve all tasks for the pet."""
        pass


@dataclass
class Owner:
    """Represents a pet owner."""
    name: str
    pets: List[Pet] = field(default_factory=list)
    
    def add_pet(self, pet: Pet):
        """Add a pet to the owner's pet list."""
        pass
    
    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks across all pets."""
        pass


class Scheduler:
    """Orchestrates scheduling and management of pet care tasks."""
    
    def generate_schedule(self, owner: Owner):
        """Generate a complete schedule for the owner's pets."""
        pass
    
    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by time."""
        pass
    
    def filter_tasks(self, tasks: List[Task], criteria):
        """Filter tasks based on given criteria."""
        pass
    
    def detect_conflicts(self, tasks: List[Task]) -> List:
        """Detect scheduling conflicts in tasks."""
        pass
    
    def build_explanation(self, tasks: List[Task]) -> str:
        """Build a human-readable explanation of the schedule."""
        pass
    
    def add_task(self, owner: Owner, pet: Pet, task: Task):
        """Add a task to a pet owned by the owner."""
        pass
    
    def mark_task_complete(self, task: Task):
        """Mark a task as complete."""
        pass
    
    def edit_task(self, task: Task, updates):
        """Edit an existing task with updates."""
        pass
    
    def remove_task(self, owner: Owner, pet: Pet, task: Task):
        """Remove a task from an owner's pet."""
        pass
