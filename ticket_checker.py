age = int(input("How old are you? "))

is_adult = age >= 18

print("Is adult:", is_adult)

if is_adult:
    print("Adult ticket price: $20")
else:
    print("Child ticket price: $10")