"""Day 16 – Speak Python 5

👉 Focus:

    String filtering
    Bug fixing (logical error)
    Micro project using string + list logic"""




"""✅ Problem 1: Remove Vowels from String

📌 Problem:
Write a function that takes a string and returns a new string with all vowels (a, e, i, o, u) removed.

📎 Example:

remove_vowels("Hello World") ➞ "Hll Wrld"  
remove_vowels("Python is cool") ➞ "Pythn s cl"

💡 Hint: Use a loop and if to skip vowels.

⏱️ Target Time: 10 minutes"""

"""def remove_vowels(word):
    
    vowels = ["a", "e", "i", "o", "u"]
    vowels_rm = ""
    
    for char in word.lower():
        if char in vowels:
            continue
        else:
            vowels_rm += char
        
    return vowels_rm
    
vowels = "aAeEiIojOuU"

print(remove_vowels(vowels))
print(remove_vowels("Hello World"))
print(remove_vowels("Python is cool"))"""

"""🐞 Problem 2: Bug Fix – Sum Positive Numbers

📌 Bugged Code:"""

"""def sum_positive(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
        else:
            total = 0
    return total

print(sum_positive([1, -2, 3, 4]))  # ➞ 8"""

"""🔍 Your Task:
Fix the bug so it correctly sums only the positive numbers without resetting the total.

🎯 Focus: Bug fixing with logic understanding
⏱️ Target Time: 7 minutes"""

#fixed code:
"""def sum_positive(nums):
    total = 0
    for n in nums:
        if n < 0:
            continue 
        else:
            total += n
    return total

print(sum_positive([1, -2, 3, 4]))
print(sum_positive([1, -2, 80, -9, -6, 0, -9, 3, 4]))"""



"""⚒️ Problem 3: Micro Project – Extract Numbers from Text

📌 Problem:
Write a function that extracts all digits from a string and returns them as a list of integers.

📎 Example:

extract_numbers("I have 2 apples and 3 bananas.") ➞ [2, 3]  
extract_numbers("No numbers here!") ➞ []

💡 Hint: Use isdigit() inside a loop. Combine with list.

⏱️ Target Time: 15 minutes"""


"""def extract_numbers(s):
    num = []
    for char in s:
        if char.isdigit():
            num.append(int(char))
    return num

print(extract_numbers("I have 2 apples and 3 bananas."))
print(extract_numbers("No numbers here!"))"""