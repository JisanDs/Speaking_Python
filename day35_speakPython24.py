"""🧠 Day 35 – Speak Python 24

Phase 6: Balanced Learning (Recursion + Data Structures + OOP + Debugging + Mini Project)

✅ Problem Set
🔁 Recursion (2 problems)

1. Power Function (Recursive)
Write a recursive function to calculate a^b (a raised to the power of b).

Input: power(2, 5)

Output: 32"""

# def power(a, b):
#     if b == 0:
#         return 1
#     return a * power(a, b-1)

# print(power(2, 5))


"""2. Palindrome Check (Recursive)
Write a recursive function to check if a string is a palindrome.

Input: "madam" → Output: True
Input: "python" → Output: False"""

# def is_palindrome(s):
#     try:
#         if len(s) == 0:
#             return True
#         elif s[0] != s[-1]:
#             return False
#         return is_palindrome(s[1:-1])
#     except RecursionError:
#         return "maximam"
    
# print(is_palindrome("madam"))
# print(is_palindrome("python"))
# print(is_palindrome("racecar"))


"""⚡ Other Concepts (2 problems)

3. Set Comprehension
Write a set comprehension that stores only the even numbers from 1 to 20.

Output: {2, 4, 6, 8, ..., 20}"""

# even_set = {n for n in range(1, 11) if n % 2 == 0}
# print(even_set)

"""4. Dictionary Filtering Given:

scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}

Create a new dictionary with only those who scored 80 or above.

Output: {"Alice": 85, "Charlie": 90}"""

scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}

# hiscores = {}
# for name, score in scores.items():
#     if score > 80:
#         hiscores[name] = score
# print(hiscores)


"""🛠️ Debugging Task
Buggy code:

class Person:
    def __init__(self, name):
        name = name

p = Person("Jisan")
print(p.name)   # Expected: Jisan

👉 Find the error and fix it."""

# Fixed code:

# class Person:
#     def __init__(self, name):
#         self.name = name

# p = Person("Jisan")
# print(p.name)


"""📂 Mini Project

Contact Book (OOP + File Handling)

একটা ছোট contact manager বানাও।

Features:

add_contact(name, phone) → নতুন contact যোগ করবে
view_contacts() → সব contact দেখাবে
remove_contact(name) → নাম দিয়ে contact delete করবে

Contacts গুলো contacts.json এ save হবে (তোমার FileUtilites library ব্যবহার করতে পারো)।"""

from FileUtilites import save_json, load_json


class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.file = filename
        self.contact = load_json(self.file)

    def add_contact(self, name, phone):
        if name not in self.contact:
            self.contact[name] = str(phone)
            save_json(self.contact, self.file)
        else:
            print(f"{name} already exist")

    def view_contacts(self):
        if not self.contact:
            print("Contacts are empty")
        else:
            for n, (name, phone) in enumerate(self.contact.items(), 1):
                print(f"{n}. Name: {name}, Phone: {phone}")

    def remove_contact(self, name):
        if name in self.contact:
            del self.contact[name]
            save_json(self.contact, self.file)
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, new_phone):
        if name in self.contact:
            self.contact[name] = str(new_phone)
            save_json(self.contact, self.file)
        else:
            print(f"Contact '{name}' not found.")


# test's  
cb = ContactBook()
cb.add_contact("Jisan", 88987)
cb.add_contact("Sonnic", 88323)
cb.add_contact("Stranger", 99733)
cb.view_contacts()

cb.remove_contact("Sonnic")
cb.view_contacts()

cb.update_contact("Jisan", 99878)
cb.view_contacts()