"""🧠 **Day 22 – Speak Python 11**

 Focus Areas:

* Sets & Operations
* Dictionary + List Combo
* Data Filtering
* Micro Project with Real-Life Idea"""

"""✅ Problem 1: Unique Elements with Sets

📌 **Task:**
Write a function that takes two lists and returns the **unique common elements** between them.

📎 **Example:**

```python
common_unique([1, 2, 3, 4], [3, 4, 4, 5, 6]) ➞ {3, 4}  
common_unique(["apple", "banana"], ["banana", "orange"]) ➞ {"banana"}
```

💡 **Hint:** Use `set()` and intersection `&`.
⏱️ **Target Time:** 10 minutes"""

# def common_unique(lst1, lst2):
#     s1 = set(lst1)
#     s2 = set(lst2)
#     return s1.intersection(s2)

# print(common_unique([1, 2, 3, 4], [3, 4, 4, 5, 6]))
# print(common_unique(["apple", "banana"], ["banana", "orange"]))


"""🧪 Problem 2: Invert a Dictionary

📌 **Task:**
Write a function that inverts a dictionary: keys become values and values become keys.

📎 **Example:**

```python
invert_dict({"a": 1, "b": 2, "c": 3}) ➞ {1: "a", 2: "b", 3: "c"}
invert_dict({"Jisan": 85, "Rahim": 90}) ➞ {85: "Jisan", 90: "Rahim"}
```

🎯 **Focus:** Key-value flipping.
💡 **Hint:** Loop or dictionary comprehension.
⏱️ **Target Time:** 12 minutes"""

# def invert_dict(dict):
#     invert_dict = {}
#     for d in dict:
#         invert_dict.update({dict.get(d) : d})
#     return invert_dict

# print(invert_dict({"a": 1, "b": 2, "c": 3}))
# print(invert_dict({"Jisan": 85, "Rahim": 90}))


"""⚒️ Problem 3: Micro Project – Library System

📌 **Task:**
Create a mini library system using dictionary. Books are keys, availability (`True`/`False`) is value.

👉 Functions:

1. `add_book(book)` → Add a book to library (default available).
2. `borrow_book(book)` → If available, mark as borrowed.
3. `return_book(book)` → Mark as available again.
4. `check_availability(book)` → Return status.

📎 **Example:**

```python
add_book("Python Basics")
borrow_book("Python Basics")  
check_availability("Python Basics") ➞ False  
return_book("Python Basics")  
check_availability("Python Basics") ➞ True
```

🎯 **Focus:** CRUD with dictionaries.
⏱️ **Target Time:** 20 minutes"""

library = {}

def add_book(book):
    library.update({book : True})

def borrow_book(book):
    if book in library:
        library.update({book : False})
    else:
        print(f"{book} Not available!")

def return_book(book):
    if book in library:
        library[book] = True
    else:
        print(f"{book} Not in library!")
        
def check_availability(book):
    if book in library:
        return library.get(book)
    return False

# run function
# add_book("book")
# print(library)
# borrow_book("book")
# borrow_book("bo")
# print(check_availability("book"))
# return_book("book")
# print(library)
# print(check_availability("book"))

# add_book("Python Basics")
# borrow_book("Python Basics")  
# print(check_availability("Python Basics")) #➞ False  
# return_book("Python Basics")  
# print(check_availability("Python Basics")) #➞ True

# print(library)


"""✅ Bonus Challenge (Optional)

📌 **Task:**
Write a function that finds the **second largest number** in a list.

📎 **Example:**

```python
second_largest([10, 20, 4, 45, 99]) ➞ 45  
second_largest([5, 5, 5]) ➞ None
```

💡 **Hint:** Use `set()` to remove duplicates, then sort."""

# def second_largest(lst):
#     unique = list(set(lst))
#     if len(unique) < 2:
#         return None
#     unique.sort()
#     return unique[-2]

# print(second_largest([10, 20, 4, 45, 99]))
# print(second_largest([5, 5, 5]))