positive = 0
negative = 0
zero = 0

for _ in range(10):
    num = int(input("Enter an integer: "))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)