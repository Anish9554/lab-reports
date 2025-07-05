armstrong_numbers = []

for num in range(100, 1000):
    digits = [int(d) for d in str(num)]
    total = sum(digit ** 3 for digit in digits)
    if total == num:
        armstrong_numbers.append(num)

print("Armstrong Numbers:", armstrong_numbers)