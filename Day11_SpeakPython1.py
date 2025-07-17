"""🧠 Day 11 – Speak Python 1"""


"""✅ 1. Problem Solving: Unique Characters Checker

Problem:
Write a function that takes a string and returns True if all characters are unique (no duplicates), otherwise False.

Example:

is_unique("abcde") ➞ True  
is_unique("hello") ➞ False  
is_unique("") ➞ True

⏱️ Time Target: 10 minutes
Focus: Loops, conditionals, string logic"""


"""def is_unique(s):
    for char in s:
        count = s.lower().count(char)
        if count > 1:
            return False
    return True
    
print(is_unique("asdd"))
print(is_unique("abcde"))
print(is_unique("Hello"))
print(is_unique("Llm"))
print(is_unique(""))"""
        


#🐞 2. Bug Fix Challenge: Count Even Numbers

"""def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 1:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 5, 6]))  # ➞ 3 (2, 4, 6)"""



"""⏱️ Time Target: 5-7 minutes
🎯 Focus: Logical bug tracking"""

#Bug is fixed this is tha answer :
"""def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 5, 6]))
print(count_even([9, 8, 4, 3, 6]))"""



"""⚒️ 3. Micro Project Logic: Password Strength Checker

Goal:
Write a function is_strong_password(pwd) that checks:

Length ≥ 8
Has at least 1 digit
Has at least 1 uppercase letter


Example:

is_strong_password("abc123") ➞ False  
is_strong_password("Abc12345") ➞ True

⏱️ Time Target: 15 minutes 
💡 Focus: String traversal, conditionals"""


def is_strong_password(pwd):
    has_digit = False
    has_upper = False
    if len(pwd) < 8:
        return False
    
    for ch in pwd:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
    return has_digit and has_upper

print(is_strong_password("Abc12345"))
print(is_strong_password("abc12345"))
print(is_strong_password("sonnic098"))