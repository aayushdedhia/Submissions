number = int(input("Enter a number: "))
divisors_sum = sum(i for i in range(1, number) if number % i == 0)

if divisors_sum == number:
    print(f"{number} is a Perfect Number")
else:
    print(f"{number} is not a Perfect Number")
