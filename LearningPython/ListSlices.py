#file: ListSlices.py
#auth: Jotham King
#date: 5/7/2023
#func: practice list slices
#   JK 5/7/2023

#two colon-separated indices return a new list contains all the values between the indices
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#print list elements from position 2 through position 6
print(squares[2:6])
#print list elements from position 3 through position 8
print(squares[3:8])
#print list elements from position 0 through position 1
print(squares[0:1])


#an additional example
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])


#if the first number in a slice is ommitted, it's taken to be the start of the list
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[:7])


#list first 2 elements
list = ["a", "b", "c", "d"]
a = list[0:2]
print(a)


sq = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sq[4:])


squared = [0, 1, 4, 9, 16, 25, 36, 49, 64]
#print every other element in list
print(squared[::2])
#print every 3rd element in list
print(squared[2:8:3])

#print every 4th element, starting at position 1
red = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(red[1::4])


#negative numbers can be used in slices and in this example the -1 will count from the end of the list
blue = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(blue[1:-1])

#negative numbers in slices example
green = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(green[7:5:-1])

#using [::-1] as a slice will reverse a list
nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res)

nums1 = [1, 2, 3, 4, 5, 6]
res = nums1[::-1]
print(res[2])


#string as an input and outputs the last character of that string
str = input()
print(str[-1])


nums2 = [1, 2, 3, 4, 5]
print(nums2[1:-1])

print("test")

list1 = [1,1,2,3,5,8,13]
print(list1[list1[4]])


x1 = [6, 4, 2, 9]
x1 = x1[::-1]
print(x1[0]+x1[2])
