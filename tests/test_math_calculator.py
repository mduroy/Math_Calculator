import unittest
from unittest.mock import patch
from src.math_calculator.dummy import (
    thales_theorem,
    pythagoras_theorem,
    angle_calculations,
    main,
)


class TestMathCalculator(unittest.TestCase):
    def test_thales_theorem_verify_right_triangle(self):
        with patch("builtins.input", side_effect=["1", "3 4 5"]), patch(
            "builtins.print"
        ) as mock_print:
            thales_theorem()
            mock_print.assert_any_call("The triangle is a right triangle.")

    def test_thales_theorem_calculate_missing_length(self):
        with patch("builtins.input", side_effect=["2", "5", "4"]), patch(
            "builtins.print"
        ) as mock_print:
            thales_theorem()
            mock_print.assert_any_call("The height of the triangle is 3.00.")

    def test_thales_theorem_invalid_choice(self):
        with patch("builtins.input", side_effect=["3"]), patch(
            "builtins.print"
        ) as mock_print:
            thales_theorem()
            mock_print.assert_any_call("Invalid choice.")

    def test_pythagoras_theorem_calculate_hypotenuse(self):
        with patch("builtins.input", side_effect=["1", "3", "4"]), patch(
            "builtins.print"
        ) as mock_print:
            pythagoras_theorem()
            mock_print.assert_any_call("The hypotenuse is 5.00.")

    def test_pythagoras_theorem_calculate_leg(self):
        with patch("builtins.input", side_effect=["2", "5", "3"]), patch(
            "builtins.print"
        ) as mock_print:
            pythagoras_theorem()
            mock_print.assert_any_call("The other leg is 4.00.")

    def test_pythagoras_theorem_verify_triangle(self):
        with patch("builtins.input", side_effect=["3", "3 4 5"]), patch(
            "builtins.print"
        ) as mock_print:
            pythagoras_theorem()
            mock_print.assert_any_call("The sides form a right triangle.")

    def test_pythagoras_theorem_invalid_choice(self):
        with patch("builtins.input", side_effect=["4"]), patch(
            "builtins.print"
        ) as mock_print:
            pythagoras_theorem()
            mock_print.assert_any_call("Invalid choice.")

    def test_angle_calculations_sine(self):
        with patch("builtins.input", side_effect=["1", "3", "5"]), patch(
            "builtins.print"
        ) as mock_print:
            angle_calculations()
            mock_print.assert_any_call("The angle is 36.87 degrees.")

    def test_angle_calculations_cosine(self):
        with patch("builtins.input", side_effect=["2", "4", "5"]), patch(
            "builtins.print"
        ) as mock_print:
            angle_calculations()
            mock_print.assert_any_call("The angle is 36.87 degrees.")

    def test_angle_calculations_tangent(self):
        with patch("builtins.input", side_effect=["3", "3", "4"]), patch(
            "builtins.print"
        ) as mock_print:
            angle_calculations()
            mock_print.assert_any_call("The angle is 36.87 degrees.")

    def test_angle_calculations_invalid_choice(self):
        with patch("builtins.input", side_effect=["4"]), patch(
            "builtins.print"
        ) as mock_print:
            angle_calculations()
            mock_print.assert_any_call("Invalid choice.")

    def test_main_menu_thales(self):
        with patch("builtins.input", side_effect=["1", "2", "5", "4", "4"]), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("The height of the triangle is 3.00.")

    def test_main_menu_exit(self):
        with patch("builtins.input", side_effect=["4"]), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("Goodbye!")

    # Additional tests for thales_theorem
    def test_thales_theorem_invalid_triangle(self):
        with patch("builtins.input", side_effect=["1", "2 2 5"]), patch(
            "builtins.print"
        ) as mock_print:
            thales_theorem()
            mock_print.assert_any_call("The triangle is not a right triangle.")

    # Additional tests for pythagoras_theorem
    def test_pythagoras_theorem_invalid_triangle(self):
        with patch("builtins.input", side_effect=["3", "1 1 5"]), patch(
            "builtins.print"
        ) as mock_print:
            pythagoras_theorem()
            mock_print.assert_any_call("The sides do not form a right triangle.")

    # Additional tests for main
    def test_main_invalid_choice(self):
        with patch("builtins.input", side_effect=["5", "4"]), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("Invalid choice. Please try again.")


if __name__ == "__main__":
    unittest.main()
