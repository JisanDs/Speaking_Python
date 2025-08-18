""" 🧠 **Day 20 – Speak Python 9**

### 👉 Focus Areas:

* List Methods
* String Cleaning
* Logic Building
* Beginner-Friendly Micro Projects"""



""" ✅ **Problem 1: Remove Duplicates from List**

📌 **Task:**
Write a function that removes duplicates from a list and returns the unique elements in the same order as they first appeared.

📎 **Example:**

```python
remove_duplicates([1, 2, 2, 3, 4, 4, 5]) ➞ [1, 2, 3, 4, 5]
remove_duplicates(["apple", "banana", "apple"]) ➞ ["apple", "banana"]
```

💡 **Hint:** Use a `set()` to track seen items.
⏱️ **Target Time:** 10 minutes"""

# def remove_duplicates(lst):
#     return list(set(lst))

# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5, 1, 2, 2, 3, 4, 4, 5]))
# print(remove_duplicates(["apple", "banana", "apple"]))



""" 🧪 **Problem 2: Clean Up String**

📌 **Task:**
Write a function that removes punctuation (like `.`, `,`, `!`, `?`) from a sentence.

📎 **Example:**

```python
clean_text("Hello, world!") ➞ "Hello world"
clean_text("Python is fun!!!") ➞ "Python is fun"
```

🎯 **Focus:** String filtering, loops
💡 **Hint:** Use `string.punctuation` from the `string` module.
⏱️ **Target Time:** 12 minutes"""

# def clean_text(s):
#     puns = [".", ",", "!", "?"]
#     rm_pun = ""
#     for char in s:
#         if char not in puns:
#             rm_pun += char
#     return rm_pun

# print(clean_text("Hello, world!"))
# print(clean_text("Python is fun!!!"))




""" ⚒️ **Problem 3: Micro Project – Shopping List Builder**

📌 **Task:**
Create a function that takes input as a comma-separated string (e.g., `"milk, eggs, bread, milk"`) and returns a cleaned shopping list (unique items, capitalized, no spaces).

📎 **Example:**

```python
build_shopping_list("milk, eggs, bread, milk") ➞ ['Milk', 'Eggs', 'Bread']
```

🎯 **Focus:** String splitting, formatting, list building
💡 **Hint:** Use `.split(',')`, `.strip()`, `.capitalize()`
⏱️ **Target Time:** 15 minutes"""

# def build_shopping_list(s):
#     split_s = s.split(",")
#     lst = []
#     for s in split_s:
#         lst.append(s.strip().capitalize())
#     return list(set(lst))

# print(build_shopping_list("milk, eggs, bread, milk"))
# print(build_shopping_list("milk, eggs, eggs, bread, eggs, milk"))

""" ✅ Bonus Idea (Optional):

**📌 Task:** Write a function that counts how many unique vowels are used in a word.

📎 **Example:**

python
unique_vowel_count("education") ➞ 5
unique_vowel_count("sky") ➞ 0"""

# def unique_vowel_count(word):
#     vowels = ["a", "e", "i", "o", "u"]
#     count = 0
#     for char in word:
#         if char in vowels:
#             count += 1
#     return count

# print(unique_vowel_count("education"))
# print(unique_vowel_count("sky"))