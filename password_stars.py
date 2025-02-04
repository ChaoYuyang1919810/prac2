'''author chaoyuyang'''

# Set the minimum required length for the password
min_length = 10

# Ask the user to enter a password
password = input("Enter a password: ")

# Check if the password meets the minimum length requirement
while len(password) < min_length:
    print(f"Password must be at least {min_length} characters long.")
    password = input("Enter a password: ")

# Print asterisks equal to the length of the password
print("*" * len(password))