import random

def determine_result(score):
    """Determine the result based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """Main function to handle user input and random score."""
    # Ask the user for their score and print the result
    score = float(input("Enter your score (0-100): "))
    result = determine_result(score)  # Use the function to determine the result
    print(f"Result: {result}")

    # Generate a random score between 0 and 100 and print the result
    random_score = random.uniform(0, 100)  # Generate a random float score
    print(f"Random score: {random_score:.2f}")
    result = determine_result(random_score)  # Use the same function to determine the result
    print(f"Result for random score: {result}")

if __name__ == "__main__":
    main()
