list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = [x for x in list1 if x not in list2]
print("Result after removal:", result)