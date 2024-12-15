import math


def thales_theorem():
    """Implements Thales' Theorem.

    This function provides two functionalities:

    1. Verify if a triangle is a right triangle using Thales' Theorem.
    2. Calculate a missing length when hypotenuse and one side are provided.

    Returns:
        None
    """
    print("\nThales' Theorem:")
    print("1. Verify if a triangle is a right triangle.")
    print("2. Calculate a missing length.")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        x, y, z = map(
            float,
            input("Enter the lengths of the sides (x, y, hypotenuse z): ").split(),
        )
        if math.isclose(x**2 + y**2, z**2):
            print("The triangle is a right triangle.")
        else:
            print("The triangle is not a right triangle.")

    elif choice == "2":
        hypotenuse = float(input("Enter the length of the hypotenuse: "))
        base = float(input("Enter the length of the base: "))
        height = math.sqrt(hypotenuse**2 - base**2)
        print(f"The height of the triangle is {height:.2f}.")

    else:
        print("Invalid choice.")


def pythagoras_theorem():
    """Implements Pythagoras' Theorem.

    This function provides three functionalities:

    1. Calculate the hypotenuse given the other two sides.
    2. Calculate a leg given the hypotenuse and the other leg.
    3. Verify if three lengths form a right triangle.

    Returns:
        None
    """
    print("\nPythagoras' Theorem:")
    print("1. Calculate the hypotenuse.")
    print("2. Calculate a leg.")
    print("3. Verify if three lengths form a right triangle.")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        a = float(input("Enter the first leg: "))
        b = float(input("Enter the second leg: "))
        hypotenuse = math.sqrt(a**2 + b**2)
        print(f"The hypotenuse is {hypotenuse:.2f}.")

    elif choice == "2":
        hypotenuse = float(input("Enter the hypotenuse: "))
        leg = float(input("Enter one leg: "))
        other_leg = math.sqrt(hypotenuse**2 - leg**2)
        print(f"The other leg is {other_leg:.2f}.")

    elif choice == "3":
        a, b, c = map(float, input("Enter the three sides: ").split())
        if (
            math.isclose(a**2 + b**2, c**2)
            or math.isclose(b**2 + c**2, a**2)
            or math.isclose(c**2 + a**2, b**2)
        ):
            print("The sides form a right triangle.")
        else:
            print("The sides do not form a right triangle.")

    else:
        print("Invalid choice.")


def angle_calculations():
    """Performs angle calculations using trigonometric functions.

    This function provides three functionalities:

    1. Calculate an angle using sine.
    2. Calculate an angle using cosine.
    3. Calculate an angle using tangent.

    Returns:
        None
    """
    print("\nAngle Calculations:")
    print("1. Calculate an angle using sine.")
    print("2. Calculate an angle using cosine.")
    print("3. Calculate an angle using tangent.")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        opposite = float(input("Enter the length of the opposite side: "))
        hypotenuse = float(input("Enter the length of the hypotenuse: "))
        angle = math.degrees(math.asin(opposite / hypotenuse))
        print(f"The angle is {angle:.2f} degrees.")

    elif choice == "2":
        adjacent = float(input("Enter the length of the adjacent side: "))
        hypotenuse = float(input("Enter the length of the hypotenuse: "))
        angle = math.degrees(math.acos(adjacent / hypotenuse))
        print(f"The angle is {angle:.2f} degrees.")

    elif choice == "3":
        opposite = float(input("Enter the length of the opposite side: "))
        adjacent = float(input("Enter the length of the adjacent side: "))
        angle = math.degrees(math.atan(opposite / adjacent))
        print(f"The angle is {angle:.2f} degrees.")

    else:
        print("Invalid choice.")


def main():
    """Main function for the Geometry Calculator.

    This function provides a menu-driven interface for the following functionalities:

    1. Thales' Theorem
    2. Pythagoras' Theorem
    3. Angle Calculations
    4. Exit

    Returns:
        None
    """
    while True:
        print("\nGeometry Calculator:")
        print("1. Thales' Theorem")
        print("2. Pythagoras' Theorem")
        print("3. Angle Calculations")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            thales_theorem()
        elif choice == "2":
            pythagoras_theorem()
        elif choice == "3":
            angle_calculations()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
