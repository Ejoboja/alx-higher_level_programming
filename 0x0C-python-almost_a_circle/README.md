0x0C. Python - Almost a Circle
This project is part of the Higher Level Curriculum and aims to prepare you for the AirBnB project. It covers a comprehensive review of Python, including topics such as:

Import
Exceptions
Class
Private attribute
Getter/Setter
Class method
Static method
Inheritance
Unittest
Read/Write file
args and kwargs
Serialization/Deserialization
JSON
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
A README.md file at the root of the project folder is mandatory
Code should use pycodestyle (version 2.8.*)
All files must be executable
Length of files will be tested using wc
Modules, classes, and functions should be documented
Python Unit Tests
Allowed editors: vi, vim, emacs
All test files should end with a new line
Test files should be inside a folder named "tests"
Use the unittest module
Test files should have a .py extension
All tests should be executed using python3 -m unittest discover tests
Tasks
0. If it's not tested, it doesn't work
All files, classes, and methods must be unit tested and PEP 8 validated.
1. Base class
Create the first class Base.
Initialize a folder named models with an empty file init.py inside to make it a Python package.
Create a file named models/base.py with a class named Base.
Implement a private class attribute __nb_objects and a class constructor.
The goal of this class is to manage the id attribute in future classes and avoid duplicating code.
2. First Rectangle
Write a class Rectangle that inherits from Base.
Create private instance attributes for width, height, x, y.
Implement a class constructor with appropriate validation and assignment logic.
3. Validate attributes
Update the Rectangle class by adding validation to setter methods and instantiation.
Raise exceptions for invalid input such as non-integer values and values less than or equal to 0.
4. Area first
Update the Rectangle class by adding a public method def area(self): that returns the area value of the Rectangle instance.
5. Display #0
Update the Rectangle class by adding a public method def display(self): that prints the Rectangle instance with the character #.
6. str
Update the Rectangle class by overriding the str method to return a formatted string representation.
7. Display #1
Improve the display method to take care of x and y coordinates.
8. Update #0
Add the public method def update(self, *args): to the Rectangle class that assigns arguments to attributes.
9. Update #1
Update the update method by changing the prototype to update(self, *args, **kwargs) to assign key/value arguments to attributes.
10. And now, the Square!
Write a class Square that inherits from Rectangle.
Implement a class constructor that calls the super class with appropriate attributes.
Use all attributes of Rectangle, as a Square is a special case of a Rectangle.
11. Square size
Update the Square class by adding public getter and setter methods for the size attribute.
12. Square update
Add the public method def update(self, *args, **kwargs) to the Square class that assigns arguments to attributes.
13. Square instance to dictionary representation
Add the public method def to_dictionary(self): to the Square class that returns a dictionary representation of a Square.
14. Dictionary to JSON string
Add the static method def to_json_string(list_dictionaries): to the Base class that returns the JSON string representation of a list of dictionaries.
15. JSON string to file
Add the class method def save_to_file(cls, list_objs): to the Base class that writes the JSON string representation of list_objs to a file.
16. JSON string to dictionary
