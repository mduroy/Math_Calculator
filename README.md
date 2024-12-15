## Authors

Math Calculator and the surrounding development environment was developed by Matteo Duroy & Thomas Klapisz in the context of a python development project at ESTACA.

# Math Calculator

Math Calculator is a Python project that provides tools for solving key geometric problems. Currently, the calculator can help with:

- **Thales' Theorem**
- **Pythagoras' Theorem**
- **Angle Calculations**

It is designed with clean code principles and includes unit tests to ensure reliability.

---

## Features

- **Thales' Theorem**: Calculates the properties of a circle inscribed in a right-angled triangle.
- **Pythagoras' Theorem**: Calculates the lengths of sides in right-angled triangles.
- **Angle Calculations**: Compute angles in geometric shapes, including right triangles.

---

## Getting Started

Follow the steps below to set up and use the Math Calculator on your local machine.

### Prerequisites

Ensure you have the following installed on your system:

1. **Python**: Version 3.12 or higher.
2. **PDM**: Python Dependency Manager. Install it via:
   ```bash
   pip install pdm
   ```
### Cloning the Repository
To get started, clone the repository from GitHub:
    ```bash
   git clone https://github.com/<your-username>/Math_Calculator.git
   cd Math_Calculator
    ```

### Installing Dependencies
Install all required dependencies using pdm:
    ```bash
   pdm install
    ```
This will create a virtual environment and install all necessary libraries listed in the pyproject.toml file.

### Using the Calculator
To use the Math Calculator, follow these steps:

1. Activate the virtual environment created by pdm:
    ```bash
   pdm venv activate
    ```
If this doesn't work, manually activate the virtual environment:
    ```bash
   source .venv/bin/activate  # For Linux/MacOS
   .venv\Scripts\activate     # For Windows
    ```
2. Place yourself in the src/mathcalculator folder using cd
3. Run the script using:
    ```bash
    python dummy.py
    ```

![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=mduroy_Math_Calculator&metric=coverage)
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=mduroy_Math_Calculator)](https://sonarcloud.io/summary/new_code?id=mduroy_Math_Calculator)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=mduroy_Math_Calculator&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=mduroy_Math_Calculator)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=mduroy_Math_Calculator&metric=bugs)](https://sonarcloud.io/summary/new_code?id=mduroy_Math_Calculator)
