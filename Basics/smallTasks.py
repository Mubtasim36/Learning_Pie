def smallTasks():
    #This file is created for practice

    # Fibonacci
    a, b = 0, 1
    n = int(input("Enter the number of Fibonacci terms: "))

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print("\n")

    # Login/Register

    registered = ["AL", "Mubtasim"]
    registered_lower = [user.lower() for user in registered]

    print("Login")

    name = input("Enter your name: ")

    if name.lower() in registered_lower:
        print(f"Welcome back, {name}")

    else:
        print("User not found.")
        print("1. Register")
        print("2. Exit")

        option = int(input("Choose: "))

        if option == 1:

            new_user = input("Enter username: ")

            if new_user.lower() in registered_lower:
                print("User already registered.")

            else:
                registered.append(new_user)
                print(f"New user {new_user} registered.")
                print("Current users:", registered)

        elif option == 2:
            return

        else:
            print("Invalid option.")