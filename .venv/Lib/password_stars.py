password = input("Enter password:")
password_length = 10
while len(password) < password_length:
    print("Error")
    password = input("Enter password:")
for i in range(len(password)):

    print("*",end = "")