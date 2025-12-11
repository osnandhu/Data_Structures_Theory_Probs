# Problem Solving Framework

**The goal isn't to solve every problem immediately. The goal is to build problem-solving skills.**

---

## The UMPIRE Method (Use this for EVERY problem)

### U - Understand
**Ask these questions:**
- What are the inputs? (type, size, constraints)
- What is the expected output?
- What are edge cases? (empty input, single element, duplicates, negative numbers)
- Can I restate the problem in my own words?

**Example (Two Sum):**
- Input: Array of integers, target integer
- Output: Indices of two numbers that sum to target
- Edge cases: Empty array, no solution, multiple solutions
- Restate: "Find positions of two numbers that add up to a goal number"

---

### M - Match
**What pattern does this match?**
- Array/String manipulation → Two pointers, sliding window, hash map
- Searching → Binary search, DFS, BFS
- Sorted data → Binary search, two pointers
- Tree/Graph → DFS, BFS, recursion
- Optimization → Dynamic programming, greedy
- Subsets/permutations → Backtracking
- Top K elements → Heap

---

### P - Plan
**Pseudocode your approach:**
1. Write steps in plain English
2. Don't code yet!
3. Walk through with example
4. Identify time/space complexity

**Example plan (Two Sum):**
```
1. Create empty hash map
2. For each number in array:
   a. Calculate complement (target - current number)
   b. Check if complement exists in hash map
   c. If yes, return current index and complement's index
   d. If no, store current number and index in hash map
3. If no solution found, return empty
```

---

### I - Implement
**Now write actual code:**
- Start with brute force if stuck
- Use clear variable names
- Add comments for complex logic
- Handle edge cases

---

### R - Review
**Check your solution:**
- Does it handle edge cases?
- Any off-by-one errors?
- Any unnecessary operations?
- Can you simplify?

---

### E - Evaluate
**Analyze complexity:**
- Time complexity: O(?)
- Space complexity: O(?)
- Can it be optimized?

---

## When You're Completely Stuck

### Level 1: Hints (Try these first)
1. **Draw it out**: Visualize with simple example
2. **Think aloud**: Explain problem to rubber duck/friend
3. **Brute force first**: What's the obvious (slow) solution?
4. **Pattern match**: Which topic does this relate to?
5. **Check constraints**: Often hints at approach (n ≤ 100 → O(n²) okay, n ≤ 10⁵ → need O(n))

### Level 2: Guided Discovery (After 30 min)
1. Read problem's "Related Topics" tags
2. Look at problem category/pattern
3. Check one hint from problem
4. Don't read solution yet!

### Level 3: Learning Mode (After 45-60 min)
1. Watch a solution explanation (NeetCode, YouTube)
2. DON'T copy code - understand the approach
3. Close video, implement yourself
4. Add comments explaining WHY each step works
5. Mark problem for review in 3 days

---

## Common Patterns & When to Use Them

### 1. Two Pointers
**When to use:**
- Array/string is sorted
- Need to find pairs/triplets
- Palindrome checking
- Merging sorted arrays

**Template:**
```python
left, right = 0, len(arr) - 1
while left < right:
    # Process
    if condition:
        left += 1
    else:
        right -= 1
```

---

### 2. Sliding Window
**When to use:**
- Subarray/substring problems
- "Maximum/minimum of K consecutive elements"
- "Longest substring with..."

**Template:**
```python
left = 0
for right in range(len(arr)):
    # Add arr[right] to window

    while window_invalid:
        # Remove arr[left] from window
        left += 1

    # Update result
```

---

### 3. Hash Map/Set
**When to use:**
- Need O(1) lookup
- Counting frequency
- Checking for duplicates
- Two Sum variations

**Template:**
```python
seen = {}  # or set()
for item in items:
    if item in seen:
        # Found duplicate/pair
    seen[item] = some_value
```

---

### 4. BFS (Breadth-First Search)
**When to use:**
- Shortest path (unweighted)
- Level-order traversal
- "Minimum steps to reach..."

**Template:**
```python
from collections import deque

queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

---

### 5. DFS (Depth-First Search)
**When to use:**
- Exploring all paths
- Backtracking problems
- Connected components
- Cycle detection

**Template (Recursive):**
```python
def dfs(node, visited):
    if node in visited:
        return

    visited.add(node)

    for neighbor in get_neighbors(node):
        dfs(neighbor, visited)
```

**Template (Iterative):**
```python
stack = [start]
visited = {start}

while stack:
    node = stack.pop()

    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)
```

---

### 6. Dynamic Programming
**When to use:**
- "Maximum/minimum/count of ways"
- Overlapping subproblems
- Optimal substructure
- Can break into smaller identical problems

**Template (Top-Down / Memoization):**
```python
def dp(state, memo):
    if base_case:
        return base_result

    if state in memo:
        return memo[state]

    # Compute result from subproblems
    result = combine(dp(subproblem1), dp(subproblem2))

    memo[state] = result
    return result
```

**Template (Bottom-Up / Tabulation):**
```python
dp = [0] * (n + 1)
dp[0] = base_case

for i in range(1, n + 1):
    dp[i] = compute_from_previous(dp[i-1], dp[i-2], ...)

return dp[n]
```

---

### 7. Backtracking
**When to use:**
- Generate all combinations/permutations/subsets
- N-Queens, Sudoku solver
- "Find all valid..."

**Template:**
```python
def backtrack(path, choices):
    if is_valid_solution(path):
        result.append(path[:])
        return

    for choice in choices:
        # Make choice
        path.append(choice)

        # Recurse
        backtrack(path, updated_choices)

        # Undo choice (backtrack)
        path.pop()
```

---

## Time Complexity Cheat Sheet

| Complexity | Max Input Size | Common Algorithms |
|------------|---------------|-------------------|
| O(1) | Any | Hash map lookup, array access |
| O(log n) | 10^18 | Binary search, balanced tree ops |
| O(n) | 10^8 | Single loop, hash map building |
| O(n log n) | 10^6 | Sorting, heap operations |
| O(n²) | 10^4 | Nested loops, brute force pairs |
| O(2^n) | 20-25 | Backtracking all subsets |
| O(n!) | 10-12 | All permutations |

**If n = 10⁵ and you use O(n²), it will timeout!**

---

## Debugging Checklist

When your code doesn't work:

✅ **Test with simple example** (n=1, n=2)
✅ **Check edge cases** (empty, single element, all same, negatives)
✅ **Print intermediate values** (use print statements liberally)
✅ **Off-by-one errors** (should it be `< n` or `<= n`?)
✅ **Index out of bounds** (accessing array[-1] or array[n]?)
✅ **Integer overflow** (rare in Python, but possible)
✅ **Infinite loops** (is loop condition ever false?)

---

## Growth Mindset Reminders

**Fixed Mindset** → **Growth Mindset**
- "I can't solve this" → "I can't solve this YET"
- "I'm bad at recursion" → "I need more practice with recursion"
- "This is too hard" → "This will make me stronger"
- "Others are smarter" → "Others have practiced more"

---

## Problem-Solving Habits

### Before solving:
1. Read problem 2-3 times carefully
2. Write down constraints
3. Create 2-3 test cases (including edge cases)

### While solving:
1. Start with brute force approach
2. Think optimization AFTER brute force works
3. Comment your code as you write

### After solving:
1. Test with edge cases
2. Analyze time/space complexity
3. Read discuss section for alternative approaches
4. Schedule review in 3 days, 1 week, 1 month

---

## Daily Practice Routine

**15 min**: Review yesterday's problem (don't look at code, solve again)
**45 min**: Attempt new problem (use UMPIRE method)
**30 min**: If stuck, learn solution properly + implement
**30 min**: Write notes - what pattern, why it works, similar problems

**Total**: 2 hours/day = Software engineer in 3-4 months

---

## Resources for Getting Unstuck

1. **Visualize**: https://visualgo.net
2. **Video explanations**: NeetCode (YouTube)
3. **Written explanations**: LeetCode Discuss (sort by "Most Votes")
4. **Pattern recognition**: https://seanprashad.com/leetcode-patterns/

---

Remember: **Struggling is learning. Every "I don't know" is an opportunity to grow.**

The best developers aren't the ones who never get stuck - they're the ones who get unstuck faster through practice.
