#file: Beginner_Tuorial.py
#auth: Jotham King
#date: 4/23/2023
#func: Write out beginner tutorial about learning Pyton
#mods: JK 4/23/2023 version 1.0.0 learning how python works, wrote a simple calc, output for a modulus, type ok to continue, bomb drop,
#      rjw 4/20/2023 version 1.0.2 add header

#import statement should be written at the top of your python file
import time

################################################################################################################

#python calculations
print("Python can calculate numbers, such as (3 * (3 + 3).")
print(3 * (3 + 3))
print("")


################################################################################################################


#python calculations with user input, return string as integer

print("Python can calculate a user input.")
multiply_five = int(input("Multiply 5 by: "))
print(5 * multiply_five)
print("")


################################################################################################################


#the modulus operator, allows you to divide and two values and the remainder is the output
print("a modulus operator, denoted as ' % ', will divide the value and output the remainder. Such as 10 / 3 will "
      "have a remainder of 1: ")
print("print(10 % 3) =", 10 % 3)


################################################################################################################


#user input only continue if user types ok
#repeat until user types ok
user_input = input("Type 👉 ok 👈 to continue: ")

#while true to create an infinite loop until user types ok
while True:

    #if user does not type ok
    while user_input != "ok":
        print("Invalid input. Please enter 👉 ok 👈.")
        user_input = input("Enter a value: ")

    #if user types ok, break while true infinity loop
    if user_input == "ok":
        print("Valid input.")
        break

#the following will print and delete i number of times defined by a range value. the value is then deleted to create a cool effect.
print("✈️")
for i in range(4):
  print("💣", end="")
  time.sleep(0.5)
  print("\b\b")

print("💥 that was an example of a 'while true' keyword. While true can create an infinite loop until")


################################################################################################################
