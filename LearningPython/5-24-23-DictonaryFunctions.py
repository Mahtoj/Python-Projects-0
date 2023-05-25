#file: 5-24-23-DictionaryFunctions.py
#auth: Jotham King
#date: 5/24/2023
#func: examples of dictonary functions

nums = {
    1: "one",
    2: "two",
    3: "Three",
}

#determine whether a key is in a dictonary using "in" and "not in"
print(1 in nums)
print("three" in nums)
print(4 not in nums)


#"get" function, if the key is not found in the dictonary  it returns another specified value instead
pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))