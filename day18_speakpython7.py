### 🧠 **Day 18 – Speak Python 7**

"""👉 **Focus Areas:**

* String Manipulation
* Conditionals
* Function Design
* Creative Thinking"""



"""✅ **Problem 1: Vowel Counter**

📌 **Task:**
Write a function that counts the number of vowels (`a`, `e`, `i`, `o`, `u`) in a given string.

📎 **Example:**

```python
count_vowels("Hello World") ➞ 3
count_vowels("Python") ➞ 1
```

💡 **Hint:** Convert to lowercase and loop through characters.
⏱️ **Target Time:** 10 minutes"""

def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("Jisan"))
print(count_vowels("Hello World"))
print(count_vowels("Python"))


"""🧪 **Problem 2: Even or Odd Digits**

📌 **Task:**
Write a function that takes a number and returns how many even and odd digits it has.

📎 **Example:**

```python
digit_parity(123456) ➞ (3, 3)  # 3 even, 3 odd
digit_parity(24680) ➞ (5, 0)
```

🎯 **Focus:** String-number conversion, conditionals
💡 **Hint:** Use `str()` to iterate digits.
⏱️ **Target Time:** 12 minutes"""


def digit_parity(digits):
    even = 0
    odd = 0
    for n in str(digits):
        if int(n) % 2 == 0:
            even += 1
        else:
            odd += 1
    return f"{even} even, {odd} odd"

print(digit_parity(123456))
print(digit_parity(24680))
print(digit_parity(123456988878788))


"""🧠 **Problem 3: Micro Project – Word Replacer**

📌 **Task:**
Write a function that replaces a word in a sentence with another word.

📎 **Example:**

```python
replace_word("I love apples", "apples", "oranges") ➞ "I love oranges"
``` 

# 🎯 **Focus:** String manipulation with `.replace()`
# 💡 **Hint:** The method `.replace(old, new)` is your friend.
# ⏱️ **Target Time:** 15 minutes"""

def replace_word(word, old, new):
    return word.replace(old, new)

print(replace_word("I love apples", "apples", "banana"))