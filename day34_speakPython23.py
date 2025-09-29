""" Day 34 – Speak Python 23

Phase 6: Balanced Learning (Recursion + Data Structures + OOP + Debugging + Mini Project)

✅ Problem Set

🔁 Recursion (2 problems)

1. Factorial (Recursive)
Write a recursive function to calculate factorial of a number.
Input: factorial(5) → Output: 120"""

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
    
# print(factorial(5))


"""2. Sum of Digits (Recursive)
Write a recursive function that returns the sum of digits of a number.
Input: sum_digits(1234) → Output: 10"""

# def sum_digits(d):
#     if d // 10 == 0:
#         return d
#     return (d % 10) + sum_digits(d // 10)

# print(sum_digits(1234))


"""⚡ Other Concepts (2 problems)

3. Dictionary Merging
Merge two dictionaries and handle duplicate keys by summing values.

# dict1 = {"a": 2, "b": 4, "c": 6}
# dict2 = {"a": 3, "c": 1, "d": 7}
# # Output → {"a": 5, "b": 4, "c": 7, "d": 7}"""

def int_dict_marge(dict1, dict2):
    try:
        marged = dict1.copy()

        for k, v in dict2.items():
            marged[k] = marged.get(k, 0) + v
        return marged
    except TypeError:
        return "Function onley marge int"

dict1 = {"a": 2, "b": 4, "c": 6}
dict2 = {"a": 3, "c": 1, "d": "7"}

print(int_dict_marge(dict1, dict2))


"""4. Tuple Operations
Given a tuple of numbers, find:

- Maximum value
- Minimum value
- Sum of all numbers"""

# my_tuple = (4, 6, 4, 89, 7, 34)

# # unfuni method
# def main():
#     print(max(my_tuple))
#     print(min(my_tuple))
#     print(sum(my_tuple))


# def max_tup(my_tuple):
#     max_num = my_tuple[0]
#     for n in my_tuple:
#         if n > max_num:
#             max_num = n
#     return max_num

# def mini_tup(my_tuple):
#     mini_num = my_tuple[0]
#     for n in my_tuple:
#         if n < mini_num:
#             mini_num = n
#     return mini_num

# def sum_tup(my_tuple):
#     my_sum = 0
#     for n in my_tuple:
#         my_sum += n
#     return my_sum
    
# def arg_sum_tup(*my_tuple):
#     my_sum = 0
#     for n in my_tuple:
#         my_sum += n
#     return my_sum
    
# print(max_tup(my_tuple))
# print(mini_tup(my_tuple))
# print(sum_tup(8, 7, 7)) # TypeError and this function need extra bracket (8, 7, 7) this shodbe right.
# print(arg_sum_tup(8, 7, 7)) # no error and also no need any extra bracket.


"""🛠️ Debugging Task

Fix this code:

class Student:
    def __init__(self, name):
        self.name = name

class CollegeStudent(Student):
    def __init__(self, name, subject):
        self.subject = subject

s = CollegeStudent("Jisan", "Python")
print(s.name, s.subject)   # Expected: Jisan Python"""

# fixed code:
# class Student:
#     def __init__(self, name):
#         self.name = name

# class CollegeStudent(Student):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

# s = CollegeStudent("Jisan", "Python")
# print(s.name, s.subject)


"""📂 Mini Project

Expense Tracker (OOP + File Handling)

Create a class ExpenseTracker.

Features:

add_expense(amount, category) → add new expense
view_expenses() → view all expenses
total_expense() → show total spending

Save data persistently in expenses.json."""

# import file_utilites as fu


# class ExpenseTracker:
#     def __init__(self, filename="expenses.json"):
#         self.file = filename
#         self.data = fu.load_json(self.file)
        
#     def add_expenses(self, amount, category):
#         count = str(len(self.data) + 1)
#         self.data[count] = {"amount": amount, "category": category}
#         fu.save_json(self.data, self.file)
    
#     def view_expenses(self):
#         if not self.data:
#             print("No data recorded")
#             return 
#         for vlu in self.data.values():
#             print(f"Category: {vlu["category"]}, Amount: {vlu["amount"]}")
                
#     def total_expense(self):
#         total = sum(vlu["amount"] for vlu in self.data.values())
#         return total


# et = ExpenseTracker()
# et.add_expenses(66, "Drink")
# et.add_expenses(120, "Food")
# et.view_expenses()
# print("Total:", et.total_expense())