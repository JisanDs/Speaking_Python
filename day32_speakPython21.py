"""🧠 Day 32 – Speak Python 21

Phase 6: Balanced Learning (Recursion + OOP + File Handling + Debugging + Mini Project)

✅ Problem Set

🔁 Recursion (2 problems)

Greatest Common Divisor (GCD)
Write a recursive function to calculate the GCD of two numbers.

# Input: gcd(48, 18) → Output: 6"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))
print(gcd(4, 2))
    
    
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

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def open_contacts(self):
        with open("contacts.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def load_contacts(self):
        try:
            with open("contacts.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        
    def save_contact(self):
        with open("contacts.json", "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, indent=2)

    def add_contact(self, name, phone):
        self.contacts.update({name: phone})
        self.save_contact()

    # extra fetur:
    def remove_contact(self, name):
        if name in self.contacts:
            self.contacts.pop(name)
            self.save_contact()
        else:
            print(f"{name} not found!")


    def view_contents(self):
        data = self.open_contacts()

        print("Your contacts: ")
        for name, phone in data.items():
            print(f"{name}: {phone}")

    def search_contact(self, name):
        data = self.open_contacts()

        if name in data:
            print(f"{name}: {data.get(name)}")
        else:
            print(f"{name} not found!")

ts = ContactBook()
ts.add_contact("Jisan", 234555)
ts.add_contact("Ji", 2345598)
ts.add_contact("Sonnic", 2345587)
ts.view_contents()
ts.remove_contact("Jisan")
ts.view_contents()
ts.search_contact("Ji")