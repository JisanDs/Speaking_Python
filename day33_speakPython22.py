"""🧠 Day 33 – Speak Python 22

Phase 6: Balanced Learning (Recursion + File Handling + OOP + Debugging + Mini Project)"""

"""✅ Problem Set

🔁 Recursion (2 problems)

1. Reverse String (Recursive)
Write a recursive function that reverses a given string.

# Input: "python" → Output: "nohtyp" """

"""def reverse_str(s):
    if len(s) == 1:
        return s
    return reverse_str(s[1:]) + s[0]
    
print(reverse_str("Jisan"))
print(reverse_str("python"))"""


"""2. Sum of List Elements (Recursive)
Write a recursive function to calculate the sum of elements in a list.

# Input: [1, 2, 3, 4, 5] → Output: 15"""

# def sum_list(lst):
#     if not lst:
#         return 0
#     return lst[0] + sum_list(lst[1:])

# print(sum_list([1, 2, 3, 4, 5]))
# print(sum_list([1, 3, 4]))

"""⚡ Other Concepts (2 problems)

3. Set Operations
Write a program to:

Find the union, intersection, and difference of two sets.

A = {1, 2, 3, 4}  
B = {3, 4, 5, 6}  
# Union → {1, 2, 3, 4, 5, 6}  
# Intersection → {3, 4}  
# Difference (A - B) → {1, 2}"""

# A = {1, 2, 3, 4}  
# B = {3, 4, 5, 6}

# def main():
#     print(A.union(B))
#     print(A.intersection(B))
#     print(A.difference(B))

# main()

# manual just for fun:
# Difference (A - B) → {1, 2}
# def set_diff(a, b):
#     diff = set()
#     for item in a:
#         if item not in b:
#             diff.add(item)
#     return diff
# print(set_diff(A, B))

"""4. CSV File Handling
Write a program to save a list of dictionaries into a CSV file, and then read it back."""

# import csv

# students = [
#     {"name": "Jisan", "age": 20},
#     {"name": "Nova", "age": 21}
# ]

# fields = ["name", "age"]

# def csv_dictwriter(dict, fields, filename="csv_data.csv"):
#     with open(filename, "w", newline="") as cf:
#         write = csv.DictWriter(cf, fieldnames=fields)
#         write.writeheader()
#         write.writerows(students)

# csv_dictwriter(students, fields)
# csv_dictwriter(students, fields, filename="ts.csv")

# with open("csv_data.csv", "r", encoding="utf-8", newline="") as cf:
#     # readata = csv.DictReader(cf)
#     readata = csv.reader(cf)
#     for data in readata:
#         print(data)


"""🛠️ Debugging Task

5. Method Bug
The following code has a bug. Fix it so it runs correctly:

class Person:
    def __init__(self, name):
        name = name   # ❌ bug
    def show(self):
        print(self.name)

p = Person("Jisan")
p.show()   # Expected output: Jisan"""


"""class Person:
    def __init__(self, name):
        name = name   # ❌ bug
    def show(self):
        print(self.name)

p = Person("Jisan")
p.show()   # Expected output: Jisan """


# fixed code:
# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def show(self):
#         print(self.name)

# p = Person("Jisan")
# p.show()


"""📂 Mini Project

6. Student Grade Manager (OOP + File Handling)
Create a program to manage student grades.

Create a class GradeManager.

Features:

add_grade(name, subject, grade) → save to JSON file
view_grades() → show all student grades
search_student(name) → show grades of a specific student
average_grade(name) → calculate average grade of that student

Store everything in a file called grades.json."""

import json


class GradeManager:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            with open("students_data.json", encoding="utf-8") as jsf:
                return json.load(jsf)
        except FileNotFoundError:
            return {}
        
    def save_data(self):
        with open("students_data.json", "w", encoding="utf-8") as jsf:
            json.dump(self.data, jsf, indent=2)

    def add_grade(self, name, subject, grade):
        if name not in self.data:
            self.data[name] = {}
        self.data[name][subject] = grade
        self.save_data()

    def view_grades(self):
        students = self.load_data()
        for student in students.values():
            for name, grade in student.items():
                print(grade)


students = {
    "jisan": {
        "math": 89
    },
    "robart": {
        "cham": 98
    },
    "sonnic": {
        "math": 87
    }
}

name = "jisna"
for names in students.keys():
    if name == names:
        for student in students.values():
            for subject, grade in student.items():
                print(grade)
else:
    print("not")