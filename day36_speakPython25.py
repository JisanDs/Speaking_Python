""" Day 36 – Speak Python 25

Phase 7: Real-World Thinking (Recursion + Data Structures + OOP + Debugging + Mini Project)"""


"""✅ Problem Set
🔁 Recursion (2 problems)

1. Factorial (Recursive)
Write a recursive function to calculate factorial of a number.

Input: factorial(5)
Output: 120"""

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n
    
# print(factorial(5))


"""2. Fibonacci (Recursive)
Write a recursive function to generate the nth Fibonacci number.

Input: fibonacci(6)
Output: 8"""

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    
# print(fibonacci(6))


"""⚡ Other Concepts (2 problems)

3. List Comprehension with Condition
Create a list comprehension to get all numbers from 1 to 50 that are divisible by both 3 and 5.

Output: [15, 30, 45]"""

div = [ n for n in range(1, 51) if n % 3 == 0 and n % 5 == 0 ]
# print(div)


"""4. Dictionary Value Transformation
Given:

prices = {"apple": 50, "banana": 20, "cherry": 30}

Create a new dictionary where each price is increased by 10%.

Output:
{"apple": 55.0, "banana": 22.0, "cherry": 33.0}"""


def add_tax(price, tax):
    """This function add 10% tax price in your dict."""
    inc_prices = {}
    for prod, price in prices.items():
        inc_prices[prod] = (price / tax) + price
    return inc_prices

prices = {"apple": 50, "banana": 20, "cherry": 30}

# print(add_tax.__doc__)
# print(add_tax(prices, 23))


"""🛠️ Debugging Task

Buggy code:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print("Name:" + self.name + ", Marks:" + self.marks)

s = Student("Jisan", 90)
s.display()

👉 Fix the error so that it correctly prints:
Name: Jisan, Marks: 90"""

# fixed code:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    """def display(self):
        print("Name:" + self.name + ", Marks:" + str(self.marks))"""
        
        # this is better way
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s = Student("Jisan", 90)
# s.display()


"""📂 Mini Project – Task Manager

Create a simple Task Manager.

Features:

add_task(title, description) → add a new task
view_tasks() → display all tasks with status
remove_task(title) → delete a task by title
mark_done(title) → mark a task as completed"""

# All tasks should be saved in tasks.json (you can use your FileUtilites library).
from FileUtilites import load_json, save_json
class TaskManager:
    def __init__(self, file="tasks.json"):
        self.file = file
        self.tasks = load_json(self.file)

    def add_task(self, title, description):
        if title not in self.tasks:
            self.tasks[title] = description
            save_json(self.tasks, self.file)
        else:
            print("Task alredy exist!")

    def view_tasks(self):
        if not self.tasks:
            print("Empty")
        else:
            for title, des in self.tasks.items():
                print(f"{title}: {des}")
    
    def remove_task(self, title):
        if title in self.tasks:
            del self.tasks[title]
            save_json(self.tasks, self.file)
        else:
            print("Invalid Title")

    def mark_done(self, title):
        if title in self.tasks:
            if "✓" not in self.tasks[title]:
                self.tasks[title] = str(self.tasks[title] + "✓")
                save_json(self.tasks, self.file)
            else:
                print("Alredy mark done")
        else:
            print("Invalid Title")



tm = TaskManager()
# tm.add_task("learn python", "learn python form cs50p")
# tm.add_task("learn bash", "learn bash from chatgpt")
# tm.view_tasks()
# tm.remove_task("learn python")
# tm.view_tasks()
# tm.mark_done("learn bash")
# tm.view_tasks()