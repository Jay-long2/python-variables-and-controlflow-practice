age = int(input("Input your age here: "))
if 1 <= age < 18:
    print("You're a Minor")
elif  18 <= age <= 65:
    print("You're an Adult")
elif  age > 65:
    print("You're a Senior")
elif age<0:
    print("Enter a valid age number!!!")
