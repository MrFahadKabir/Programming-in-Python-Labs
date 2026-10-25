total = 0

for number in range(2, 1000):
    prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            prime = False
            break

    if prime:
        total = total + number

print("Sum of primes below 1000 =", total)