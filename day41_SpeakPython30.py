import json


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
print(sort_by_score(scores))
