"""🧠 **Day 28 – Speak Python 17**

### **Phase 6: Balanced Learning (Recursion + Core Topics)**

**Focus Areas:**

* Recursion practice
* Core Python concepts (OOP, File Handling, etc.)
* Debugging real problems
* Mini Project for fun 🚀"""

"""✅ Problem 1: Recursion – Print Numbers (1 to n)

📌 **Task:**
Write a recursive function that prints numbers from 1 to `n`.

📎 Example:

```python
print\_numbers(5)
\# Output: 1 2 3 4 5
```

💡 **Hint:**
Print smaller first, then current number."""

def print_numbers(n):
    if n == 0:
        return 
    print_numbers(n-1)
    print(n)

print_numbers(5)


"""✅ Problem 2: Recursion – Sum of Even Numbers

📌 **Task:**
Write a recursive function that calculates the sum of even numbers up to `n`.

📎 Example:

```python
sum\_even(6) ➞ 12   # (2+4+6)
```

💡 **Hint:**
Check if `n` is even → add, otherwise skip.
"""

def sum_even(n):
    if n == 0:
        return 0
    even = n if n % 2 == 0 else 0
    return even + sum_even(n-1)

print(sum_even(6))
print(sum_even(10))


"""✅ Problem 3: OOP – Student Class

📌 Task:
Create a Student class with attributes: name, age, grade.
Add a method display_info() to print details.

📎 Example:

s1 = Student("Jisan", 20, "A")
s1.display_info()
# Output: Name: Jisan, Age: 20, Grade: A"""

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

s1 = Student("Jisan", 20, "A")
s2 = Student("Robart", 45, "A")

s1.display_info()
s2.display_info()


"""✅ Problem 4: File Handling – Word Counter

📌 Task:
Write a program that opens a text file sample.txt, counts total words, and prints the result.

📎 Example:

sample.txt → "Python is fun and powerful"
Output: Total words = 5"""

with open("sample.txt", "w") as f:
    f.write("Python is fun and powerful")

with open("sample.txt", "r") as f:
    data = f.read()
    word_count = len(data.split())
    print(f"Total words = {word_count}")


"""⚒️ Mini Project – Simple Calculator (OOP Version)

📌 Task:
Make a Calculator class with methods: add, subtract, multiply, divide.
Create an object and test all operations.

📎 Example:

calc = Calculator()
print(calc.add(5, 3))      # 8
print(calc.multiply(4, 2)) # 8"""

class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("ZeroDivitionError")
    
    
calc = Calculator()

print(calc.add(5, 3))
print(calc.multiply(4, 2))
print(calc.subtract(45, 23))
print(calc.divide(89, 8))


"""🐞 Debugging Task – Fix the Code

❌ Wrong Code:

def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n-1)

print(factorial(5))


✅ Expected Output: 120"""

# ✅ Fixed Code:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(7))