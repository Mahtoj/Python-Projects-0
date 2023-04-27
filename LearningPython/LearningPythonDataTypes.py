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
            data_type = input("Which of the following would you like to see:"
                                   "\n •What is a string? Type str"
                                   "\n •What is an integer? Type int"
                                   "\n •What is an float? Type flt"
                                   "\n •Return to beginning? Type done"
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
                print(" ")
                print("An Integer is a data type that represents a whole numbers. This can be a postiive, negative, or zero. They can represent a variety of values, such as quantity, year, age, etc.")
                print(" •-100")
                print(' •0')
                print(" •print('100')")
                print(' •print("83")')
                print(" ")
                break

            elif data_type == "flt":
                print(" ")
                print("A Float is a data type that represents a floating-point number. This can be a positive, negative, or zero. they can repsent a price, speed of an object, quantiy, etc.")
                print(" •-83.00")
                print(' •0.00')
                print(" •print(float('-100'))")
                print("   ↳ -100.00")
                print(' •print(float("83"))')
                print("   ↳ 83.00")
                print(" ")
                break

            elif data_type == "done":
                break
    else:
        print("Invalid answer. Please try again.")

