number = int(input("Enter a number: "))

if number < 0:
    print("Enter a non-negative number")
else:
    while number >= 0:
        print(number)
        number = number - 1