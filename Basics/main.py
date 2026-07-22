print("Welcome to my Python Learning Playground")
#Importing from other files
from helper import greet
print(greet) #print the function object
greet()

print("Choose Operation:1. Basics 2. Basic Calculation 3. Lists 4. Small Tasks 5. Numeric Conditionals 6. String Conditionals 7. Practice")
op=int(input("Enter which operation you want to perform: From 1-7: "))

if op==1:#Perform operation 1
    from Basics import basics
    basics()
elif op==2:#Perform operation 2
    from basicCalc import basicCalc
    basicCalc()
elif op==3:#Perform operation 3
    from lists import list_tutorial
    list_tutorial()
elif op==4:#Perform operation 4
    from smallTasks import smallTasks
    smallTasks()
elif op==5:#Perform operation 5 
    from NumericConditionals import NumericConditionals
    NumericConditionals()
elif op==6:#Perform operation 6
    from StringConditionals import StringConditionals
    StringConditionals()
elif op==7:
    from smallTasks import smallTasks
    smallTasks()