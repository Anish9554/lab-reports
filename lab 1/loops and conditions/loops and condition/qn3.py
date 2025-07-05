n = int(input("Enter a number: "))
factorial = 1
i = n

while i > 0:
    factorial *= i
    i -= 1

print(f"Factorial of {n} is {factorial}")
