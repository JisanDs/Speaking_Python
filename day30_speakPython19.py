"""🧠 Day 30 – Speak Python 19

Phase 6: Balanced Learning (Functions + OOP + File Handling)

Focus Areas:

» Functions deep dive (default parameters, *args, **kwargs, scope)
» OOP – Level 2 (class vs instance attributes, __init__ logic, multiple objects)
» File handling (read / write / save data)
» Building a small real-world mini project (Student Manager)
» Debugging common OOP / function bugs"""

"""✅ Problem 1: Functions – Stats with *args

📌 Task:
Write a function that accepts unlimited numbers (*args) and returns a dictionary with sum, average, max, min.

📎 Example:

stats(2, 5, 7, 1) ➞ {"sum":15, "avg":3.75, "max":7, "min":1}

💡 Hint:
Handle the case when no arguments are given (return None or an informative message)."""

# def stats(*args):
#     if not args:
#         return None
#     else:
#         d = {
#             "sum":sum(args),
#             "avg":sum(args) / len(args),
#             "max":max(list(args)),
#             "min":min(list(args))
#         }

#         return d

# print(stats(2, 5, 7, 1))
# print(stats(8, 7, 2, 89))
# print(stats())


"""✅ Problem 2: Functions – Default params + **kwargs

📌 Task:
Write a greet(name, greeting="Hello", **kwargs) function that returns a formatted greeting. Use **kwargs to accept optional details (e.g., title="Mr.", lang="bn").

📎 Example:

greet("Jisan") ➞ "Hello, Jisan!"
greet("Jisan", greeting="Hi", title="Mr.") ➞ "Hi, Mr. Jisan!"

💡 Hint:
Check for title in kwargs and prepend it if present. Use default greeting when none provided."""

# def greet(name, greeting="Hello", **kwargs):
#     if not kwargs:
#         return f"{greeting}, {name}!"
#     else:
#         for title in kwargs.values():
#             return f"{greeting}, {title} {name}!"

# print(greet("Jisan"))
# print(greet("Jisan", greeting="Hi", title="Mr."))
# print(greet("Sonnic", greeting="Welcome", title="Dr."))


"""✅ Problem 3: OOP – Student Class (Level 2)

📌 Task:
Create a Student class with:

attributes: name, age, grade

method: get_details() → returns a details string
method: is_passed() → returns True if grade >= 40 else False

📎 Example:

s = Student("Jisan", 20, 85)
s.get_details() ➞ "Name: Jisan, Age: 20, Grade: 85"
s.is_passed() ➞ True


💡 Hint:
Use __init__ to set attributes. Keep grade numeric."""

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_details(self):
#         print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

#     def is_passed(self):
#         if self.grade > 60:
#             print(True)
#         else:
#             print(False)

# s = Student("Jisan", 20, 85)
# s.get_details()
# s.is_passed()


"""✅ Problem 4: File Handling – Save & Load Students

📌 Task:
Write two functions:

save_students(filename, students_list) — saves students (one per line, e.g. name|age|grade)
load_students(filename) — reads file and returns a list of Student objects

📎 Example file students.txt:

Jisan|20|85
Rafi|19|72


load_students("students.txt") ➞ [Student("Jisan",20,85), Student("Rafi",19,72)]

💡 Hint:
Use str.split("|") to parse each line. Handle missing file with try/except."""


def save_students(filename, students_list):
    with open(filename, "a") as f:
        for student in students_list:
            f.write(f"{student}\n")

def load_students(filename):
    try:
        with open(filename, "r") as f:
            data = f.readlines()
            students_list = []
            for student in data:
                nag = student.replace("\n", "").split("|")
                students_list.append((f"Student{nag[0], nag[1], nag[2]}"))
            return students_list
    except FileNotFoundError:
        return "File Not Foound"

save_students("students.txt", ["Jisan|20|93", "Rafi|19|83"])
print(load_students("students.txt"))


"""⚒️ Mini Project – Student Management System (OOP + File)

📌 Task:
Build a StudentManager class that can:

add a student (add_student(name, age, grade))
list all students (list_students())
compute average grade (average_grade())
save to file (save(filename)) and load from file (load(filename))

📎 Example usage:

mgr = StudentManager()
mgr.add_student("Jisan",20,85)
mgr.add_student("Rafi",19,72)
mgr.list_students()
mgr.average_grade() ➞ 78.5
mgr.save("students.txt")


💡 Hint:
Internally keep a list of Student objects. Reuse save_students / load_students functions from Problem 4."""


class StudentManager:
    def add_student(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

        with open("students.txt", "a") as f:
            f.write(f"{self.name}|{self.age}|{self.grade}\n")

    def students_list(self):
        try:
            with open("students.txt", "r") as f:
                data = f.readlines()
                students_list = []
                for student in data:
                    nag = student.replace("\n", "").split("|")
                    students_list.append((f"Student{nag[0], nag[1], nag[2]}"))
                print(students_list)
                return students_list
        except FileNotFoundError:
            print("File Not Foound")

    def average_grade():
        return 