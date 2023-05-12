#file: StringFormatting.py
#auth: Jotham King
#date: 5/11/2023
#func: practice string formating

#
nums1 = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums1[0], nums1[1], nums1[2])
print(msg)

#
print("{0}{1}{0}".format("abra","cad"))

#example of naming the placholdser, instead of the index numbers
a = "{x}, {y}".format(x=5, y=12)
print(a)

str ="{a}, {b}, {c}".format(a=5, b=9, c=7)
print(str)

#join() joinas a list of string with another string as a seperator
x = ", ".join(["spam", "eggs", "ham"])
print(x)

#split() is the opposite of join(). It turns a string with a certain separator into a list.
str = "some test goes here"
x = str.split(' ')
print(x)

#replace() repalces one substring in a string with another
x1 = "Hello ME"
print(x1.replace("ME", "world"))

#lower() and upper() change the case of a string to a lowercase and uppercse
print("This is a sentence.".upper())
print("AN ALL CAPS SENTENCE".lower())


txt = "hello"
print(max(txt))