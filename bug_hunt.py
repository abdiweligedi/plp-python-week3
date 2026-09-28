count = 1
total = 0

# BUG: The while condition was missing a colon. Added the colon.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Changed < to <= so the loop includes the number 5.
# BUG: Changed + total to a comma because total is an integer, not a string.
print("Sum of 1 to 5 is:", total)
