user_input = input("Enter a string: ")

alphabets = 0
digits = 0

for char in user_input:
	if char.isalpha():
		alphabets += 1
	elif char.isdigit():
		digits += 1

print(f"Alphabets: {alphabets} & Number: {digits}")
