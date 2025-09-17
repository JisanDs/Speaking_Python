"""📂 Mini Project

6. Task Manager (OOP + File Handling)
Build a small Task Manager program.

Create a class TaskManager.

Features:

add_task(task) → add a new task (save to JSON file)
view_tasks() → show all tasks
remove_task(task) → remove a task

Save tasks persistently in a file tasks.json."""

import json
# fileutillites is my wone library 
from fileutillites import load_json


class TaskManager:
    def __init__(self, filename="tasks.json"):
        #self.tasks = []
        self.filename = filename
        self.data = load_json(self.filename)
            
    def save_task(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file)
            
    def add_task(self, task):
        self.data.append(task)
        self.save_task()
        
    def view_task(self):
        for n, task in enumerate(self.data, start=1):
            print(f"{n}. {task}")
            
    def remove_task(self, task_number):
        if task_number in self.data:
            self.data.pop(task_number -1)
            self.save_task()
        else:
            print("Invalid task")


"""tm = TaskManager()
tm.add_task("hello")
tm.add_task("by")
tm.view_task()
tm.remove_task(1)
tm.view_task()"""