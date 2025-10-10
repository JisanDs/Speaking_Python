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

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# print(fib(10))


"""🧩 Part 3 – OOP + Real-World Task
5️⃣ Task Manager App (Mini Project)

Create a simple Task Manager class that allows:

add_task(task_name)
remove_task(task_name)
view_tasks()

📁 Save all tasks in a JSON file (tasks.json)
🟢 Each task should have two fields:"""

from fu import save_json, load_json

class TaskManager:
    def __init__(self, file="tasks.json"):
        self.file = file
        self.tasks = load_json(file)

    def add_tasks(self, task, status=False):
        if any(t["task"] == task for t in self.tasks.values()):
            print("Task already exists")
            return
        count = str(len(self.tasks) + 1)
        self.tasks[count] = {"task": task, "done": status}
        save_json(self.tasks, self.file)

    def remove_task(self, task):
        found = False
        for key in list(self.tasks.keys()):
            if task == self.tasks[key]["task"]:
                found = True
                del self.tasks[key]
                print("Task removed")
                break
        save_json(self.tasks, self.file)
        if not found:
            print("Invalid task: not exist")

    def remove_all(self):
        if self.tasks:
            self.tasks = {}
            save_json(self.tasks, self.file)
        else:
            print("Tasks file empty")

    def view_task(self):
        if self.tasks:
            print("Your Task's:")
            for n, data in enumerate(self.tasks.values(), start=1):
                print(f"{n}. {data["task"]}")
        else:
            print("Tasks file empty")

def main():
    tm = TaskManager()
    tm.add_tasks("learn bash")
    tm.add_tasks("learn python")
    tm.add_tasks("learn linux cmd")
    tm.view_task()

    tm.remove_task("learn bash")
    tm.remove_task("learn")
    tm.view_task()


# if __name__ == "__main__":
#     main()


"""🧠 Bonus Challenge (Optional)
6️⃣ String Compression

Write a function that compresses repeated characters in a string.

Input: "aaabbccdaa"
Output: "a3b2c2d1a2"

(Hint: use a loop and count consecutive characters)"""

def compress_char(s):
    if not s:
        return None
    
    count = 1
    result = ""
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result


# print(compress_char("aaabbccdaa"))