#file: 5-15-23-ReturningfromFunctions.py
#auth: jotham king
#date: 5/15/2023
#func: number guessing game
#mods: jk 5/15/2023 version 1.0.0

#return value can be used later in the code
def sum(x, y):
    return x+y

res = sum(42,7)
print(res)

#example of return value
def foo(x,y):
    if x>y:
        return x
    else:
        return y

x = foo(4,7)
print(x)

#example of return function and an if statement

def max(x,y):
    if x >=y:
        return x
    else:
        return y

if max (6, 4) > 10:
    print("Yes")
else:
    print("Nope")

#example of how once you return a value from a function, it immediately stops being executed
def add_numbers(x,y):
    total = x + y
    return total
    #example of any code after return state won't be executed
    print("This won't be printed")

print(add_numbers(4, 5))

#a function can only return once, thus, if you need to return multiple values, you can use a list
def double(a, b):
    return[a*2, b*2]

x = double(6, 9)
print(x)

#
def calc(x, y):
    return[x+y,x*y]

res1 = calc(3,4)
print(res1[1])

#calc the area of a given rectangle

#sample input 7, 4
#sample output 28

def area(x,y):
    #calc area by multiplying width x height
    return x*y

w = int(input("Enter the rectangle's width: "))
h = int(input("Enter the rectangle's length: "))

print(area(w,h))

#example of 4 iterations, value of i ranges 0, 1, 2, 3
def sum(x):
    res = 0
    for i in range(x):
        res+=i
    return res

print(sum(4))