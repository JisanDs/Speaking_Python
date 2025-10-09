"""🔥 অসাধারণ, Jisan ভাই! আমরা এখন পৌঁছে গেছি —

🧠 Day 40 – Speak Python 29
(Phase 7: Advanced Logic + Problem Solving + Mini Project 2)"""


"""⚙️ Part 1 – Function + Logic Problems
1️⃣ Longest Word Finder

Write a function that finds the longest word in a sentence.

Input: "Python is powerful and beautiful"
Output: beautiful"""

def long_word(s):
    if not s:
        return None
    
    words = s.split(" ")
    print(words)
    max_word = words[0]
    length = len(words[0])

    for word in words:
        if len(word) > length:
            max_word = word
            length = len(word)
    return max_word


# print(long_word("hello my name is jisan"))
# print(long_word("The magnificent programming language is Python")) 
# print(long_word("Python is powerful and beautiful")) 


"""2️⃣ Number to Words (Recursive)

Write a recursive function that prints numbers in words (1 → one, 2 → two, etc.) for any given integer.

Input: 123
Output: "one two three" """

def num_to_word(n):
    if n == 0:
        return n
    
    word_map = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    last_digit = n % 10
    remain = n // 10
    result = num_to_word(remain)
    current_word = word_map[last_digit]

    if result:
        return result +" "+ current_word
    else:
        return current_word


# print(num_to_word(1234567890))
# for n in range(1, 10):
#     print(num_to_word(n))

"""🔁 Part 2 – Advanced Recursion
3️⃣ Flatten Nested List

Write a recursive function that flattens a deeply nested list into a single list.

Input: [1, [2, [3, [4, 5]]]]
Output: [1, 2, 3, 4, 5]"""

def flatten_nest_lst(nest_lst):
    flat_lst = []
    for n in nest_lst:
        if isinstance(n, list):
            flat_lst.extend(flatten_nest_lst(n))
        else:
            flat_lst.append(n)
    return flat_lst

# print(flatten_nest_lst([1, [2, [3, [4, 5]]]]))


"""4️⃣ Fibonacci Memoization

Write a recursive function with memoization to generate the nth Fibonacci number efficiently.

Input: 10
Output: 55

Hint: Use a dictionary memo = {} to store computed results."""



# print(fib(10))


"""🧠 Bonus Challenge (Optional)
6️⃣ String Compression

Write a function that compresses repeated characters in a string.

Input: "aaabbccdaa"
Output: "a3b2c2d1a2"

(Hint: use a loop and count consecutive characters)"""



# print(compress_char("aaabbccdaa"))


"""🧩 Part 3 – OOP + Real-World Task
5️⃣ Task Manager App (Mini Project)

Create a simple Task Manager class that allows:

add_task(task_name)
remove_task(task_name)
view_tasks()
mark_done(task_name)

📁 Save all tasks in a JSON file (tasks.json)
🟢 Each task should have two fields:"""

from fu import save_json, load_json

class TaskManager:
    def __init__(self, file):
        self.file = file
        self.tasks = load_json(file)


