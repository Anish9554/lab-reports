n = input("Enter a number: ")
if n == n[::-1]:
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")