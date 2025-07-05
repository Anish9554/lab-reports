n = int(input("How many terms? "))
a, b = 0, 1
sequence = []

for _ in range(n):
    sequence.append(a)
    a, b = b, a + b

print("Fibonacci Sequence:", sequence)