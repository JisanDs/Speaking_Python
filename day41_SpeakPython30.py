import fu
import sys


"""🔁 Part 1: Algorithmic Thinking (New Patterns)
1️⃣ Two Sum (Optimized Logic)

Write a function that returns the indices of two numbers that add up to a target.

Input:

nums = [2, 7, 11, 15]
target = 9

Output: (0, 1)

✅ Condition

Do NOT use nested loops
Use dictionary (hash map)

⚠️ This is a classic interview-level problem."""

nums = [2, 7, 11, 15]
target = 9

sp = nums[0]
for n in nums:
    if n < target:
        pass


"""⚡ Part 2: Data Processing Logic
3️⃣ Group Words by Length
Given a list of words, group them by length.

Input: words = ["hi", "hello", "cat", "python", "ok"]

Output:

{
  2: ["hi", "ok"],
  3: ["cat"],
  5: ["hello"],
  6: ["python"]
}

✅ Focus: dictionary + iteration"""

def group_by_length(lst: list) -> dict:
    result = {}
    for s in lst:
        if result.get(len(s)):
            result[len(s)].append(s)
        else:
            result.update({len(s): [s]})
    return result


# words = ["hi", "hello", "cat", "python", "ok"]
words = ["hi", "by", "hello", "group", "name", "cat", "python", "ok"]
# rus = group_by_length(words)
# print(json.dumps(rus, indent=2))


"""2️⃣ Valid Parentheses

Write a function that checks whether a string of brackets is valid.

Input: "()[]{}"
Output: True
Invalid example: "(]"

👉 Use stack logic (list)"""

def valid_prntes(s: str) -> bool:
    stack = ["()", "[]", "{}"]
    status = False

    for paren in stack:
        if paren in s:
            status = True
    return status

# print(valid_prntes("()"))
# print(valid_prntes("(}"))
# print(valid_prntes("()[]{}"))


"""4️⃣ Sort Dictionary by Value (Descending)

Given: scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

Output: [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

✅ Use sorted() with key"""

def sort_by_score(d: dict) -> list:
    result = []
    work_dict = [{'name': name, 'score': score} for name, score in d.items()]
    for data in sorted(work_dict, key=lambda data: data['score'], reverse=True):
        result.append((data['name'],data['score']))
    return result

scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
#print(sort_by_score(scores))


""" Part 3: Debugging + Clean Code

5️⃣ Bug Fix + Refactor

Buggy Code:

class User:
    def __init__(self, name, age):
        name = name
        self.age = age

    def show(self):
        print("Name:", self.name, "Age:", self.age)

u = User("Jisan", 20)
u.show()

👉 Fix it
👉 Make code clean & professional"""


# dbuggy code:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def __str__(self):
        # str method is my proposing approach
        return f"Name: {self.name}, Age: {self.age}"


#u = User("Jisan", 20)
#print(u)


"""📂 Part 4: Mini Project – Student Result Manager

🎓 Student Result System (OOP + JSON)

Build a small system to manage student results.

Features:

  add_student(name, marks)
  view_students()
  topper() → highest marks
  remove_student(name)


📁 Data must be stored in:

students.json

✅ You can use your FileUtilites library
✅ Store data like:

{
  "Jisan": 89,
  "Alex": 92
}"""


class Students:
    def __init__(self, file_name="students.json"):
        self.file_name = file_name
        self.db = fu.load_json(self.file_name)

    def add_student(self, name, mark):
        found = False
        for student in self.db:
            if student['name'].lower() == name.lower():
                found = True
                break

        if found:
            sys.stderr.write(f"Student: {name} alrady exists\n")
            return
        student = {"name": name, "mark": mark}
        self.db.append(student)
        fu.save_json(self.db, self.file_name)

    def view_students(self):
        print("____STUDENTS____:")
        for st in self.db:
            print(f"Name: {st['name']}, Mark: {st['mark']}")

    def topper(self):
        for st in sorted(self.db, key=lambda st: st['mark'], reverse=True):
            print(f"Name: {st['name']}, Mark: {st['mark']}")
            break

    def remove_student(self, name):
        found = False
        for i, st in enumerate(self.db):
            if st['name'] == name:
                self.db.pop(i)
                found = True
                fu.save_json(self.db, self.file_name)
                break

        if not found:
            sys.stderr.write(f"ExistError: {name} Not found in students databeas\n")

    def count_students(self):
        students = len(self.db)
        print(f"Students in databace: {students}")


st = Students()
st.count_students()
