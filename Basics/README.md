# Python Basics Learning Examples

## Overview
This folder contains beginner-friendly Python examples that introduce core programming concepts such as printing output, taking user input, performing arithmetic operations, assigning values to variables, and importing functions from another file.

## Concepts Covered
The examples in this folder demonstrate:
- Printing text to the console
- Accepting user input
- Working with variables
- Performing basic arithmetic operations
- Using integer division and exponentiation
- Importing and using functions from another Python file
- Basic string formatting with f-strings

## Learning Objectives
By working through these examples, learners will be able to:
- Write and run simple Python scripts
- Understand how user input works in Python
- Perform basic calculations using operators
- Organize code by separating helper functions into another file
- Recognize how Python programs are structured and executed

## File Descriptions
- main.py: The main script that demonstrates printing, input handling, arithmetic calculations, variable assignment, and importing the greet() function from helper.py.
- helper.py: A small helper module that stores a reusable greet() function used by main.py.

## How to Run the Examples
1. Open a terminal or command prompt.
2. Navigate to the Basics folder.
3. Run the main script:
   - On Windows: `python main.py`
   - On Linux/macOS: `python3 main.py`
4. Follow the prompts and enter values when requested.

## Expected Output
The program will print several messages and ask for input. A sample run with inputs such as "Alice" and numbers 10 and 5 might look like this:

```text
Hehe
Hello, World!
Enter anything: Hello
You entered:  Hello
Enter name: Alice
Hello,Alice!
Enter first number: 10
Enter second number: 5
Summation of the numbers is:  15
Subtraction of the numbers is:  5
Multiplication of the numbers is:  50
Division of the numbers is:  2.0
Integer Division of the numbers is:  2
Square of the numbers is:  100000
Summation of the numbers is:  73
Subtraction of the numbers is:  27
Multiplication of the numbers is:  1150
Division of the numbers is:  2.1739130434782608
This line is from the Helper.py file: Hello! Welcome to the program.
```

## Prerequisites
- Python 3.x installed on your system
- A terminal or command prompt
- Basic familiarity with navigating folders using the command line

## Notes
- The script uses `int()` for arithmetic, so the inputs for calculations should be whole numbers.
- The helper file must remain in the same folder as main.py for the import to work correctly.
- If you encounter an import error, make sure you are running the script from the Basics directory.
