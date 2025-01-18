numbers = sorted([int(x) for x in input("Enter numbers separated by space: ").split()])

n = len(numbers)

if n % 2 == 0:
	median = (numbers[n // 2] + numbers[(n - 1) // 2]) / 2
else: 
	numbers[n // 2]

print(f"Median: {median}")
