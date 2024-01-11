Python - Test-driven Development
Overview
This project focuses on Test-Driven Development (TDD) principles in Python. The goal is to write Python scripts and corresponding test cases to ensure code correctness. The project consists of several tasks, each targeting specific Python programming concepts.

Tasks
0. Integers Addition
Write a function that adds two integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats; otherwise, raise a TypeError exception
a and b must be casted to integers if they are floats
Returns an integer: the addition of a and b
No module imports are allowed
1. Divide a Matrix
Write a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats
Each row of the matrix must be of the same size; otherwise, raise a TypeError exception
div must be a number (integer or float); otherwise, raise a TypeError exception
div cannot be equal to 0; otherwise, raise a ZeroDivisionError exception
Returns a new matrix with elements divided by div
2. Say My Name
Write a function that prints "My name is <first name> <last name>."

Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings; otherwise, raise a TypeError exception
Prints the formatted string with the provided names
3. Print Square
Write a function that prints a square with the character '#.'

Prototype: def print_square(size):
size is the size length of the square; must be an integer
If size is less than 0, raise a ValueError exception
Prints the square using '#'
4. Text Indentation
Write a function that prints a text with 2 new lines after '.', '?', and ':'.

Prototype: def text_indentation(text):
text must be a string; otherwise, raise a TypeError exception
Prints the formatted text with 2 new lines after specified characters
5. Max Integer - Unittest
Write unittests for the function def max_integer(list=[]):.

Test file should be inside a folder named tests
Use the unittest module for testing
Test file should be executed using python3 -m unittest tests.6-max_integer_test
6. Matrix Multiplication
Write a function that multiplies two matrices.

Prototype: def matrix_mul(m_a, m_b):
Validate input matrices according to specified requirements
Raise exceptions for invalid input
Return a new matrix resulting from the multiplication of m_a and m_b
7. Lazy Matrix Multiplication
Write a function that multiplies two matrices using the NumPy module.

Prototype: def lazy_matrix_mul(m_a, m_b):
Test cases should be the same as in task 6, with new exception types/messages
Requires NumPy installation: pip3 install numpy==1.15.0
8. CPython #3: Python Strings
Create a function that prints Python strings.

Prototype: void print_python_string(PyObject *p);
Print the information about the Python string object
If p is not a valid string, print an error message
Note: This task involves C programming and uses the CPython API.
