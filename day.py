"""🧠 Day 37 – Speak Python 26

Phase 7: Real-World Thinking (Recursion + Data Structures + OOP + Debugging + Mini Project)
"""

# ---------------------------------------------------
"""✅ Problem Set

🔁 Recursion (2 problems)

1. Sum of Digits (Recursive)
Write a recursive function that returns the sum of digits of a number.

Input: sum_digits(1234)
Output: 10"""

def sum_digits(d):
    if d // 10 == 0:
        return d
    return (d % 10) + sum_digits(d // 10)
    
# print(sum_digits(1234))

# ---


"""2. Reverse String (Recursive)
Write a recursive function to reverse a string.

Input: "hello"
Output: "olleh" """

def rvs_str(s):
    if len(s) == 1:
        return s
    return rvs_str(s[1:len(s)]) + s[0]
    
# print(rvs_str("jisan"))

# ---------------------------------------------------


"""⚡ Other Concepts (2 problems)

3. List Flattening
Given: nested_list = [[1, 2], [3, 4], [5, 6]]
Flatten this into a single list: [1, 2, 3, 4, 5, 6]"""

def unpack_nested_lst(nested_list):
    """This function unpack 2D list"""
    try:
        single_list = []
        for lst in nested_list:
            for n in lst[0: len(lst)]:
                single_list.append(n)
        return single_list
    except TypeError:
        return "Only allow '2D' list"
    
nested_list = [[1, 2], [3, 4], [5, 6]]
nst = [7, 6, 7]
nst_lst = [
    [8, 8, 7, 6],
    [5, 5, 4, 4],
    [7, 2, 1, 0]
]

"""print(unpack_nested_lst.__doc__)

print(unpack_nested_lst(nested_list))
print(unpack_nested_lst(nst))
print(unpack_nested_lst(nst_lst))"""
# ---

"""4. Dictionary Merge
Given:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

Merge them into: {"a": 1, "b": 3, "c": 4}"""

def int_dict_marger(dict1, dict2):
    try:
        marge = dict1.copy()
        
        for k, v in dict2.items():
            marge[k] = dict1.get(k, 0) + v
        return marge
    except TypeError:
        return "Function only marge int"


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

test1 = {"math": 87, "cham": 76}
test2 = {"phy": 93, "cs": 99}

print(int_dict_marger(dict1, dict2))
print(int_dict_marger(test1, test2))


# ---------------------------------------------------


"""🛠️ Debugging Task

Buggy code:

class Car:
    def __init__(self, model, year):
        self.model = model
        year = year

c = Car("Tesla", 2025)
print(c.year)

👉 Fix the error so it correctly prints 2025."""

# fixed code:
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

c = Car("Tesla", 2025)
# print(c.year)
# ---------------------------------------------------


"""📂 Mini Project – Notes App (OOP + File Handling)

Create a simple Notes App.

Features:
- add_note(title, content) → add a new note
- view_notes() → display all notes
- delete_note(title) → delete a note
- search_note(keyword) → search notes by keyword

All notes should be saved in notes.json (you can use your FileUtilites library)."""

from fileutillites import save_json, load_json


class SimpleNotes:
    def __init__(self, file="notes.json"):
        self.file = file
        self.notes = load_json(self.file)
        
    def add_note(self, title, content):
        if title not in self.notes:
            self.notes[title] = content
            save_json(self.notes, self.file)
        else:
            print("alredy exist")
            
    def view_notes(self):
        if self.notes:
            for title, cont in self.notes.items():
                print(f"Title: {title}")
                print(f"Content: {cont}")
        else:
            print("Notes are empty")
            
    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            save_json(self.notes, self.file)
        else:
            print("This note not exist")

    def search_note(self, title):
        if title in self.notes:
            print(self.notes[title])
        else:
            print("This note not exist")

    def clear_notes(self):
        if self.notes:
            self.notes = {}
            save_json(self.notes, self.file)
        else:
            print("Notes are empty")

sn = SimpleNotes()

"""sn.add_note("Test", "This is a note class")
sn.add_note("Learn Regex", "Learn regex from cs50p")
sn.add_note("Bash Script", "Bash script is use to creat autometion")
sn.view_notes()
sn.delete_note("test")
sn.delete_note("Test")
sn.view_notes()
sn.search_note("test")
sn.search_note("Learn Regex")

sn.view_notes()
sn.clear_notes()
sn.view_notes()"""