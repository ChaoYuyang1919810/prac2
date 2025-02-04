"""This module contains a function to calculate the area of a rectangle and
displays the result using the given height and width."""


# No external imports or constants needed for this simple example
#
def main():
    """Main function that orchestrates the program."""
    # Example input values for the height and width
    height = 5
    width = 10

    area = calculate_area(height, width)
    print(f"The area of the rectangle is: {area}")


def calculate_area(height, width):
    """This function will calculate the area of a rectangle."""
    return height * width


main()
