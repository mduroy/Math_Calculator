# Math Calculator

Math Calculator is a Python-based utility that provides a suite of mathematical functions. It is designed for educational purposes, showcasing clean code practices, test-driven development, and integration with CI/CD tools like GitHub Actions and SonarCloud.

## Authors

Math Calculator and the surrounding development environment was developed by Matteo Duroy & Thomas Klapisz in the context of a python development project at ESTACA.

## Features

- **Arithmetic Operations**: Trigonometry calculations using Pythagoras' and Thales' theorems.
- **Robust Testing**: Comprehensive unit tests with over 85% code coverage.

## Getting Started

### Prerequisites

- Python 3.12 or later
- `pdm` (Python Dependency Manager)
- Optional: `pytest` and `pytest-cov` for local testing

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Math_Calculator.git
   cd Math_Calculator


2. Install dependencies using pdm:
    ```bash
    pdm install

## Running the Application
To use the math functions, you can directly import the module in your Python code:
    ```bash
    from src.math_calculator import add, subtract, multiply, divide
    result = add(2, 3)
    print(f"The result is {result}")

## Running Tests
Run the test suite with coverage reporting:
    ```bash
    pdm run pytest --cov=src --cov-report=xml

## Continuous Integration

This project uses GitHub Actions for CI/CD. The pipeline:

1. Runs the test suite.
2. Reports code coverage using pytest-cov.
3. Integrates with SonarCloud for code quality analysis.

## SonarCloud Integration

SonarCloud provides advanced code analysis and ensures high-quality code. 

Key Metrics
Code Coverage: 85%+
Maintainability: A
Reliability: A

![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=mduroy_Math_Calculator&metric=coverage)
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=mduroy_Math_Calculator)](https://sonarcloud.io/summary/new_code?id=mduroy_Math_Calculator)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=mduroy_Math_Calculator&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=mduroy_Math_Calculator)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=mduroy_Math_Calculator&metric=bugs)](https://sonarcloud.io/summary/new_code?id=mduroy_Math_Calculator)
