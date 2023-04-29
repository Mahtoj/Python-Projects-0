#file: ListOperations.py
#auth: Jotham King
#date: 4/29/2023
#func: practice list operations.


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

#

words1 = ["spam", "egg", "spam", "sausage"]
print()