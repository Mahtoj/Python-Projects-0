#file: 4-29-23-ListOperations.py
#auth: Jotham King
#date: 4/29/2023
#func: practice list operations.
#   JK 5/1/2023 added more list operations examples


#list of items
nums = [5, 8, 2]
#change item in list, nums[position] = change to variable
nums[1] = 42
print(nums)


#new example#################

#list of items
nums1 = [1,2,3,4,5]
#change position 3 to match variable in position 1. Variable 4 is now 2
nums1[3] = nums1[1]
print(nums1[3])


#new example#################

#concatenate two lists
nums2 = [1, 2, 3]
print(nums2 + [4, 5, 6])

#new example#################

x = [2, 4]
x += [6, 8]
#calculate position 2 (6) / position 0 (2) = 3
print(x[2]//x[0])

#new example#################

#example of type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#new example#################

#example of list()

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

a = [2, 4]
a = a * 3
print(a[3])

#new example#################

#search for value in list, return true or false

words1 = ["spam", "egg", "spam", "sausage"]
print("spam" in words1)
print("egg" in words1)
print("tomato" in words1)

#new example#################

l = [2, 4]
l = l * 2
print(l[3])

#new example#################

nums1=[10,9,8,7,6,5]
nums1[0] = nums1[1]-5
if 4 in nums1:
    print(nums1[3])
else:
    print(nums1[4])

#new example#################

j = "hello world"

if "world" in x:
    print(yes)

#Not operator#################

#not operator can be used in one of the following ways
nums2 = [1, 2, 3]
print(not 4 in nums2)
print(4 not in nums2)
print(not 3 in nums2)
print(3 not in nums2)

#User Inpuit#################

g = [1, 2, 3, 4, 5, 6]

userinput = int(input("Write Input:"))
if userinput in g:
    print("Bingo")