"""
Python Skills Assessment - Be Honest!
Answer each question by uncommenting your answer.
Don't look up answers - this is to help YOU understand where you are.
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

# Uncomment ONE answer:
# background = "Never coded anything before"
# background = "Tried coding once or twice (tutorials)"
# background = "Took a programming course (any language)"
# background = "Coded in another language (Java/C++/JS)"
# background = "Professional programmer in another language"

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

# TODO: Write your code here
# my_name =

try:
    print(f"Result: {my_name}")
    q2_pass = True
except:
    print("❌ Not done yet")
    q2_pass = False
print()

# =========================
# SECTION 3: Lists Test
# =========================
print("QUESTION 3: Can you work with lists?")
print("-" * 60)
print("Task: Create a list of numbers 1 to 5, then print the 3rd element")
print()

# TODO: Write your code here
# numbers =
# third_element =

try:
    print(f"Your list: {numbers}")
    print(f"Third element: {third_element}")
    q3_pass = (third_element == 3)
    if q3_pass:
        print("✅ Correct!")
    else:
        print("❌ Not quite - the third element should be 3")
except:
    print("❌ Not done yet")
    q3_pass = False
print()

# =========================
# SECTION 4: Loop Test
# =========================
print("QUESTION 4: Can you write a simple loop?")
print("-" * 60)
print("Task: Print numbers 1 to 5 using a for loop")
print()

# TODO: Write your code here
# for ...

print()

# Rate yourself on this question:
# Uncomment ONE:
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

# TODO: Write your code here
# def double(n):
#     ...

# Test it (uncomment after writing function):
# print(f"double(5) = {double(5)}")  # Should print 10

print()

# Rate yourself:
# Uncomment ONE:
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

# Uncomment ONE:
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

# TODO: Write your code here

print()

# Rate yourself:
# Uncomment ONE:
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
# Uncomment ONE:
# daily_hours = "1-2 hours max (busy schedule)"
# daily_hours = "2-3 hours (normal schedule)"
# daily_hours = "3-4 hours (serious commitment)"
# daily_hours = "4+ hours (full-time learning)"

daily_hours = "CHOOSE_ONE_ABOVE"
print(f"Your answer: {daily_hours}")
print()

print("QUESTION 9: How many days per week?")
# Uncomment ONE:
# days_per_week = "3-4 days (part-time)"
# days_per_week = "5 days (weekdays only)"
# days_per_week = "6 days (serious)"
# days_per_week = "7 days (extreme)"

days_per_week = "CHOOSE_ONE_ABOVE"
print(f"Your answer: {days_per_week}")
print()

print("QUESTION 10: What's your biggest fear?")
# Uncomment ONE or write your own:
# fear = "I'm not smart enough"
# fear = "I'll fail and waste time"
# fear = "Everyone else is better than me"
# fear = "I won't be able to solve problems"
# fear = "I'll give up when it gets hard"
# fear = "Something else: __________"

fear = "CHOOSE_ONE_ABOVE"
print(f"Your answer: {fear}")
print()

# =========================
# INSTRUCTIONS
# =========================
print("=" * 60)
print("NEXT STEPS")
print("=" * 60)
print()
print("1. Fill in ALL the answers above")
print("2. Try to complete the coding tasks")
print("3. Save this file")
print("4. Run: python3 assessment.py")
print("5. Copy the ENTIRE output")
print("6. Show me the output")
print()
print("Based on your answers, I'll give you:")
print("  - Honest timeline (how many weeks you need)")
print("  - Personalized daily plan")
print("  - What to focus on")
print("  - Realistic expectations")
print()
print("Remember: This is NOT a test to pass. It's a tool to help YOU.")
print("Be honest so I can give you the RIGHT plan, not a fantasy plan.")
print()
print("=" * 60)
