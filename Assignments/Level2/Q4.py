arr = [int(x) for x in input("Enter array elements separated by space: ").split()]
d = int(input("Enter the number of rotations (D): "))

rotated_array = arr[-d:] + arr[:-d]
print(f"Array after rotation: {rotated_array}")
