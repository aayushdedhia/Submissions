temperatures = [float(x) for x in input("Enter temperature readings separated by space: ").split()]

average_temp = sum(temperatures) / len(temperatures)
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

print(f"Average Temperature: {average_temp:.2f}")
print(f"Highest Temperature: {highest_temp}")
print(f"Lowest Temperature: {lowest_temp}")
