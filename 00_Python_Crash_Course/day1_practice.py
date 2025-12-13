"""
Day 1 Practice - Your First Python Program
Run this file: python3 day1_practice.py
"""

print("=" * 50)
print("WELCOME TO YOUR DSA JOURNEY!")
print("=" * 50)
print()

# =========================
# SECTION 1: Variables
# =========================
print("SECTION 1: Variables")
print("-" * 30)

# TODO: Create variables with your information
your_name = "FILL_THIS_IN"  # Replace with your name
your_age = 0  # Replace with your age
start_date = "December 13, 2024"
target_date = "March 14, 2025"

print(f"Name: {your_name}")
print(f"Age: {your_age}")
print(f"Start Date: {start_date}")
print(f"Target Date: {target_date}")
print()

# =========================
# SECTION 2: Math
# =========================
print("SECTION 2: Math Operations")
print("-" * 30)

# Calculate days until interview ready
weeks = 12
days_per_week = 7
total_days = weeks * days_per_week

print(f"Total days of training: {total_days}")
print(f"Hours per day: 3-4")
print(f"Total hours: {total_days * 3} - {total_days * 4}")
print()

# =========================
# SECTION 3: Strings
# =========================
print("SECTION 3: String Practice")
print("-" * 30)

motivational_quote = "Every expert was once a beginner"
print(f"Quote: {motivational_quote}")
print(f"Quote in CAPS: {motivational_quote.upper()}")
print(f"Quote reversed: {motivational_quote[::-1]}")
print()

# =========================
# SECTION 4: Lists (Arrays)
# =========================
print("SECTION 4: List Practice")
print("-" * 30)

# Create a list of topics you'll learn
topics = ["Arrays", "Strings", "Hash Tables", "Linked Lists",
          "Stacks", "Queues", "Trees", "Graphs", "DP"]

print(f"Total topics to learn: {len(topics)}")
print(f"First topic: {topics[0]}")
print(f"Last topic: {topics[-1]}")
print("All topics:", topics)
print()

# =========================
# SECTION 5: Loops
# =========================
print("SECTION 5: Loop Practice")
print("-" * 30)

print("Your learning roadmap:")
for i, topic in enumerate(topics, start=1):
    print(f"  {i}. {topic}")
print()

# =========================
# SECTION 6: If/Else
# =========================
print("SECTION 6: Conditionals")
print("-" * 30)

hours_today = 0  # TODO: Change this to how many hours you plan to study today

if hours_today >= 3:
    print("✅ Great! You're on track!")
elif hours_today >= 2:
    print("⚠️  Good start, try to reach 3 hours")
else:
    print("❌ You need at least 2-3 hours daily")
print()

# =========================
# CHALLENGE: Your First Algorithm!
# =========================
print("=" * 50)
print("CHALLENGE: Find Maximum Number")
print("=" * 50)

numbers = [23, 45, 12, 67, 34, 89, 15, 90, 5]
print(f"Numbers: {numbers}")

# TODO: Write code to find the maximum number WITHOUT using max()
# Hint: Use a loop and compare each number

max_num = numbers[0]  # Start with first number
for num in numbers:
    if num > max_num:
        max_num = num

print(f"Maximum number: {max_num}")
print(f"Verify with max(): {max(numbers)}")
print()

# =========================
# CHALLENGE 2: Sum of Even Numbers
# =========================
print("CHALLENGE 2: Sum of Even Numbers")
print("-" * 30)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {nums}")

# TODO: Calculate sum of only even numbers
# Hint: Use modulo (%) to check if even

even_sum = 0
for num in nums:
    if num % 2 == 0:  # Even numbers are divisible by 2
        even_sum += num

print(f"Sum of even numbers: {even_sum}")
print()

# =========================
# CHALLENGE 3: Reverse a List
# =========================
print("CHALLENGE 3: Reverse a List")
print("-" * 30)

original = [1, 2, 3, 4, 5]
print(f"Original: {original}")

# Method 1: Using slicing
reversed_1 = original[::-1]
print(f"Reversed (slicing): {reversed_1}")

# Method 2: Using reverse() method
original_copy = original.copy()
original_copy.reverse()
print(f"Reversed (method): {original_copy}")

# Method 3: Manual reversal (for learning!)
manual_reversed = []
for i in range(len(original) - 1, -1, -1):
    manual_reversed.append(original[i])
print(f"Reversed (manual): {manual_reversed}")
print()

# =========================
# FINAL MESSAGE
# =========================
print("=" * 50)
print("CONGRATULATIONS! 🎉")
print("=" * 50)
print("You just ran your first Python program!")
print()
print("Next steps:")
print("1. Make sure all TODO items are filled in")
print("2. Read Day1_Basics.md completely")
print("3. Try the Day 1 Challenge in the markdown file")
print("4. Tomorrow: Functions & Dictionaries")
print()
print("Remember: You're not trying to be perfect.")
print("You're trying to be CONSISTENT.")
print()
print("See you tomorrow! 💪")
print("=" * 50)
