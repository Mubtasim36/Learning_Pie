def list_tutorial():
    print("\n")
    print("This is a tutorial for lists in Python")
    # Tutorial for Lists
    print("Creating list:")
    my_list = [1, 2, 3, 4, 5]
    print(my_list)  # printing the whole list
    print(my_list[3])  # printing the 4th element of the list
    print(my_list[2:4])  # printing elements from index 2 to 3
    print(my_list[-1])  # printing the last element of the list
    print("Adding and removing elements from the list:")
    my_list.append(6)  # adding an element to the list
    print(my_list)  # printing the whole list after changes

    my_list.remove(3)  # removing an element from the list
    print(my_list)  # printing the whole list after changes

    my_list[4] = 9  # changing the value of an element in the list
    print(my_list)  # printing the whole list after changes

    print("Working with strings and lists:")
    test_string = "Testing testing"
    # String lists
    colors = ["red", "green", "blue"]
    print(colors)  # printing the whole list
    rgb = colors
    print(rgb)  # printing the whole list with a new variable name
    print(id(test_string) == id(rgb))  # Checking if both variables point to the same list in memory
    colors.append("yellow")  # changing the value of an element in the list
    print(colors)  # printing the whole list after changes

    colors[0:1] = ["orange", "purple"]  # changing the value of an element in the list
    print(colors)  # printing the whole list after changes
    rgb[:] = []
    print(rgb)  # printing the whole list after changes
    print(len(colors))  # printing the length of the list

    print("Working with lists of lists:")
    animals = ["cat", "dog", "rabbit"]
    birds = ["parrot", "eagle", "sparrow"]
    wildlife = animals + birds  # combining two lists
    wildLives = [animals, birds]  # creating a list of lists
    print(wildlife)  # printing the whole list after changes
    print(wildLives)  # printing the list of lists
    print(wildlife[0])  # printing the first element of the list
    print(wildLives[0][1])  # printing the second element of the first list in the list of lists
    print(wildLives[1][1])  # printing the second element of the second list in the list of lists
