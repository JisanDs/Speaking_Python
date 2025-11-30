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
rus = group_by_length(words)
print(json.dumps(rus, indent=2))
