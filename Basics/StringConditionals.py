def StringConditionals():

    print("\nConditionals for String Case")
    text=input("Enter a string: ")
    if text.isalpha():

        if text.islower():
            print("The string is in lowercase")
        elif text.isupper():
            print("The string is in uppercase")
        else:
            print("Text is mixed")
    else:
        print("The string contains non-alphabetic characters")

    print("\nConditionals to check if known user")
    name=input("Enter your name: ")
    if name.lower() in ["alice", "bob"]:        
        print("Hello, ", name)
    else:
        print("I don't know you, ", name)

    print("\nConditionals for checking Password")
    password=input("Enter your password: ")
    if len(password)<6:
        print("Password is too short")
    else:
        if(password.find("@") != -1 or password.find("#") != -1 or password.find("$") != -1):
            print("Password is strong")
            if(password.find("123456") != -1 or password.find("password") != -1):
                print("Password is weak")
        else:
            print("Password is weak")

    print("\nConditionals for checking Vowel/Consonents")
    letter=input("Enter a letter: ")
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single alphabetic character.")
    else:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            print("The letter is a vowel")
        else:
            print("The letter is a consonant")

    print("Check if string is palindrome or not")

    word=input("Enter a word: " )
    word=word.lower()
    if word==word[::-1]:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")

    print("\nChecking the input type:")
    user_input=input("Enter anything: ")
    if user_input.isdigit():
        print("The input is a number")
    elif user_input.isalpha():
        print("The input is a string")
    else:
        print("The input is a mix of string and number or special characters")