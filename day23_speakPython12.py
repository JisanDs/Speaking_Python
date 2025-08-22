"""🧠 **Day 23 – Speak Python 12**

👉 **Phase 1: Data Structure Boost**

আজকের ফোকাস:

* Sorting & Searching
* Nested Dictionary & List
* Dictionary + Set Combo
* Micro Project"""


"""✅ Problem 1: Find Maximum & Minimum in a List

📌 **Task:**
Write a function that takes a list of numbers and returns both the maximum and minimum.

📎 **Example:**

```python
find_max_min([3, 7, 1, 9, 2]) ➞ (9, 1)
find_max_min([-5, 10, 0]) ➞ (10, -5)
```

💡 **Hint:** Use `max()` and `min()` or manual loop.
"""
def find_max_min(lst):
    return (max(lst), min(lst))

print(find_max_min([3, 7, 1, 9, 2]))
print(find_max_min([-5, 10, 0]))


"""✅ Problem 2: Count Occurrences of Each Number

📌 **Task:**
Write a function that counts how many times each number appears in a list.

📎 **Example:**

```python
count_occurrences([1, 2, 2, 3, 1, 4, 2])  
➞ {1: 2, 2: 3, 3: 1, 4: 1}
```

💡 **Hint:** Use dictionary to store counts."""

def count_occurrences(lst):
    frq = {}
    for n in lst:
        frq[n] = frq.get(n, 0) + 1
    return frq

print(count_occurrences([1, 2, 2, 3, 1, 4, 2]))
print(count_occurrences([81, 82, 72, 3, 81, 44, 82]))


"""✅ Problem 3: Nested Dictionary – Student Records

📌 **Task:**
You have student data stored in a nested dictionary like this:

```python
students = {
    "Jisan": {"math": 85, "english": 78},
    "Rahim": {"math": 90, "english": 82},
}
```

👉 Write a function `get_score(name, subject)` that returns the score of the student in that subject.

📎 **Example:**

```python
get_score("Jisan", "math") ➞ 85  
get_score("Rahim", "english") ➞ 82  
get_score("Hasan", "math") ➞ "Not Found"
```
"""

students = {
    "Jisan": {"math": 85, "english": 78},
    "Rahim": {"math": 90, "english": 82},
}

def get_score(name, subject):
    if name in students:
        return students[name].get(subject, "Not Found")
    return "Not Found"

print(get_score("Jisan", "math"))
print(get_score("Rahim", "english"))
print(get_score("Hasan", "math"))

"""✅ Problem 4: Set + Dictionary Combo – Unique Words Counter

📌 **Task:**
Write a function that counts how many **unique words** are in a given sentence.

📎 **Example:**

```python
unique_word_count("I love Python because I love coding")  
➞ {'I': 1, 'love': 2, 'Python': 1, 'because': 1, 'coding': 1}
```

💡 **Hint:** Split sentence → use set to find uniques → dictionary to count."""

def unique_word_count(s):
    words = s.split(" ")
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    return count

print(unique_word_count("I love Python because I love coding"))


"""⚒️ **Micro Project – To-Do List Manager (Data Structure Version)**

📌 **Task:**
Build a simple **To-Do List Manager** where tasks are stored in a list/dictionary.

👉 Functions:

1. `add_task(task)` → Add a task
2. `remove_task(task)` → Remove a task
3. `view_tasks()` → Show all tasks

📎 **Example:**

```python
add_task("Study Python")  
add_task("Do Homework")  
view_tasks() ➞ ["Study Python", "Do Homework"]  
remove_task("Do Homework")  
view_tasks() ➞ ["Study Python"]
```

🎯 **Focus:** CRUD idea with list/dictionary"""

To_Do = []

def add_task(task):
    To_Do.append(task)

def remove_task(task):
    if task in To_Do:
        To_Do.remove(task)
    else:
        print("Not found!")

def view_tasks():
    return To_Do

# test
add_task("Study Python")  
add_task("Do Homework")  
print(view_tasks())
remove_task("Do Homework")  
print(view_tasks())