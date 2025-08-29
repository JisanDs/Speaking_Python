"""🧠 **Day 29 – Speak Python 18**

### **Phase 6: Balanced Learning (Recursion + Core Topics)**

**Focus Areas:**

* Recursion practice
* Core Python concepts (OOP, File Handling, etc.)
* Debugging real problems
* Mini Project for fun 🚀"""

"""### ✅ Problem 1: Recursion – Factorial Sum

📌 **Task:**
Write a recursive function that calculates the sum of factorials from 1 to `n`.

📎 Example:

```
factorial_sum(3) ➞ 1! + 2! + 3! = 9  
factorial_sum(4) ➞ 33
```

💡 **Hint:**
Use a helper factorial function + recursion."""

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# def factorial_sum(n):
#     if n == 1:
#         return 1
#     return factorial(n) + factorial_sum(n-1)

# print(factorial_sum(3))
# print(factorial_sum(4))


"""✅ Problem 2: Recursion – Reverse String

📌 **Task:**
Reverse a string using recursion.

📎 Example:

```
reverse_string("hello") ➞ "olleh"
```

💡 **Hint:**
Last char + reverse(rest)."""

# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]

# print(reverse_string("Jisan"))
# print(reverse_string("hello"))


"""✅ Problem 3: OOP – Bank Account Class

📌 **Task:**
Create a `BankAccount` class with:

* `deposit(amount)`
* `withdraw(amount)`
* `get_balance()`

📎 Example:

```python
acc = BankAccount(1000)
acc.deposit(500)   # Balance = 1500
acc.withdraw(200)  # Balance = 1300"""

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Invalid Amount")
    
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#         else:
#             print("Incorrect Amount")


# acc = BankAccount(1000)
# acc.deposit(500) 
# print(acc.balance)  # Balance = 1500
# acc.withdraw(200)  # Balance = 1300
# print(acc.balance)


"""✅ Problem 4: File Handling – Line Counter

📌 **Task:**
Write a program to count how many lines are in a file `sample.txt`.

📎 Example:

```
sample.txt → 
Python
is
fun

Output: 3 lines"""

# with open("sample.txt", "w") as f:
#     f.write("Python\nis\nfun")

# with open("sample.txt", "r") as f:
#     data = f.readlines()

# print(f"Output: {len(data)} lines")


"""⚒️ Mini Project – To-Do List Manager (File + OOP)

📌 **Task:**
Make a `Todo` class where you can add tasks, view tasks, and save them to a file.

📎 Example:

```python
todo = Todo()
todo.add("Learn Python")
todo.add("Build Project")
todo.show()"""

# class Todo:
#     todo = []

#     def add(self, task):
#         self.todo.append(task)

#     def show(self):
#         tasks = self.todo
#         for n, task in enumerate(tasks,start=1):
#             print(n, task)

# todo = Todo()
# todo.add("Learn Python")
# todo.add("Build Project")
# todo.show()


"""🐞 Debugging Task – Fix the Code

❌ Wrong Code:

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return 0   # ❌ Wrong for n=1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
```

✅ Expected Output:

fibonacci(5) ➞ 5"""

# ✅fixed code:

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))