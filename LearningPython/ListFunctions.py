#file: ListFunction.py
#auth: Jotham King
#date: 5/9/2023
#func: practice list functions

#example of 'len' function, which lets you get the number of items in a list
nums = [1, 3, 5, 2, 4]
print(len(nums))


#example of 'len' function, which lets you get the number of items in a list
letters = ["a", "b", "c"]
#add "d" to list of letters
letters += ["d"]
print(len(letters))
print(letters)


#len can be used in a string to return their character count/length
str = "some text"
x = len(str)
print(x)


x1 = "abc"
#multiply the string
x1 *= 2
#count the number of characters
print(len(x1))


#append() function is used to add an item to the end of the list
nums2 = [1, 2, 3]
#append 4 to the end of the num2 list of integers
nums2.append(4)
print(nums2)


#insert() inserts a new item at the given position in the list
words = ["python", "fun"]
words.insert(1, "is")
print(words)

#example
nums3 = [9,8,7,6,5]
#add 4 at the end of list
nums3.append(4)
#insert 11 in the 2 position
nums3.insert(2,11)
print(len(nums3))

#index finds the first occurrence of a list item and returns its index
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q'))

x = [2, 4, 5, 7, 4]
y = x.index(4)
print(y)


#max(list) returns the maximum value
#min(list) returns the minimum value

x1 = [1, 8, 42, 3]
print(min(x1))
print(max(x1))

nums1 = [1, 3, 5, 2, 4]
res = min(nums1) + max(nums1)
print(res)


#list.count(item) returns a count of how many times an item occurs in a list
#list.remove(item) removes an item from a list
#list.reverse() reverses items in a list
x3 = [2, 4, 6, 2, 7, 2, 9]
print(x3.count(2))

x3.remove(4)
print(x3)

x3.reverse()
print(x)


list5 = [8, 4, 2, 6]
list5.remove(2)
print(len(list5)+list5.count(6))


#write a program that will take an input and append it to the list
queue = ['John', 'Amy', 'bob', 'Adam']
uinput = input()
queue.append(uinput)
print(queue)


nums9 = [2,4,8,9,5]
nums9.insert(1,3)
nums9.remove(9)
nums9.insert(0, nums9.count(8))
print(nums[3])