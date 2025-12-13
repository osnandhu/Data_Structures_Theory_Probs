# Week 0: Python Crash Course for DSA (Dec 13-19, 2024)

**Goal**: Learn ONLY the Python you need for data structures. Not everything, just enough.

**Time Required**: 3-4 hours/day for 7 days

---

## Day 1 (TODAY - Dec 13): Python Basics

### 1. Hello World & Variables (30 min)
```python
# Run this in terminal: python3
# Or create a file: day1.py

# Printing
print("Hello, World!")
print("My DSA journey starts today!")

# Variables (no type declaration needed!)
name = "Your Name"
age = 25
height = 5.9
is_learning = True

print(name, age, height, is_learning)

# Multiple assignment
x, y, z = 1, 2, 3
```

**Practice**: Create `day1_practice.py` and print your name, age, and goal.

---

### 2. Numbers & Math (20 min)
```python
# Basic math
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333... (float division)
print(a // b)  # 3 (integer division) ← Important for DSA!
print(a % b)   # 1 (modulo/remainder) ← Very important!
print(a ** b)  # 1000 (exponent)

# Comparisons
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True
```

**Practice**: Write code to check if a number is even (hint: use modulo %)

---

### 3. Strings (30 min)
```python
# String basics
s = "Hello"
s2 = 'World'  # Single or double quotes

# String operations (similar to arrays!)
print(s[0])        # 'H' (indexing)
print(s[-1])       # 'o' (last character)
print(s[1:4])      # 'ell' (slicing)
print(s + s2)      # 'HelloWorld' (concatenation)
print(len(s))      # 5 (length)

# String methods (memorize these!)
text = "hello world"
print(text.upper())      # 'HELLO WORLD'
print(text.lower())      # 'hello world'
print(text.split())      # ['hello', 'world'] ← Important!
print(text.replace('h', 'j'))  # 'jello world'

# Check substring
print('hello' in text)   # True
print('xyz' in text)     # False
```

**Practice**: Create a string with your name and print it reversed (hint: `s[::-1]`)

---

### 4. Lists (Arrays in Python) (40 min) ← CRITICAL FOR DSA
```python
# Creating lists
arr = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Can mix types (but usually don't)

# Accessing elements
print(arr[0])    # 1
print(arr[-1])   # 5 (last element)
print(arr[1:3])  # [2, 3] (slicing)

# Modifying lists
arr[0] = 10      # [10, 2, 3, 4, 5]
arr.append(6)    # [10, 2, 3, 4, 5, 6]
arr.insert(0, 0) # [0, 10, 2, 3, 4, 5, 6]
arr.pop()        # Removes and returns 6
arr.remove(10)   # Removes first occurrence of 10

# List operations (MEMORIZE THESE!)
nums = [3, 1, 4, 1, 5, 9, 2]
print(len(nums))      # 7
print(max(nums))      # 9
print(min(nums))      # 1
print(sum(nums))      # 25
print(sorted(nums))   # [1, 1, 2, 3, 4, 5, 9] (returns new list)
nums.sort()           # Sorts in place
nums.reverse()        # Reverses in place

# List comprehension (powerful!)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

**Practice**: Create a list of numbers 1-10, find the sum, find the max, reverse it.

---

### 5. If/Else Statements (20 min)
```python
# Basic if-else
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is exactly 5")
else:
    print("x is less than 5")

# One-liner (ternary)
result = "even" if x % 2 == 0 else "odd"

# Multiple conditions
age = 25
if age >= 18 and age < 65:
    print("Adult")

# Check in list
if x in [1, 2, 3, 4, 5]:
    print("Found!")
```

**Practice**: Write code to find if a number is positive, negative, or zero.

---

### 6. Loops (40 min) ← CRITICAL FOR DSA
```python
# For loop (most common)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 10, 2):  # start, stop, step
    print(i)  # 2, 4, 6, 8

# Loop through list
arr = [10, 20, 30, 40]
for num in arr:
    print(num)

# Loop with index (IMPORTANT!)
for i in range(len(arr)):
    print(f"Index {i}: {arr[i]}")

# Loop with enumerate (BETTER!)
for i, num in enumerate(arr):
    print(f"Index {i}: {num}")

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# Break and continue
for i in range(10):
    if i == 5:
        break  # Exit loop
    if i % 2 == 0:
        continue  # Skip this iteration
    print(i)  # Only prints odd numbers < 5
```

**Practice**: Print all even numbers from 1 to 20 using a for loop.

---

## Day 1 Challenge (60 min)

Combine everything to solve this:

```python
# Create a list of numbers from 1 to 100
# Print all numbers that are:
# 1. Divisible by 3 OR 5
# 2. But NOT divisible by both

# Expected output: 3, 5, 6, 9, 10, 12, 18, 20, ...
```

<details>
<summary>Solution (try first!)</summary>

```python
for i in range(1, 101):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i)
```
</details>

---

## Day 1 Checklist

- [ ] Set up Python (already done!)
- [ ] Understand variables and types
- [ ] Can work with strings
- [ ] Comfortable with lists (append, remove, slice)
- [ ] Can write if/else statements
- [ ] Can write for and while loops
- [ ] Completed Day 1 Challenge

**If you finish all this today, you're 15% done with Python basics! 🎉**

---

## Tomorrow (Day 2): Functions & Dictionaries

You'll learn:
- How to write reusable functions
- Dictionaries (hash maps) - CRITICAL for DSA
- More list operations

**See you tomorrow! Don't skip Day 1 - it's the foundation.**
