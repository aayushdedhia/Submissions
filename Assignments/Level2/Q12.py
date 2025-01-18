username = input("Enter your username: ")
password = input("Enter your password: ")

for i in range(3):
    retype_password = input("Re-Type your password: ")
    if retype_password == password:
        print("Login successful!")
        break
    else:
        print("Incorrect password. Try again.")
else:
    print("Too many failed attempts.")
