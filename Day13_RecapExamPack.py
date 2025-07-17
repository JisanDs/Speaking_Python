#✅ Day 13 – Recap Exam Pack

"""Focus:

1. Loops
2. Strings & Lists
3. Logic & Conditionals
4. Debugging


⏱️ Time Target: 45–60 minutes (Full Set)"""


"""🔶 1. Count Uppercase Letters

Write a function that counts how many uppercase letters are in a string.
Example:

count_upper("Hello World") ➞ 2  
count_upper("python") ➞ 0"""

"""def count_upper(s):
    count_upper = 0
    for i in range(len(s)):
        if s[i].isupper():
            count_upper += 1
    return count_upper
    
s = "So J Sjjs jJ"
print(count_upper(s))
print(count_upper("Hello World"))
print(count_upper("python"))"""

"""🔶 2. Remove Vowels

Remove all vowels (a, e, i, o, u) from a string and return the result.
Example:

remove_vowels("hello") ➞ "hll"  
remove_vowels("Python is Fun") ➞ "Pythn s Fn"""

"""def remove_vowels(s):
    rm_vowels = ""
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(s)):
        if s[i].lower() in vowels:
            continue
        else:
            rm_vowels += s[i]
    return rm_vowels
    
s = "soOnniIc"
print(remove_vowels(s))
print(remove_vowels("hello"))
print(remove_vowels("Python is Fun"))"""

"""🔶 3. Bug Fix: Reverse List

def reverse_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[-i]
    return lst

print(reverse_list([1, 2, 3, 4]))  # ➞ [4, 3, 2, 1]"""

#Bug fixed code:
"""def reverse_list(lst):
    rev_lst = []
    for i in range(len(lst)-1, -1, -1):
        rev_lst.append(lst[i])
    return rev_lst

print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c", "d"]))"""

"""🔶 4. Check for Prime Number

Write a function that returns True if a number is prime, else False.
Example:

is_prime(7) ➞ True  
is_prime(10) ➞ False"""

#sonnic(chat gpt) code:
"""def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(18))  # False"""

#my code with optmize
"""def is_prime(n):
   if n <= 1:
       return False
   for i in range(2, n):
       if n % i == 0:
           return False
   return True
   
print(is_prime(18))
print(is_prime(17))"""

"""🔶 5. Repeat Last Character n Times

Write a function that repeats the last character of a string n times.
Example:

repeat_last("hello", 3) ➞ "hellooo"  
repeat_last("sonnic", 2) ➞ "sonniccc"""

def repeat_last(s, n):
    return s[0:-1] + (s[-1]*n)

print(repeat_last("jisan", 3))
print(repeat_last("hello", 3))
print(repeat_last("sonnic", 2))