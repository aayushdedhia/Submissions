arr = [int(x) for x in input("Enter array elements separated by space: ").split()]
k = int(input("Enter the sum (K): "))

pairs = [(arr[i], arr[j]) for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] + arr[j] == k]

print(f"Pairs with sum {k}: {pairs}")
