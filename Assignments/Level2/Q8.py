string = input("Enter a string: ").lower()
vowels = "aeiou"
 
count = sum(string.count(vowel) for vowel in vowels)
print(count)
