# Arrays - Foundation of DSA

## What is an Array?

An array is a **contiguous block of memory** that stores elements of the same type, accessed by an index.

```
Index:  0   1   2   3   4
Array: [10, 20, 30, 40, 50]
         ↑
Memory: 1000, 1004, 1008, 1012, 1016 (if integers are 4 bytes)
```

## Why Arrays Matter

- **60%+ of easy problems** involve array manipulation
- Foundation for more complex data structures (stacks, heaps, hash tables)
- Most common in interview questions

---

## Python Lists vs Traditional Arrays

**Python Lists** (what you'll use):
```python
arr = [1, 2, 3, 4, 5]  # Dynamic, can grow/shrink
arr.append(6)           # O(1) amortized
arr.insert(0, 0)        # O(n) - shifts everything
```

**Traditional Arrays** (in C/Java):
- Fixed size at creation
- Cannot grow dynamically

---

## Time Complexity (Critical to Memorize!)

| Operation | Time Complexity | Why? |
|-----------|----------------|------|
| **Access** `arr[i]` | O(1) | Direct memory calculation: base + (i × element_size) |
| **Search** (unsorted) | O(n) | Must check every element |
| **Search** (sorted) | O(log n) | Binary search possible |
| **Insert at end** | O(1) amortized | Just append (may need resize) |
| **Insert at index i** | O(n) | Shift all elements after i |
| **Delete at index i** | O(n) | Shift all elements after i |

---

## Space Complexity

- Storing array: **O(n)** where n = number of elements
- Modifying in-place: **O(1)** extra space

---

## Common Operations in Python

### 1. Creating Arrays
```python
# Empty array
arr = []

# With values
arr = [1, 2, 3, 4, 5]

# Using list comprehension
arr = [i for i in range(10)]  # [0, 1, 2, ..., 9]

# Fixed size with same value
arr = [0] * 5  # [0, 0, 0, 0, 0]
```

### 2. Accessing Elements
```python
arr = [10, 20, 30, 40, 50]

# Forward indexing
print(arr[0])   # 10
print(arr[2])   # 30

# Backward indexing (Python specific!)
print(arr[-1])  # 50 (last element)
print(arr[-2])  # 40 (second to last)
```

### 3. Slicing (Very Powerful!)
```python
arr = [10, 20, 30, 40, 50]

# arr[start:end]  → elements from start to end-1
print(arr[1:4])   # [20, 30, 40]
print(arr[:3])    # [10, 20, 30] (start to index 2)
print(arr[2:])    # [30, 40, 50] (index 2 to end)
print(arr[:])     # [10, 20, 30, 40, 50] (copy entire array)

# With step
print(arr[::2])   # [10, 30, 50] (every 2nd element)
print(arr[::-1])  # [50, 40, 30, 20, 10] (reverse!)
```

### 4. Modifying Arrays
```python
arr = [10, 20, 30]

# Append to end - O(1)
arr.append(40)  # [10, 20, 30, 40]

# Insert at index - O(n)
arr.insert(0, 5)  # [5, 10, 20, 30, 40]

# Extend with another array - O(k) where k is length of added array
arr.extend([50, 60])  # [5, 10, 20, 30, 40, 50, 60]

# Remove by value - O(n)
arr.remove(20)  # [5, 10, 30, 40, 50, 60]

# Remove by index - O(n)
arr.pop(0)  # [10, 30, 40, 50, 60], returns 5
arr.pop()   # [10, 30, 40, 50], returns 60 (removes last)
```

### 5. Searching
```python
arr = [10, 20, 30, 40, 50]

# Check if element exists - O(n)
if 30 in arr:
    print("Found!")

# Get index of element - O(n)
index = arr.index(30)  # 2
```

### 6. Sorting
```python
arr = [40, 10, 30, 20, 50]

# In-place sort - O(n log n)
arr.sort()  # [10, 20, 30, 40, 50]

# Return sorted copy
sorted_arr = sorted(arr)  # Original unchanged

# Reverse sort
arr.sort(reverse=True)  # [50, 40, 30, 20, 10]
```

---

## Common Patterns You'll Use

### 1. Iterating Through Array
```python
arr = [10, 20, 30, 40, 50]

# Method 1: By value
for num in arr:
    print(num)

# Method 2: By index
for i in range(len(arr)):
    print(f"Index {i}: {arr[i]}")

# Method 3: Index and value (BEST!)
for i, num in enumerate(arr):
    print(f"Index {i}: {num}")
```

### 2. Two Pointer Technique
```python
# Useful for: palindromes, pair sums, reversing
left, right = 0, len(arr) - 1

while left < right:
    # Process arr[left] and arr[right]
    left += 1
    right -= 1
```

### 3. Sliding Window
```python
# Useful for: subarrays, substrings
window_start = 0

for window_end in range(len(arr)):
    # Add arr[window_end] to window

    while window_invalid:
        # Remove arr[window_start] from window
        window_start += 1

    # Update result
```

### 4. Prefix Sum (Critical Pattern!)
```python
# Useful for: subarray sum queries
arr = [1, 2, 3, 4, 5]

# Build prefix sum
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]

# Now sum from index i to j = prefix[j+1] - prefix[i]
# Example: sum from index 1 to 3 = prefix[4] - prefix[1] = 9
```

---

## Common Pitfalls (Don't Make These Mistakes!)

### 1. Index Out of Bounds
```python
arr = [10, 20, 30]

# WRONG ❌
print(arr[3])  # IndexError!

# RIGHT ✅
if 3 < len(arr):
    print(arr[3])
```

### 2. Modifying Array While Iterating
```python
arr = [1, 2, 3, 4, 5]

# WRONG ❌
for i in range(len(arr)):
    arr.append(i)  # Infinite loop!

# RIGHT ✅
original_length = len(arr)
for i in range(original_length):
    arr.append(i)
```

### 3. Shallow Copy vs Deep Copy
```python
arr = [1, 2, 3]

# WRONG ❌ (both point to same array)
arr2 = arr
arr2.append(4)  # arr is also [1, 2, 3, 4]

# RIGHT ✅ (creates new array)
arr2 = arr[:]  # or arr.copy() or list(arr)
```

---

## Practice Problems (Start Here!)

### Week 1 Problems:
1. **Two Sum (LC 1)** - Hash map approach
2. **Best Time to Buy/Sell Stock (LC 121)** - Single pass
3. **Contains Duplicate (LC 217)** - Hash set
4. **Product of Array Except Self (LC 238)** - Prefix/suffix
5. **Maximum Subarray (LC 53)** - Kadane's algorithm

---

## Before Moving to Next Topic

Ask yourself:
✅ Can I explain how array indexing works in memory?
✅ Can I implement common operations (insert, delete, search)?
✅ Do I understand time complexity for each operation?
✅ Have I solved at least 5 array problems?

**If yes to all → Move to Strings!**
**If no → Review and practice more.**

---

## Next Steps

1. Implement operations in `implementation.py`
2. Solve problems in `problems/` folder
3. Mark progress in `/PROGRESS.md`
4. Review in 3 days, 1 week, 1 month

**Remember**: Understanding beats memorization. Ask "WHY" not just "HOW".
