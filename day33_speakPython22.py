"""🧠 Day 33 – Speak Python 22
Phase 6: Balanced Learning (Recursion + Data Structures + OOP + Debugging + Mini Project)"""


"""✅ Problem Set
🔁 Recursion (2 problems)

Fibonacci (Recursive with Memoization)
Write a recursive function to generate Fibonacci numbers using memoization (dictionary caching) to optimize performance.

Input: fib(10) → Output: 55"""

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(10))


"""String Reversal (Recursive)
Write a recursive function that reverses a string.

Input: "python" → Output: "nohtyp" """

# def revers_string(s):
#     if len(s) == 0:
#         return s
#     return revers_string(s[1:]) + s[0]

# print(revers_string("Jisan"))
# print(revers_string("python"))


"""⚡ Other Concepts (2 problems)

Set Operations
Create two sets and perform: union, intersection, and difference. Print the results."""
# test1 = {3, 4, 5, 6}
# test2 = {9, 8, 7, 6, 4}

# def main():
#     print(f"union: {set_union(test1, test2)}")
#     print(f"intersection : {set_inter(test1, test2)}")
#     print(f"difference:  {set_diff(test1,test2)}")


# def set_union(set1, set2):
#     return set1.union(set2)

# def set_inter(set1, set2):
#     return set1.intersection(set2)

# def set_diff(set1, set2):
#     return set1.difference(set2)

# main()


"""List Comprehension with Condition
From a list of numbers, create a new list that contains only the numbers divisible by 3.

# Input: [1,2,3,4,5,6,7,8,9] → Output: [3,6,9]"""

# nums = [1,2,3,4,5,6,7,8,9]

# div_3 = [n for n in nums if n % 3 == 0]
# print(div_3)


"""🛠️ Debugging Task

OOP Inheritance Bug
The following code has a bug in inheritance. Fix it.
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed

d = Dog("Tommy", "German Shepherd")
print(d.name, d.breed)  # Expected: Tommy German Shepherd """

# fixed code:
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Tommy", "German Shepherd")
print(d.name, d.breed)