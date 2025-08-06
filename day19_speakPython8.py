"""*Day 19 – Speak Python 8**
🧠 Focus Areas:

* List Comprehension
* Loops
* String Formatting
* Conditional Thinking"""

"""*Problem 1: Square the Odds**
📌 **Task:**
Write a function that takes a list of numbers and returns a new list containing the squares of only the *odd* numbers.

📎 **Example:**

```python
square_odds([1, 2, 3, 4, 5]) ➞ [1, 9, 25]  
square_odds([2, 4, 6]) ➞ []
```

💡 **Hint:** Use list comprehension with a condition.
⏱️ **Target Time:** 10 minutes"""

# def square_odds(lst):
#     square_lst = []
#     for n in lst:
#         if n % 2 != 0:
#             square = n**2
#             square_lst.append(square)
#     return square_lst

# print(square_odds([1, 2, 3, 4, 5]))
# print(square_odds([2, 4, 6]))


"""*Problem 2: Title Formatter**
📌 **Task:**
Write a function that takes a name string and returns it in proper title case (each word capitalized).

📎 **Example:**

```python
format_title("hello world") ➞ "Hello World"  
format_title("pYTHON is fun") ➞ "Python Is Fun"
```

🎯 **Focus:** String manipulation
💡 **Hint:** Use `.title()` or split-capitalize-join manually.
⏱️ **Target Time:** 10 minutes"""

# def format_title(s):
#     return s.title()

# print(format_title("jisan js"))
# print(format_title("hello world"))
# print(format_title("pYTHON is fun"))

"""**Problem 3: Micro Project – Word Censor**
📌 **Task:**
Write a function that replaces all occurrences of a “banned” word in a sentence with asterisks (\*\*\*).

📎 **Example:**

```python
censor("I hate bad words", "hate") ➞ "I *** bad words"  
censor("No violence here", "violence") ➞ "No *** here"
```

🎯 **Focus:** Text cleaning
💡 **Hint:** Use `.replace()` for the banned word with `'*' * len(word)`
⏱️ **Target Time:** 15 minutes"""

def censor(s, rep):
    return s.replace(rep, "*"*len(rep))

print(censor("jisan is bad", "bad"))
print(censor("I hate bad words", "hate"))
print(censor("No violence here", "violence"))