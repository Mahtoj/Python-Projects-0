#file: ListFunction.py
#auth: Jotham King
#date: 5/13/2023
#func: practice arguments

#functions can take arguments, which can be used to generate the function output
def exclamation (word):
    print(word + "!")

exclamation ("spam")


#function that prints double X
def print_double(x):
    print(2*x)

print_double(3)


#calling same function for different arguments
def exclamation(word):
    print(word + "!")

exclamation("spam")
exclamation("eggs")
exclamation("python")


#function adds 2 to x
def x(y):
    print(y+2)

x(5)


#example of function with more multiple arguments

def print_sum_twice(x, y):
    print(x + y)
    print(x + y)

print_sum_twice(5, 8)


#function that prints "yes" if the argument is an even number, and "no" otherwise

def even(x):
    if x%2 == 0:
        print("Yes")
    else:
        print("No")
