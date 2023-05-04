#file: Range.py
#auth: Jotham King
#date: 5/2/2023
#func: practice ranges
#   JK 5/2/2023 added range examples
#   JK 5/3/2023 added more range examples

#print's "list" of numbers that "range" 0 - 9
numbers = list(range(10))
print(numbers)

#prints only number isted in count 4 in list
nums = list(range(5))
print(nums[4])

#bolean, true because 20 = 0, 20
print(range(20) == range(0, 20))

#print range of numbers, from 5 - 20, and list only ever 2nd number list
numbers1 = list(range(5, 20, 2))
print(numbers1)

#
nums1 = list(range(3, 15, 3))
print(nums1[2])

#
x = list(range(7, 3, -1))
print(x)


#
numbers3 = list(range(5, 10, 2))
print(numbers3)

#print "hello" 5 times
for i in range (5):
    print("hello")

#
for e in range (0, 20, 2):
    print(e)

#
for f in range (2005, 2011, 2):
    print(f)

#input to list range
a = int(input())
b = int(input())
list = list(range (a, b))
print(list)

#
x = int(range(0,100))
print(list[4])