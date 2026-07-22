# Python Basics Learning Examples

## Overview
This folder contains beginner-friendly Python examples that introduce core programming concepts such as printing output, taking user input, performing arithmetic operations, assigning values to variables, importing functions from another file, and working with lists.

## Concepts Covered
The examples in this folder demonstrate:
- Printing text to the console
- Accepting user input
- Working with variables
- Performing basic arithmetic operations
- Using integer division and exponentiation
- Importing and using functions from another Python file
- Basic string formatting with f-strings
- Creating, indexing, slicing, and modifying lists
- Using lists of lists and list aliasing

## Learning Objectives
By working through these examples, learners will be able to:
- Write and run simple Python scripts
- Understand how user input works in Python
- Perform basic calculations using operators
- Organize code by separating helper functions into another file
- Work with Python lists and understand common list operations
- Recognize how Python programs are structured and executed

## File Descriptions
- main.py: The main script that demonstrates printing, input handling, arithmetic calculations, variable assignment, importing the `greet()` function from helper.py, and calling `list_tutorial()` from lists.py.
- helper.py: A small helper module that stores a reusable `greet()` function used by main.py.
- lists.py: A list tutorial module that demonstrates list creation, indexing, slicing, appending, removing, list aliasing, clearing, and nested lists.

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
This is how to show a ' or a " in a string by using a backslash before it and for a new line use "\n" 
see now?
Adding strings with strings is called concatenation. For example: HelloWorld
Repeating strings: For example: HelloHello Or you can do it like this: HelloHelloHello
You can add string that are next to each other using (') 'Hi' 'there' '!'
Hello WorldExtra
Hello
Hello, World!
This line is from the Helper.py file: Hello! Welcome to the program.

This is a tutorial for lists in Python
Creating list:
[1, 2, 3, 4, 5]
4
[3, 4]
5
Adding and removing elements from the list:
[1, 2, 3, 4, 5, 6]
[1, 2, 4, 5, 6]
[1, 2, 4, 5, 9]
Working with strings and lists:
['red', 'green', 'blue']
['red', 'green', 'blue']
False
['red', 'green', 'blue', 'yellow']
['orange', 'purple', 'blue', 'yellow']
[]
4
Working with lists of lists:
['cat', 'dog', 'rabbit', 'parrot', 'eagle', 'sparrow']
[['cat', 'dog', 'rabbit'], ['parrot', 'eagle', 'sparrow']]
cat
dog
eagle
```

## Prerequisites
- Python 3.x installed on your system
- A terminal or command prompt
- Basic familiarity with navigating folders using the command line

## Notes
- The script uses `int()` for arithmetic, so the inputs for calculations should be whole numbers.
- The helper file must remain in the same folder as main.py for the import to work correctly.
- The lists file must remain in the same folder as main.py for `list_tutorial()` to be imported and executed.
- If you encounter an import error, make sure you are running the script from the Basics directory.
