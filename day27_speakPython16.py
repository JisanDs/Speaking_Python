"""🧠 **Day 27 – Speak Python 16**

### **Phase 5: Recursion Mastery – Real Problem Solving**

**Focus Areas:**

* More Practice with Recursion
* Thinking about Base Case First
* Visualizing Call Stack
* Easy–to–Medium problems only (প্রজেক্ট বাদ)"""

"""✅ Problem 1: Sum of Digits

📌 **Task:**
Write a recursive function to calculate the sum of digits of a number.

📎 **Example:**

```python
sum_digits(123) ➞ 6   # (1+2+3)
sum_digits(9875) ➞ 29
```

💡 **Hint:**
Last digit পাওয়া যাবে `n % 10` দিয়ে, বাকি digit → `n // 10`"""

# def sum_digits(n):
#     if n == 0:
#         return n
#     return (n%10) + sum_digits(n//10)

# print(sum_digits(234))
# print(sum_digits(123))
# print(sum_digits(9875))


"""✅ Problem 2: Product of List (Recursive)

📌 **Task:**
Write a recursive function to multiply all numbers in a list.

📎 **Example:**

```python
product([1, 2, 3, 4]) ➞ 24
product([2, 5, 6]) ➞ 60
```

💡 **Hint:**
`[x]` → return x
Otherwise → first \* product(rest)"""

# def product(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] * product(lst[1:])

# print(product([1, 2, 3, 4]))
# print(product([2, 5, 6]))


"""✅ Problem 3: Recursive Max Finder

📌 **Task:**
Find the maximum number in a list using recursion.

📎 **Example:**

```python
recursive_max([3, 5, 2, 9, 1]) ➞ 9
recursive_max([10, 7, 22, 14]) ➞ 22
```

💡 **Hint:**
Compare first element with `recursive_max(rest)`"""

# def recursive_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     max_result = recursive_max(lst[1:])
#     return lst[0] if lst[0] > max_result else max_result

# print(recursive_max([30, 5, 2, 9, 1]))
# print(recursive_max([3, 5, 2, 9, 1]))
# print(recursive_max([10, 7, 22, 14]))


"""✅ Problem 4: Count Occurrences (Recursive)

📌 **Task:**
Count how many times a given element appears in a list using recursion.

📎 **Example:**

```python
count_occurrences([1, 2, 3, 2, 4, 2], 2) ➞ 3
count_occurrences([5, 5, 5, 5], 5) ➞ 4
```

💡 **Hint:**
Check first element, then recurse on the rest of the list."""

# def count_occurrences(lst, terget):
#     if not lst:
#         return 0
#     count = 1 if lst[0] == terget else 0
#     return count + count_occurrences(lst[1:], terget)

# print(count_occurrences([1, 2, 3, 2, 4, 2], 2))
# print(count_occurrences([5, 5, 5, 5], 5))