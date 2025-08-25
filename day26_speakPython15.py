"""🧠 **Day 26 – Speak Python 15**

### **Phase 4: Problem Solving with Recursion & Thinking Smart**

**Focus Areas:**

* Classic Recursion Problems
* Backtracking Basics
* Recursion vs Iteration
"""

"""✅ Problem 1: Power Function with Recursion

📌 **Task:**
Write a recursive function to calculate `a^b`.

📎 **Example:**

```python
power(2, 3) ➞ 8  
power(5, 0) ➞ 1
```

💡 **Hint:**
`a^b = a \* a^(b-1)` with base case `power(a,0)=1`."""

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)

print(power(2, 3))
print(power(4, 3))
print(power(5, 0))


"""✅ Problem 2: Count Digits using Recursion

📌 **Task:**
Write a recursive function that counts digits in a number.

📎 **Example:**

```python
count\_digits(12345) ➞ 5  
count\_digits(7) ➞ 1
```

💡 **Hint:**
`count\_digits(n) = 1 + count\_digits(n//10)` until `n==0`."""

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n//10)

print(count_digits(1345))
print(count_digits(12345))
print(count_digits(7))


"""✅ Problem 3: Greatest Common Divisor (GCD)

📌 **Task:**
Find GCD of two numbers using recursion.

📎 **Example:**
```python
gcd(48, 18) ➞ 6
```

💡 **Hint:**
Use Euclidean Algorithm:
`gcd(a,b) = gcd(b, a%b)` with base `gcd(a,0)=a`.
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(48, 18))
print(gcd(12, 18))


"""✅ Problem 4: Palindrome Check with Recursion

📌 **Task:**
Check if a string is palindrome using recursion.

📎 **Example:**

```python
is\_palindrome("madam") ➞ True  
is\_palindrome("hello") ➞ False
```

💡 **Hint:**
Check first and last character, then recurse on the substring.
"""

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("racecar"))