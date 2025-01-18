start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))

sum_of_odds = sum(number for number in range(start, stop + 1) if number % 2 != 0)

print(f"Sum of odd numbers between {start} and {stop}: {sum_of_odds}")
