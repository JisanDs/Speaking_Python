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

words = ["hi", "hello", "cat", "python", "ok"]

result = {}

for word in words:
    if result.get(len(word)):
        result[len(word)].append(word)
    else:
        result.update({len(word): [word]})


print(result)
