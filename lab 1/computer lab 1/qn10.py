dictionary = {}

while True:
    key = input("Enter key (or type 'done'): ")
    if key.lower() == 'done':
        break
    value = input("Enter value: ")
    dictionary[key] = value

search_key = input("Enter key to search: ")
if search_key in dictionary:
    print("Value:", dictionary[search_key])
else:
    print("Key not found.")