# Configurable Python Auto-Grader (TO BE DONE LATER )

The Configurable Python Auto-Grader is a flexible tool designed to automatically grade Python code based on predefined test cases provided in a JSON input file. This tool allows educators, developers, and anyone conducting Python assessments to streamline the grading process while maintaining customization options.

## Features

- **JSON Input:** Define test cases and expected outcomes in a JSON file.
- **Configurability:** Easily customize grading criteria, input parameters, and expected outputs.
- **Scalability:** Support for grading multiple assignments in a batch.
- **Detailed Reports:** Generate detailed reports with results for each test case.

## Usage

1. **Installation:**

    ```bash
    pip install configurable-python-autograder
    ```

2. **Create JSON Input File:**

    Create a JSON file containing test cases. Example structure:

    ```json
    {
      "tests": [
        {
          "input": "2 3",
          "output": "5"
        },
        {
          "input": "5 5",
          "output": "10"
        }
      ]
    }
    ```

3. **Use the Auto-Grader:**

    ```python
    from auto_grader import AutoGrader

    # Instantiate the AutoGrader with the path to the JSON input file
    grader = AutoGrader("path/to/tests.json")

    # Provide the Python code to be graded
    python_code = """
    def add_numbers(a, b):
        return a + b
    """

    # Grade the code and get the results
    results = grader.grade(python_code)

    # Print the results
    print(results)
    ```

4. **Customization:**

    Modify the JSON input file to adjust test cases, add new ones, or change grading criteria. Refer to the [documentation](docs/README.md) for customization options.

## JSON Input File Structure

- **Tests Array:** Contains an array of test cases.
  - **Input:** Input parameters for the Python code (string).
  - **Output:** Expected output for the given input (string).

```json
{
  "tests": [
    {
      "input": "input_parameters",
      "output": "expected_output"
    },
    ...
  ]
}
```

## Contributing

Contributions are welcome! If you have suggestions, enhancements, or bug fixes, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to contributors and users who have provided valuable feedback and improvements.

---

*Note: This README provides a basic structure, and you may want to include more details based on your specific implementation.*