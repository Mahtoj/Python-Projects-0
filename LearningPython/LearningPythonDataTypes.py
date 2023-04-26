#file: LearningPythonDataTypes.py
#auth: Jotham King
#date: 4/25/2023
#func: write a program that will allow user to select what data types to learn about
#mods: JK 4/25/2023 version 1.0.0 write a while true function that allows user to select data types. added string, int, float. Added
#

import time

#for loop to display each character, backspace, with a 0.25 second delay. will appear to be a loading animation
for character in ['←', '\b', '↖', '\b', '↑', '\b', '↗', '\b', '→', '\b', '↘', '\b', '↓', '\b', '↙', '\b', '☐', '\b', '☑']:
    print(character, end="")
    time.sleep(.25)

print()

#python lesson loaded will display one character at a time with a 0.25 second delay. text is a variable defining string "python lesson"
text = "Python Lesson Loaded."

for character in text:
    print(character, end="")
    time.sleep(.25)

print()

#while true will loop the question if the user would like to see a vairable lesson.
while True:
    answer = input("Would you like to see some examples of Python Variables? (yes/no): ")
    if answer == "no":
        break
    elif answer == "yes":
        print("I'm so glad to hear that!")
        print(" ")
        while True:
            data_type = input("Which of the following would you like to see"
                                   "\n •What is a string? Type str"
                                   "\n •What is an integer? Type int"
                                   "\n •What is an float? Type flt"
                                   "\n •What to quit? Type quit"
                                   "\nI want to see an example of: ")
            if data_type == "str":
                print(" ")
                print("A string is a sequence of characters. strings are usually enclosed in single or double quotes. Here's an example:")
                print(" •hello world")
                print(' •hello world')
                print(" •print('hello world')")
                print(' •print("hello world")')
                print(" ")
                break

            elif data_type == "int":
                print("....")
                break
            elif data_type == "flt":
                print("...")
                break
            elif data_type == "quit":
                break
    else:
        print("Invalid answer. Please try again.")