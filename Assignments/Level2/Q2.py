input_list = [int(x) for x in input("Enter elements separated by space: ").split()]
unique_list = list(set(input_list))

print(f"Unique elements: {unique_list}")
