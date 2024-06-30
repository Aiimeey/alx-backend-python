Unittests and Integration Tests

This repository contains implementations of unit tests and integration tests for various Python functions and classes, focusing on robust testing practices and code quality. The tests are designed to ensure reliability and correctness across different scenarios and edge cases.

Overview

This project covers several tasks related to testing using the unittest framework and leveraging unittest.mock for mocking dependencies. It explores common testing patterns such as parameterization, fixture management, and mocking techniques essential for testing in isolation.

Project Structure

The tasks are organized as follows:

    Task 0-3: Implementing unit tests for functions like access_nested_map, get_json, and memoize, covering different input scenarios and expected behaviors.
    Task 4-7: Testing a GithubOrgClient class, mocking HTTP requests to the GitHub API, and validating expected responses and behaviors.
    Task 8-9: Integration testing GithubOrgClient methods using predefined fixtures, ensuring functionality across real-world scenarios.

Requirements

    Environment: Ubuntu 18.04 LTS with Python 3.7.
    Style: Code adheres to pycodestyle standards (version 2.5).
    Documentation: Comprehensive docstrings for all modules, classes, and functions.
    Testing: Extensive use of unittest and unittest.mock for unit and integration tests.
    Execution: All files are executable with necessary permissions.

Setup and Execution

To run the tests:

    Clone the repository:

Execute individual test files using:

    python -m unittest path/to/test_file.py

Learning Objectives

By completing this project, you will gain proficiency in:

    Distinguishing between unit tests and integration tests.
    Applying mocking techniques to isolate components for testing.
    Parameterizing tests to validate multiple scenarios efficiently.
