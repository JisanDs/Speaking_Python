"""🧠 **Day 24 – Speak Python 13**

👉 **Phase 2: Data Structure Pro Pack**

**Focus Areas:**

* Custom Sorting
* Searching Algorithms
* Nested List + Dictionary Combo
* Micro Project (Leaderboard style)
"""

"""✅ Problem 1: Sort Students by Score

📌 **Task:**
You are given a list of students where each student is represented as a tuple `(name, score)`.
Write a function that sorts the students by their score in **descending order**.

📎 **Example:**

```python
students = [("Jisan", 85), ("Rahim", 92), ("Karim", 78)]

sort_students(students)  
➞ [("Rahim", 92), ("Jisan", 85), ("Karim", 78)]
```

💡 **Hint:** Use `sorted(list, key=..., reverse=True)`."""

def sort_students(students):
    return sorted(students, key=lambda x: x[1], reverse=True)

students = [("Jisan", 85), ("Rahim", 92), ("Karim", 78)]
print(sort_students(students))


"""✅ Problem 2: Linear Search

📌 **Task:**
Write a function that searches for a number in a list and returns its index if found, otherwise return `-1`.

📎 **Example:**

```python
linear_search([10, 20, 30, 40], 30) ➞ 2  
linear_search([5, 6, 7], 10) ➞ -1
```

💡 **Hint:** Use a loop with index check.
"""

def linear_search(lst, n):
    for i, item in enumerate(lst):
        if item == n:
            return i
    return -1

print(linear_search([10, 20, 30, 40], 30))
print(linear_search([10, 20, 30, 40], 40))
print(linear_search([5, 6, 7], 10))


"""✅ Problem 3: Nested Data – Employee Manager

📌 **Task:**
You have employee data stored in a nested dictionary:

```python
employees = {
    "101": {"name": "Jisan", "role": "Developer", "salary": 50000},
    "102": {"name": "Rahim", "role": "Designer", "salary": 40000},
}
```

👉 Write a function `get_employee(emp_id, field)` that returns employee information.

📎 **Example:**

```python
get_employee("101", "name") ➞ "Jisan"
get_employee("102", "salary") ➞ 40000
get_employee("103", "role") ➞ "Not Found"
"""

employees = {
    "101": {"name": "Jisan", "role": "Developer", "salary": 50000},
    "102": {"name": "Rahim", "role": "Designer", "salary": 40000},
}

def get_employee(emp_id, field):
    if emp_id in employees:
        return employees[emp_id].get(field, "Not Found")
    return "Not Found"
    
print(get_employee("101", "name"))
print(get_employee("102", "salary"))
print(get_employee("103", "role"))


"""⚒️ Micro Project – Leaderboard System

📌 **Task:**
Build a simple leaderboard using dictionary/list.

👉 Functions:

1. `add_player(name, score)` → Add a new player.
2. `update_score(name, score)` → Update an existing player’s score.
3. `top_players(n)` → Return the top **N** players sorted by score.

📎 **Example:**

```python
add_player("Jisan", 85)
add_player("Rahim", 95)
add_player("Karim", 70)

top_players(2) ➞ [("Rahim", 95), ("Jisan", 85)]"""
leaderboard = []

def add_player(name, score):
    leaderboard.append((name, score))

def top_players(n):
    return sorted(leaderboard, key=lambda x: x[1], reverse=True)[:n]

def update_score(name, score):
    global leaderboard
    leaderboard = [(n, s) if n != name else (name, score) for (n, s) in leaderboard]

def remove_player(name):
    for (n, s) in leaderboard:
        if n == name:
            leaderboard.remove((n, s))


add_player("Jisan", 85)
add_player("Rahim", 95)
add_player("Karim", 70)
print(leaderboard)
print(top_players(1))
update_score("Karim", 99)
print(leaderboard)
print(top_players(2))
remove_player("Karim")
print(leaderboard)