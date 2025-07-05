# Create a set of primes less than 50
prime_set = set()
for num in range(2, 50):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_set.add(num)

number = int(input("Enter a number to check: "))
if number in prime_set:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")