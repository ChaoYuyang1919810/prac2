def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")


def determine_result(score):
    """Return the result based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print stars based on the score."""
    print('*' * int(score))


def main():
    """Main function to run the menu system."""
    score = get_valid_score()  # Get a valid score before the menu loop.

    while True:
        print("\\nMenu:")
        print("G) Get a valid score")
        print("P) Print result")
        print("S) Show stars")
        print("Q) Quit")

        choice = input("Please choose an option: ").upper()

        if choice == "G":
            score = get_valid_score()  # Get a new valid score if selected.
        elif choice == "P":
            result = determine_result(score)  # Call the result function.
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)  # Print stars based on score.
        elif choice == "Q":
            print("Farewell! Thank you for using the program.")
            break  # Exit the loop and end the program.
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
