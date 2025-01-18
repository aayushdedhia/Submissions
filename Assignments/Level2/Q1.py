list1 = [int(x) for x in input("Enter elements of list 1 separated by space: ").split()]
list2 = [int(x) for x in input("Enter elements of list 2 separated by space: ").split()]

common_elements = list(set(list1).intersection(set(list2)))
print(f"Common elements: {common_elements}")
