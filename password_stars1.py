def get_password(min_length):
    """
    Prompt the user for a password and ensure it meets the minimum length.

    Parameters:
        min_length (int): The minimum allowed length for the password.

    Returns:
        str: A valid password entered by the user.
    """
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """
    Print asterisks matching the length of the password.

    Parameters:
        password (str): The password string whose length determines the number of asterisks.
    """
    print("*" * len(password))


def main():
    min_length = 8  # You can change this variable to set a different minimum length
    password = get_password(min_length)
    print_asterisks(password)


# this is the main call
if __name__ == "__main__":
    main()
