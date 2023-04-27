#file: PythonMadLibGame.py
#auth: Jotham King
#date: 4/26/2023
#func: write a MadLib Game where the madlib is random selected from a group of sentences.

import random
import time

#ask user to input place, name, adjective, and verb
place = input("Enter a place: ")
person = input("Enter a person's name: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")

#for loop to display each character, backspace, with a 0.25 second delay. will appear to be a loading animation
for character in ['←', '\b', '↖', '\b', '↑', '\b', '↗', '\b', '→', '\b', '↘', '\b', '↓', '\b', '↙', '\b', '☐', '\b', '☑']:
    print(character, end="")
    time.sleep(.25)

#display one character at a time with a 0.25 second delay
text = "MadLib Loaded."

for character in text:
    print(character, end="")
    time.sleep(.25)

#generate random number between 0 and 2
random_number = random.randint(0, 2)

while True:

    if random_number == 0:
        print("I went to the",place,"and saw",person,"\b. They were",verb,"so",adjective,"that I started",verb,"too!")
        break

    if random_number == 1:
        print(person,"went to",place,"and started",verb,"and I was",adjective,"to see.")
        break

    if random_number == 2:
        print(person,"went to the",place,"and saw a",adjective,"dog.")
        break

print("")
print("Thank you playing!")