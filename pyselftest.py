#!/usr/bin/python

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


def main():
    """
    Main function to demonstrate the usage of calculate_area function.
    """
    length = 10.0
    width = 6.0
    area = calculate_area(length, width)
    print(f"The area of the rectangle with length {length} and width {width} is {area}")


if __name__ == "__main__":
    main()

