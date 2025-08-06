"""Day 17 – Speak Python 6

👉 Focus:

    Conditionals Practice
    Logical Thinking
    String/Number Conversion
    Mini Project Practice"""



"""✅ Problem 1: Armstrong Number Checker

📌 Problem:
Write a function that checks whether a number is an Armstrong number.
An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits.

📎 Example:

armstrong_check(153) ➞ True  
(1³ + 5³ + 3³ = 153)

armstrong_check(123) ➞ False

💡 Hint: Use str() to get digits, then ** for power.
⏱️ Target Time: 10 minutes"""

"""def armstrong_check(digits):
    sum = 0
    for n in str(digits):
        power = int(n) ** len(str(digits))
        sum += power
    return sum == digits
    
print(armstrong_check(234))
print(armstrong_check(153))
print(armstrong_check(12))"""



"""🐞 Problem 2: Bug Fix – Reverse Words

📌 Bugged Code:"""
"""def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return words.join(" ")

print(reverse_words("Python is awesome"))  # ➞ "awesome is Python"""

#Bugfixed code:
    
"""def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

print(reverse_words("Python is awesome"))  # ➞ "awesome is Python"""


"""🔍 Your Task:
Fix the bug so it correctly returns the reversed sentence.

🎯 Focus: String + list method bug fixing
⏱️ Target Time: 7 minutes"""



"""⚒️ Problem 3: Micro Project – Word Frequency Counter

📌 Problem:
Write a function that counts how many times each word appears in a sentence and returns a dictionary.

📎 Example:

count_words("apple banana apple orange banana apple")  
➞ {'apple': 3, 'banana': 2, 'orange': 1}

💡 Hint: Use .split() and dictionary.
⏱️ Target Time: 15 minutes"""

"""def count_words(s):
    words = s.split(" ")
    dict = {}
    for word in words:
        count = words.count(word)
        dict.update({word : count})
    return dict

print(count_words( "apple banana apple orange banana apple"))"""