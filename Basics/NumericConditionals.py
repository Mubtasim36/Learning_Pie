def NumericConditionals():
    print("\nThe start of numeric conditional statements tutorial in Python")

    print("\nConditionals for positive, negative and zero numbers:")

    a=int(input("Enter a number: "))
    if a>0:
        print("The number is positive.")
    elif a<0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    print("\nConditionals for Even or odd numbers:")
    b=int(input("Enter another number: "))
    if b%2==0:
        print("The number input is even")
    else:
        print("The number input is odd")

    print("\nConditionals for smaller or larger numbers:")
    c=int(input("Enter 3rd number: "))
    d=int(input("Enter 4th number: "))
    if c>d:
        print("3rd number is larger than 4th number")
    elif c==d:
        print("3rd number is equal to 4th number")
    else:
        print("3rd number is smaller than 4th number")

    print("\nConditionals for checking if a number is in a range:")
    e=int(input("Enter a number to check if it is in the range of 1 to 10: "))
    if 1 < e < 10:
        print("The number is in range of 1 to 10")
    elif e==1 or e==10:
        print("The number is on the boundary of the range")
    else:
        print("The number is out of range of 1 to 10")

    print("\nConditionals for checking if a number is divisible by 3 and 5:")
    f=int(input("Enter a number to check if it is divisible by 3 and 5: "))
    if f%3==0 and f%5==0:
        print("The number is divisible by 3 and 5")
    elif f%3==0 and f%5!=0:
        print("Number is divisible by 3 but not 5")
    elif f%3!=0 and f%5==0:
        print("Number is divisible by 5 but not 3")
    else:
        print("Number is not divisible by 3 and 5")

    print("\nConditionals to see if input is a leap year or not:")
    year = int(input("Enter a year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
     print(f"{year} is a leap year.")
    else:
     print(f"{year} is not a leap year.")

    print("\nConditionals to see if input is a prime number or not:")
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number") 

    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not a prime number")
    else:
     for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")

    print("\nConditionals to check grade")
    marks=int(input("Enter your marks: "))
    if marks>100 or marks<0:
        print("Invalid marks")
    elif 0<marks<100:
        if marks>=90:
            print("Your grade is A+")
        elif 85<=marks<90:
            print("Your grade is A")
        elif 80<=marks<85:
            print("Your grade is A-")
        elif 75<=marks<80:
            print("Your grade is B+")
        elif 70<=marks<75:
            print("Your grade is B")
        elif 65<=marks<70:
            print("Your grade is C+")
        elif 60<=marks<65:
            print("Your grade is C")
        elif 55<=marks<60:
            print("Your grade is D+")
        elif 50<=marks<55:
            print("Your grade is D")
        else:
            print("Your grade is F")

    print("\nConditionals to check BMI")
    weight=float(input("Enter your weight in kg: "))
    height=float(input("Enter your height in meters: "))
    bmi=weight/(height**2)

    if bmi>25:
        print("You are overweight")
    elif 18.5<=bmi<=25:
        print("You are healthy")
    else:
        print("You are underweight")

    print("\nChecking quadrants")
    x=int(input("Enter value of X: "))
    y=int(input("Enter value of Y: "))

    if x>0 and y>0:
        print("The point is in the first quadrant")
    elif(x<0 and y>0):
        print("The point is in the second quadrant")
    elif(x<0 and y<0):
        print("The point is in the third quadrant")
    elif(x>0 and y<0):
        print("The point is in the fourth quadrant")
    else:
        print("The point is the center point")