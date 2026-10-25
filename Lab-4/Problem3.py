base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

if base == 0 and exponent < 0:
    print("Invalid exponent")
else:
    result = 1

    for i in range(abs(exponent)):
        result = result * base

    if exponent < 0:
        result = 1 / result

    print("Result =", result)