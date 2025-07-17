#Day 12 – Speak Python 2

"""✅ Problem 1: Double Characters

Problem:
Write a function that takes a string and returns a new string where each character is repeated twice.

Example:

double_char("hello") ➞ "hheelllloo"
double_char("abc") ➞ "aabbcc"""

"""def double_char(s):
    double = ""
    for i in range(len(s)):
        double += (s[i] + s[i])
    return double

print(double_char("hello"))
print(double_char("abc"))"""

# short and more pythonic code
"""def double_chr(s):
    return "".join(c*2 for c in s)
    
print(double_chr("jisan"))"""

"""🐞 Problem 2: Bug Fix – Average Calculator

Bugged Code:"""

"""def average(nums):
    total = 0
    for num in nums:
        total += num
    return total

print(average([2, 4, 6]))  # ➞ 4.0"""

"""Your Task:
Fix the bug in the function so that it correctly returns the average of the numbers in the list.

Expected Output:

average([2, 4, 6]) ➞ 4.0"""

#fixed code:
def average(nums):
    total = 0
    avg = 0
    for num in nums:
        total += num
    avg = total / len(nums)
    return avg

print(average([2, 4, 6]))


"""⚒️ Problem 3: Micro Project – Palindrome Checker

Goal:
Write a function is_palindrome() that checks whether a given word or sentence is a palindrome.

> A palindrome is a word that reads the same forward and backward.



Example:

is_palindrome("madam") ➞ True  
is_palindrome("racecar") ➞ True  
is_palindrome("hello") ➞ False

Bonus:
Make it ignore spaces and capitalization:

is_palindrome("A man a plan a canal Panama") ➞ True"""

"""def is_palindrome(s):
    rm_sp = ""
    for i in range(len(s)):
        if s.lower()[i].isspace():
            continue
        else:
            rm_sp += s.lower()[i]
    s = rm_sp
    rev = s[::-1]
    return s == rev

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("madma"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("abcba"))"""