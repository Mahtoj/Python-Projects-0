#file: WhatsMyNumber.py
#auth: jotham king
#date: 4/18/2023
#func: number guessing game
#mods: rjw 4/19/2023 version 1.0.1 add input validy cheeck to prevent error crash
#      rjw 4/20/2023 version 1.0.2 add header


import random
import time

def is_valid_int(input):
  """
  This function tests if the input is a valid integer.

  Args:
    input: The input string to be tested.

  Returns:
    True if the input is a valid integer, False otherwise.
  """

  try:
    int(input)
    return True
  except ValueError:
    return False

# Generate a random number between 0 and 100
random_number = random.randint(0, 100)

# Repeat until true
while True:

    # User Input
    user_input = input("I'm thinking of a number between 0 - 100 🔮 what is it?: ")
    if not is_valid_int(user_input):

        print("You need to enter an integer value")
        print("\r")
        continue
    else:
        user_input = int(user_input)

    # User Input too low
    if random_number > user_input:
        print("🤬 You're too LOW!👎🏻 Hint:",random_number)
        print("\r")
        continue

    # User Input too high
    elif random_number < user_input:
        print("🤬 You're too HIGH!👎🏻 Hint:",random_number)
        print("\r")
        continue

    # User Input just right
    else:
        random_number = user_input
        print("✈️ Wow!")
        print("\r")
        break

for i in range(4):
  print("💣", end="")
  time.sleep(0.5)
  print("\b\b")

print("💥 You got it!")
