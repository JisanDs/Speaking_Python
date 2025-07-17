#Day 15 – Speak Python 4: Pattern Practice + Mini Challenges

    #Loop mastery
    #Print-based logic
    #Pattern & mini code writing




"""✅ Problem 1: Right-Angled Triangle Pattern

📌 Problem:
Write a function that prints a right-angled triangle using * of height n.

📎 Example:

triangle(4)

Output:
*
**
***
****

⏱️ Time Target: 7 minutes"""

"""def triangle(n):
    for i in range(1, n+1):
        print(i*"*")
        
triangle(5)
triangle(10)
triangle(30)"""

"""def counter_angle(n):
    for i in range(n, -1, -1):
        print(i*"*")

counter_angle(30)
counter_angle(10)
counter_angle(5)"""


"""🐞 Problem 2: Bug Fix – Square Sum

📌 Bugged Code:"""

"""def square_sum(numbers):
    for num in numbers:
        total = 0
        total += num ** 2
    return total

print(square_sum([1, 2, 3]))  # ➞ 14"""

"""🔍 Your Task:
Fix the bug so it returns the correct sum of squares of the numbers.

⏱️ Time Target: 5 minutes"""

#fixed code:
"""def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

print(square_sum([1, 2, 3]))"""

"""⚒️ Problem 3: Micro Project – Letter Counter

📌 Goal:
Write a function letter_counter(text) that counts how many times each letter appears (ignore spaces, count case-insensitively).

📎 Example:

letter_counter("Hello") ➞ {'h': 1, 'e': 1, 'l': 2, 'o': 1}
letter_counter("A b a") ➞ {'a': 2, 'b': 1}

💡 Hint: Use a dictionary
⏱️ Target Time: 15 minutes"""

"""def letter_counter(s):
    s = s.lower()
    dict = {}
    for char in s.lower():
        if char.isspace():
            continue
        else:
            count = s.count(char)
            dict.update({char : count})
    return dict

print(letter_counter("i    Llm Ai Ds Desine"))
print(letter_counter("A b c"))
print(letter_counter("hello"))"""