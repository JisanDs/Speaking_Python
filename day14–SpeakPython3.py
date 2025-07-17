""" Day 14 – Speak Python 3

👉 Focus:

String analysis
Simple debugging
Project-style logic building"""




"""✅ Problem 1: Count Digits in a String

📌 Problem:
Write a function that takes a string and returns how many digits (0–9) it contains.

📎 Example:

count_digits("abc123") ➞ 3  
count_digits("no digits") ➞ 0  
count_digits("2024 is near") ➞ 4

⏱️ Target Time: 10 minutes"""


"""def count_digits(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count

s = "abc123"
print(count_digits(s))
print(count_digits("no digits"))
print(count_digits("2024 is near"))"""


"""🐞 Problem 2: Bug Fix – Find Max in List

📌 Bugged Code:"""

"""def find_max(lst):
    max = lst[0]
    for num in lst:
        if num > max:
            max = num
    return max

print(find_max([-1, -2, -3]))  # ➞ -1"""

"""🔍 Your Task:
Fix the bug so it correctly returns the max even for negative numbers.

🎯 Focus: Logical bug understanding
⏱️ Target Time: 7 minutes"""

# Bug fixed code:
"""def find_max(lst):
    max = lst[0]
    for num in lst:
        if num > max:
            max = num
    return max

print(find_max([-1, -2, -3]))
print(find_max([1, 2, 3]))"""



"""⚒️ Problem 3: Micro Project – Remove Duplicates from List

📌 Problem:
Write a function that removes duplicates from a list and returns a new list with only unique elements (order preserved).

📎 Example:

remove_duplicates([1, 2, 2, 3, 4, 4, 4]) ➞ [1, 2, 3, 4]  
remove_duplicates(["a", "b", "a", "c"]) ➞ ["a", "b", "c"]

💡 Hint: Use a loop and a helper list to check if an item is already added.
⏱️ Target Time: 15 minutes"""

"""def remove_duplicates(lst):
    dup_rm = []
    for i in lst:
        if i in dup_rm:
            continue
        else:
            dup_rm.append(i)
    return dup_rm

print(remove_duplicates( [1, 2, 2, 3, 4, 4, 4]))
print(remove_duplicates( ["a", "b", "a", "c"]))"""