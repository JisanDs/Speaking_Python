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



"""def lst_sum(lst):
    if len(lst) == 0:
        return lst[0]
    return lst[0] + lst_sum(lst[0:])


print(lst_sum([1, 2, 3, 4, 5]))"""


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

students = [
    {"name": "Jisan", "age": 20},
    {"name": "Nova", "age": 21}
]
import csv






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