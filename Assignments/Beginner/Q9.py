input_list = [int(x) for x in input("Enter list elements separated by space: ").split()]
frequency = {item: input_list.count(item) for item in set(input_list)}

print(f"Frequency count: {frequency}")
