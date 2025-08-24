"""🧠 **Day 25 – Speak Python 14**

### **Phase 3: Recursion & Thinking in Steps**

**Focus Areas:**

* Introduction to Recursion
* Factorial & Fibonacci
* Sum & Reverse with Recursion
* Mini Project with Recursion"""

"""✅ Problem 1: Factorial with Recursion

📌 **Task:**
Write a function to calculate factorial of a number using recursion.

📎 **Example:**

```python
factorial(5) ➞ 120  
factorial(0) ➞ 1```

💡 **Hint:**
`n! = n \* (n-1)!` with base case `factorial(0) = 1`.
"""

# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n-1) * n

# print(factorial(0))
# print(factorial(5))


"""✅ Problem 2: Fibonacci with Recursion

📌 **Task:**
Write a recursive function to get the nth Fibonacci number.

📎 **Example:**

```python
fibonacci(5) ➞ 5  
fibonacci(7) ➞ 13
```

💡 **Hint:**
`fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)` with base cases `fibonacci(0)=0`, `fibonacci(1)=1`."""

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))
# print(fibonacci(7))
# print(fibonacci(13))

# for n in range(1, 10+1):
#     print(fibonacci(n))


"""✅ Problem 3: Recursive Sum of List

📌 **Task:**
Write a recursive function that returns the sum of all numbers in a list.

📎 **Example:**

```python
recursive\_sum(\[1, 2, 3, 4]) ➞ 10  
recursive\_sum(\[5, 10, 15]) ➞ 30```
"""

# def recursive_sum(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] + recursive_sum(lst[1:])

# print(recursive_sum([1, 2, 3, 4]))
# print(recursive_sum([5, 10, 15]))


"""✅ Problem 4: Reverse String with Recursion

📌 **Task:**
Write a recursive function that reverses a string.

📎 **Example:**

```python
reverse\_string("python") ➞ "nohtyp"  
reverse\_string("Jisan") ➞ "nasiJ"
```
"""

# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]

# print(reverse_string("python"))
# print(reverse_string("Jisan"))

"""⚒️ Micro Project – Recursive Directory Printer

📌 **Task:**
Simulate printing files/folders in a nested structure using recursion.

📎 **Example:**

```python

files = {
    "root": {
        "file1.txt": None,
        "docs": {
            "resume.docx": None,
            "notes.txt": None
        }
    }
}

```

👉 Write a function `print\_files(files, indent=0)` that prints the structure like:

```

root
  file1.txt
  docs
    resume.docx
    notes.txt

```
"""

files = {
    "root": {
        "file1.txt": None,
        "docs": {
            "resume.docx": None,
            "notes.txt": None
        }
    }
}

files2 = {
    "root": {
        "file1.txt": None,
        "docs": {
            "resume.docx": None,
            "notes.txt": None,
            "text": {
                "hello.txt": None,
                "welcome.txt": None
            }
        }
    }
}

def print_files(files, indent=0):
    for name, content in files.items():
        print(" " * indent + name)
        if isinstance(content, dict):
            print_files(content, indent+1)

print_files(files)
print_files(files2)