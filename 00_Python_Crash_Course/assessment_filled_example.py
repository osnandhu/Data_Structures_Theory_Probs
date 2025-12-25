"""
Python Skills Assessment - EXAMPLE OF HOW TO FILL IT OUT
This shows you HOW to uncomment and fill in your answers.
Copy your answers from here to assessment.py
"""

print("=" * 60)
print("PYTHON SKILLS ASSESSMENT")
print("=" * 60)
print("\nBe HONEST. This is for YOU, not a test to pass.\n")

# =========================
# SECTION 1: Have you coded before?
# =========================
print("QUESTION 1: Programming Background")
print("-" * 60)

# EXAMPLE: If you've never coded, do this:
# Keep the # on the ones that DON'T apply to you
# Remove the # from the ONE that applies to you

# background = "Never coded anything before"  ← REMOVE # if this is you
# background = "Tried coding once or twice (tutorials)"
# background = "Took a programming course (any language)"
# background = "Coded in another language (Java/C++/JS)"
# background = "Professional programmer in another language"

# PICK ONE ABOVE and uncomment it (remove the #)
# For now, I'll leave this as placeholder:
background = "CHOOSE_ONE_ABOVE"

print(f"Your answer: {background}")
print()

# =========================
# SECTION 2: Python Variables Test
# =========================
print("QUESTION 2: Can you create variables?")
print("-" * 60)
print("Task: Create a variable 'my_name' with your name")
print()

# EXAMPLE: If you can do this, write:
# my_name = "Your Actual Name"
# If you CAN'T, just leave it commented (with #)

# TODO: Uncomment and fill in:
# my_name = "YourName"

try:
    print(f"Result: {my_name}")
    q2_pass = True
except:
    print("❌ Not done yet (it's okay!)")
    q2_pass = False
print()

# =========================
# SECTION 3: Lists Test
# =========================
print("QUESTION 3: Can you work with lists?")
print("-" * 60)
print("Task: Create a list of numbers 1 to 5, then print the 3rd element")
print()

# EXAMPLE: If you can do this:
# numbers = [1, 2, 3, 4, 5]
# third_element = numbers[2]  # Remember: index 2 is the 3rd element!

# TODO: Uncomment and fill in:
# numbers = [1, 2, 3, 4, 5]
# third_element = numbers[2]

try:
    print(f"Your list: {numbers}")
    print(f"Third element: {third_element}")
    q3_pass = (third_element == 3)
    if q3_pass:
        print("✅ Correct!")
    else:
        print("❌ Not quite - the third element should be 3")
except:
    print("❌ Not done yet (it's okay!)")
    q3_pass = False
print()

# =========================
# SECTION 4: Loop Test
# =========================
print("QUESTION 4: Can you write a simple loop?")
print("-" * 60)
print("Task: Print numbers 1 to 5 using a for loop")
print()

# EXAMPLE: If you can do this:
# for i in range(1, 6):
#     print(i)

# TODO: Try to write the loop here (uncomment if you can):
# for i in range(1, 6):
#     print(i)

print()

# Rate yourself on this question:
# UNCOMMENT ONE:
# q4_answer = "I have no idea how to do this"
# q4_answer = "I know what a loop is but can't write it"
# q4_answer = "I can write it with help/Google"
# q4_answer = "I can write it easily"

q4_answer = "CHOOSE_ONE_ABOVE"
print(f"Your self-rating: {q4_answer}")
print()

# =========================
# SECTION 5: Function Test
# =========================
print("QUESTION 5: Can you write a function?")
print("-" * 60)
print("Task: Write a function that takes a number and returns double of it")
print()

# EXAMPLE: If you can do this:
# def double(n):
#     return n * 2

# TODO: Try to write the function (uncomment if you can):
# def double(n):
#     return n * 2

# Test it (uncomment after writing function):
# print(f"double(5) = {double(5)}")  # Should print 10

print()

# Rate yourself:
# UNCOMMENT ONE:
# q5_answer = "I don't know what a function is"
# q5_answer = "I know what it is but can't write it"
# q5_answer = "I can write it with help"
# q5_answer = "I can write it easily"

q5_answer = "CHOOSE_ONE_ABOVE"
print(f"Your self-rating: {q5_answer}")
print()

# =========================
# SECTION 6: Dictionary Test (Hash Map)
# =========================
print("QUESTION 6: Do you know what a dictionary/hash map is?")
print("-" * 60)

# UNCOMMENT ONE:
# q6_answer = "Never heard of it"
# q6_answer = "Heard of it, don't know how to use"
# q6_answer = "Can use with examples"
# q6_answer = "Comfortable with dictionaries"

q6_answer = "CHOOSE_ONE_ABOVE"
print(f"Your answer: {q6_answer}")
print()

# =========================
# SECTION 7: Problem Solving Test
# =========================
print("QUESTION 7: Can you solve this?")
print("-" * 60)
print("Task: Find the largest number in this list WITHOUT using max()")
print("numbers = [23, 45, 12, 67, 34, 89, 15]")
print()

# EXAMPLE: If you can solve it:
# nums = [23, 45, 12, 67, 34, 89, 15]
# largest = nums[0]
# for num in nums:
#     if num > largest:
#         largest = num
# print(f"Largest: {largest}")

# TODO: Try it yourself here

print()

# Rate yourself:
# UNCOMMENT ONE:
# q7_answer = "No clue how to approach this"
# q7_answer = "I understand the logic but can't code it"
# q7_answer = "I can code it with hints"
# q7_answer = "I solved it myself"

q7_answer = "CHOOSE_ONE_ABOVE"
print(f"Your self-rating: {q7_answer}")
print()

# =========================
# FINAL QUESTIONS
# =========================
print("=" * 60)
print("FINAL QUESTIONS")
print("=" * 60)
print()

print("QUESTION 8: How many hours per day can you REALISTICALLY commit?")
# UNCOMMENT ONE:
# daily_hours = "1-2 hours max (busy schedule)"
# daily_hours = "2-3 hours (normal schedule)"
# daily_hours = "3-4 hours (serious commitment)"
# daily_hours = "4+ hours (full-time learning)"

daily_hours = "CHOOSE_ONE_ABOVE"
print(f"Your answer: {daily_hours}")
print()

print("QUESTION 9: How many days per week?")
# UNCOMMENT ONE:
# days_per_week = "3-4 days (part-time)"
# days_per_week = "5 days (weekdays only)"
# days_per_week = "6 days (serious)"
# days_per_week = "7 days (extreme)"

days_per_week = "CHOOSE_ONE_ABOVE"
print(f"Your answer: {days_per_week}")
print()

print("QUESTION 10: What's your biggest fear?")
# UNCOMMENT ONE or write your own:
# fear = "I'm not smart enough"
# fear = "I'll fail and waste time"
# fear = "Everyone else is better than me"
# fear = "I won't be able to solve problems"
# fear = "I'll give up when it gets hard"
# fear = "Something else: I don't have enough time"  # ← You can customize this!

fear = "CHOOSE_ONE_ABOVE"
print(f"Your answer: {fear}")
print()

print("=" * 60)
print("NOW YOU KNOW HOW TO FILL IT OUT!")
print("=" * 60)
print()
print("Copy your answers to assessment.py and run it!")
