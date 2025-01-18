str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")
