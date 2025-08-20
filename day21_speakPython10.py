""" 🧠 Day 21 – Speak Python 10

👉 Focus Areas:

* Dictionaries
* Nested Data
* Problem Solving with Keys & Values
* Micro Project using Dictionary"""



"""✅ **Problem 1: Word Frequency Counter**

📌 **Task:**
Write a function that counts how many times each word appears in a given sentence.

📎 **Example:**

```python
word_frequency("I love python because I love coding")
➞ {'I': 2, 'love': 2, 'python': 1, 'because': 1, 'coding': 1}
```

💡 **Hint:** Split the string and use a dictionary to count.
⏱️ **Target Time:** 12 minutes"""

# def word_frequency(s):
#     words = s.split(" ")
#     frq ={}
#     for w in words:
#         count = words.count(w)
#         frq.update({w: count})
#     return frq

# print(word_frequency("I love python because I love coding"))
# print(word_frequency("My name is Jisan"))

"""🧪 **Problem 2: Student Grade Finder**

📌 **Task:**
You have a dictionary of students and their grades. Write a function that takes a student's name and returns their grade. If the student does not exist, return `"Not Found"`.

📎 **Example:**

```python
grades = {"Jisan": 85, "Rahim": 90, "Karim": 78}

find_grade("Rahim", grades) ➞ 90  
find_grade("Hasan", grades) ➞ "Not Found"
```

🎯 **Focus:** Dictionary lookup, error handling
⏱️ **Target Time:** 10 minutes"""
grades = {"Jisan": 85, "Rahim": 90, "Karim": 78}

# def find_grade(name, grades):
#     if name in grades:
#         return grades.get(name)
#     else:
#         return "Not Found"
# print(find_grade("Rahim", grades))
# print(find_grade("Hasan", grades))


"""⚒️ **Problem 3: Micro Project – Contact Book**

📌 **Task:**
Build a simple contact book using a dictionary where keys are names and values are phone numbers. Implement functions to:

1. Add a contact
2. Search a contact
3. Delete a contact

📎 **Example:**

```python
contacts = {}
add_contact("Jisan", "12345")
add_contact("Rahim", "67890")
search_contact("Rahim") ➞ "67890"
delete_contact("Rahim")
search_contact("Rahim") ➞ "Not Found"
```

🎯 **Focus:** Dictionary operations, functions, CRUD idea
⏱️ **Target Time:** 20 minutes"""

# contacts = {}

# def add_contact(name, number):
#     contacts.update({name : number})

# def search_contact(name):
#     if name in contacts:
#         return contacts.get(name)
#     else:
#         return "Not Found"

# def delete_contact(name):
#     contacts.pop(name)

# add_contact("Jisan", "12345")
# add_contact("Rahim", "67890")
# print(contacts)

# print(search_contact("Jisan"))
# delete_contact("Jisan")
# print(search_contact("Jisan"))
# print(contacts)

"""✅ **Bonus Challenge (Optional):**
Write a function that takes a sentence and returns the **longest word**.

📎 **Example:**

```python
longest_word("Python is an amazing language") ➞ "amazing"
```"""

# def longest_word(s):
#     words = s.split()
#     long_word = words[0]
#     for word in words:
#         if len(word) > len(long_word):
#             long_word = word
#     return long_word

# print(longest_word("Python is an amazing language"))
# print(longest_word("Write a function that takes a sentence"))