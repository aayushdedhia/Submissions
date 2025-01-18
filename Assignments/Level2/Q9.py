try:
    elements = [int(x) for x in input("Enter list elements separated by space: ").split()]
    index = int(input("Enter an index to access: "))
    print(f"Element at index {index}: {elements[index]}")
except IndexError:
    print("Index out of range.")
