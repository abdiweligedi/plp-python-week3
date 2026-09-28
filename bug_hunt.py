count = 1
total = 0

# BUG: The while condition was missing a colon. Added a colon to make it valid Python syntax.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The loop originally used count < 5, which stopped at 4. Changed it to count <= 5 so that 5 is included.
# BUG: The original print statement tried to join a string and an integer with +. Changed it to use a comma so Python can print both.
print("Sum of 1 to 5 is:", total)

count = 1
total = 0

# BUG: The while condition was missing a colon. Added the colon.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Changed < to <= so the loop includes the number 5.
# BUG: Changed + total to a comma because total is an integer, not a string.
print("Sum of 1 to 5 is:", total)
