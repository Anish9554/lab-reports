name_list = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
name_count = {}

for name in name_list:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

print("Name counts:", name_count)