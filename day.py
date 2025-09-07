"""🧠 Day 32 – Speak Python 21

Phase 6: Balanced Learning (Recursion + OOP + File Handling + Debugging + Mini Project)

✅ Problem Set

🔁 Recursion (2 problems)

Greatest Common Divisor (GCD)
Write a recursive function to calculate the GCD of two numbers.

# Input: gcd(48, 18) → Output: 6"""

def gcd(n, n2):
    pass
    
    
"""Power Function (Recursive)
Write a recursive function to calculate a^b (a raised to the power b).

# Input: power(2, 5) → Output: 32 """

"""def power(n, p):
    if p == 0:
        return 1
    return n * power(n, p-1)
    
print(power(2, 5))
print(power(3, 3))
print(power(5, 3))"""

"""⚡ Other Concepts (2 problems)

Dictionary Comprehension
From a list of numbers, create a dictionary where the key is the number and the value is its square.

# Input: [1, 2, 3, 4] → {1: 1, 2: 4, 3: 9, 4: 16} """

"""def square_dict(lst):
    return {n: n * n for n in lst}
    
print(square_dict([1, 2, 3, 4]))"""


"""File Handling – Append Mode
Write a program that takes user input and appends it to a text file (notes.txt).
Each new input should be saved on a new line."""

"""with open("notes.txt", "w") as f:
    pass"""
    
"""def append_data(filename, user_input):
    with open(filename, "a") as f:
        f.write(f"{user_input}\n")

data = input("Whats your mind today?\n")
append_data("notes.txt", data)

# this for checking data is append or not
with open("notes.txt", "r") as f:
    print(f.read())"""
    
    
"""🛠️ Debugging Task

OOP Constructor Bug
The following code has a bug in the constructor. Fix it so the program runs correctly:

class Student:
    def __init__():
        self.name = "Unknown"
        self.age = 0
s = Student()
print(s.name)"""

# fixed code:
"""class Student:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
s = Student()
print(s.name)"""


"""📂 Mini Project

Contact Book (OOP + File Handling)
Create a simple contact book program.

Create a class ContactBook.

Features: 

add_contact(name, phone) → save contact to a JSON file
view_contacts() → show all contacts
search_contact(name) → search by name and display details

Store all contacts in a file called contacts.json."""

import json

dict = {"h": 3, "u": 7}
print(json.dumps(dict))