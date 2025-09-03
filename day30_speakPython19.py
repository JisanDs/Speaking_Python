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
#             "max":max(args),
#             "min":min(args)
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
#     title = kwargs.get("title", "")
#     if title:
#         return f"{greeting}, {title} {name}!"
#     return f"{greeting}, {name}!"
    

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
#         return self.grade >= 40

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
    students_list = []
    try:
        with open(filename, "r") as f:
            data = f.readlines()
            students_list = []
            for student in data:
                nag = student.replace("\n", "").split("|")
                students_list.append((f"Student{nag[0], nag[1], nag[2]}"))
            return students_list
    except FileNotFoundError:
        return []
    return students_list

# save_students("students.txt", ["Jisan|20|93", "Rafi|19|83"])
# print(load_students("students.txt"))


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


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_detalis(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
def save_students(filename, students_list):
    with open(filename, "w") as f:
        for student in students_list:
            f.write(f"{student.name}|{student.age}|{student.grade}\n")

def load_students(filename):
    students_list = []
    try:
        with open(filename, "r") as f:
            for line in f:
                name, age, grade = line.strip().split("|")
                students_list.append(Student(name, int(age), int(grade)))
            return students_list
    except FileNotFoundError:
        return []
    return students_list
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        self.students.append(Student(name, age, grade))

    def list_students(self):
        for student in self.students:
            print(student.get_detalis())

    def average_grade(self):
        if not self.students:
            return 0
        return sum(s.grade for s in self.students) / len(self.students)
    
    def save(self, filename):
        save_students(filename, self.students)

    def load(self, filename):
        self.students = load_students(filename)


mgr = StudentManager()
mgr.add_student("Jisan",20,85)
mgr.add_student("Rafi",19,72)
mgr.list_students()
mgr.average_grade()
mgr.save("students.txt")
mgr.save("updata.txt")


"""🐞 Debugging Task – Fix the Code (OOP gotcha: class vs instance attribute)

❌ Wrong Code:

class School:
    students = []

    def add_student(self, name):
        self.students.append(name)

s1 = School()
s2 = School()
s1.add_student("A")
s2.add_student("B")
print(s1.students)  # ➞ ["A", "B"]
print(s2.students)  # ➞ ["A", "B"]


✅ Expected Behavior:
Each School() instance should have its own students list.
print(s1.students) ➞ ["A"]
print(s2.students) ➞ ["B"]

👉 Fix it: move students into __init__ as an instance attribute (self.students = [])."""
# ✅ Fixed code:

# class School:
#     def __init__(self):
#         self.students = []

#     def add_student(self, name):
#         self.students.append(name)

# s1 = School()
# s2 = School()
# s1.add_student("A")
# s2.add_student("B")
# print(s1.students)  
# print(s2.students)  