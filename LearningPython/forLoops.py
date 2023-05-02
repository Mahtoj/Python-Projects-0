#file: forLoops.py
#auth: Jotham King
#date: 5/1/2023
#func: practice for loops
#   JK 5/1/2023 added more list operations examples

print("Example #1")
#add "!" to end of each item in list
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")
print("")

print("Example #2")
letters = ['a', 'b', 'c']
for x in letters:
    print(x)
print("")

#muiltiply each value by 2
print("Example #3")
nums1 = [4,7,3,1]
for y in nums1:
    print(y*2)
print("")

#muiltiply each value by 2
print("Example #4")
str = "testing lop loops"
count = 0

for x in str:
    if x == 't':
        count += 1
print(count)
print("")

#loops breaks once the process loops to 'e'
print("Example #5")
text1 = "some text"
for z in text1:
    if z == 'e':
        break
    print(z)
print("")

#loop break example, % is a modelo sign, example 3%2 output is 1
# (2%2==1 and 2>4) false.
# (3%2==1 and 3>4) false.
# (4%2==1 and 4>4) false.
# (5%2==1 and 5>4) true.
print("Example #6")
list2= [2,3,4,5,6,7]

for x in list2:
    if(x%2==1 and x>4):
        print(x)
        break

print("")

print("Example #7")
x = [42,8,7,1,0,124,8897,555,3,67,99]
sum1 = 0

for num3 in x:
    sum1 += num3

print(sum1)


print("Example #8")
nums5=[1,2,3,4]
res5=0

for x in nums5:
    if x%2==0:
        continue
    else:
        res5 +=x

print(res5)