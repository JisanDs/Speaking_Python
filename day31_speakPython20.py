"""🧠 Day 31 – Speak Python 20

Phase 6: Balanced Learning (Recursion + Core Topics + Debugging + Mini Project)"""


"""✅ Problem Set

🔁 Recursion (2 problems)

1. Sum of Digits
Write a recursive function that takes an integer and returns the sum of its digits.

Input: 1234 → Output: 10 (1+2+3+4)"""

"""def sum_digits(d):
    if d // 10 == 0:
        return d
    return (d % 10) + sum_digits(d // 10)
    
print(sum_digits(565))
print(sum_digits(1234))"""


"""2. Palindrome Check (Recursive)
Write a recursive function to check if a string is a palindrome.

# Input: "madam" → True
# Input: "python" → False"""

"""def is_palindrom(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])
    
print(is_palindrom("madam"))
print(is_palindrom("python"))"""


"""⚡ Other Concepts (2 problems)

3. Lambda + Filter
Use lambda and filter() to filter only the even numbers from a list."""

"""nums =  [5, 12, 17, 18, 24, 32]

is_even = lambda x: x % 2 == 0
even = filter(is_even, nums)

for n in even:
    print(n)"""
    
    
"""4. JSON File Handling
Save a Python dictionary into a file in JSON format, then load it back and print it."""

import json

student = {"name": "Jisan", "age": 20, "skills": ["Python", "Git", "OOP"]}

def write_json(filename, obj, indent=2):
    with open(filename, "w") as f:
        json.dump(obj, f, indent=indent)
        
write_json("student.json", student)

# this for testing
write_json("test.json", student, indent=4)

def read_json(filename):
    with open(filename, "r") as f:
        return json.load(f)
        
data = read_json("student.json")
print(data)

print(data.get("name"))
print(data.get("age"))
print(data.get("skills")[2])


"""🛠️ Debugging Task

5. Recursive Factorial Bug Fix
Debug the following code (the base case is wrong):

def fact(n):
    if n == 0:
        return 0 
    return n * fact(n-1)

print(fact(5))  # Expected: 120"""

    # fixed code:
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(5))


"""📂 Mini Project

6. Expense Tracker (File Handling + OOP)

Create a class ExpenseTracker.

Features:
    
add_expense(name, amount) → add an expense (save it to file)
view_expenses() → show all expenses
total_expense() → calculate the total amount

Save each entry in JSON format in a file."""


class ExpenseTracker:
    def __init__(self):
        self.exp_amount = []
        self.expenses = {}
        
    def add_expense(self, name, amount):
        self.expenses.update({name: amount})
        # i alrady writed this function 'write_json()' in problam 4
        write_json("expenses.json", self.expenses)
        
        self.exp_amount.append(amount)
        
    def view_expenses(self):
        # i alrady writed this function 'read_json()' in problam 4.
        data = read_json("expenses.json")
        
        print("Your Expenses:")
        for exp, amount in data.items():
            print(f"{exp}: {amount}")
            
    def total_expenses(self):
        return sum(self.exp_amount)

ts = ExpenseTracker()
ts.add_expense("cake", 50)
ts.add_expense("cokies", 45)
ts.add_expense("biskit", 34)
ts.add_expense("speed", 25)
ts.add_expense("coffi", 275)
ts.view_expenses()
print(ts.total_expenses())