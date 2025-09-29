"""Phase 7: Real-World Thinking (Recursion + Data Structures + OOP + Debugging + Mini Project)

✅ Problem Set

🔁 Recursion (2 problems)

Greatest Common Divisor (GCD – Recursive)
Write a recursive function to find the GCD of two numbers using the Euclidean algorithm.

Input: gcd(48, 18)
Output: 6"""

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

# print(gcd(48, 18))



"""String Length (Recursive)
Write a recursive function to calculate the length of a string without using len().

Input: str_len("python")
Output: 6"""

def str_len(s):
    if len(s) <= 0:
        return s
    return  str_len(s[0:len(s)])
    
#print(str_len("jisan"))


"""⚡ Other Concepts (2 problems)

Tuple Comprehension (Generator Expression)
Create a generator expression that yields squares of numbers from 1 to 10.

Output: 1, 4, 9, 16, ..., 100"""

seq = (n * n for n in range(1, 11))
for x in seq:
    #print(x, end=", ")
    pass
    
    
"""Dictionary Inversion
Given:
students = {"Alice": 1, "Bob": 2, "Charlie": 3}

Invert it to:
{1: "Alice", 2: "Bob", 3: "Charlie"}"""

students = {"Alice": 1, "Bob": 2, "Charlie": 3}

inv = {v: k for k, v in students.items()}
#print(inv)


"""🛠️ Debugging Task

Buggy code:

class Rectangle: def __init__(self, width, height): self.width = width height = height def area(self): return self.width * self.height r = Rectangle(5, 10) print(r.area()) # Expected: 50 """

"""👉 Fix the error so that it works correctly.

📂 Mini Project – Expense Tracker (OOP + File Handling)

Create a simple Expense Tracker.

Features:

add_expense(category, amount) → add a new expense
view_expenses() → display all expenses
total_expenses() → show total amount spent
remove_expense(category) → remove expense by category"""

# All expenses should be saved in expenses.json.

from file_utilites import save_json, load_json


class ExpenseTracker:
    def __init__(self, file="expensea.json"):
        self.file = file
        self.expenses = load_json(self.file)
        
    def add_expense(self, category, amount):
        count = 0
        if count not in self.expenses:
            self.expenses[count] = {}
            self.expenses[count]["category"] = category
            self.expenses[count]["amount"] = amount
            save_json(self.expenses, self.file)
        else:
            print("alrady exist")
            
    def view_expenses(self):
        pass
        
    def total_expenses(self):
        pass
        
    def remove_expense(self, category):
        pass

et = ExpenseTracker()
et.add_expense("frout", 89)
et.add_expense("game", 6799)

print(type(et))