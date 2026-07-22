def basics():

    #String things
    print("This is how to show a \' or a \" in a string by using a backslash before it and for a new line use \"\\n\" \nsee now?")
    print("Adding strings with strings is called concatenation. For example: " + "Hello" + "World")
    print("Repeating strings: For example: " + 2 * "Hello" + " Or you can do it like this: " + "Hello" * 3)

    Special_Concat=("You can add string that are next to each other using (') 'Hi' \'there' '!'")
    print(Special_Concat)

    Text1="Hello"
    Text2="World"
    Text3=Text1+" "+Text2+"Extra"
    print(Text3)

    #Indexing
    word="Hello"
    word3=word[0]+word[1]+word[4]+word[3]+word[-1]  #[-1] means last character, -2 means second last character and so on
    print(word3)

    word[:3]  #This will print the first three characters of the string
    word[2:4]  #This will print the characters from index 3 to 4
