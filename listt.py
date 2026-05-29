#String oparations
#1.Concatination
"""string1=input("Enter the string1:")
string2=input("Enter the string2:")
print(string1+" "+string2)"""

#2.Repetation
"""String1=input("Enter the string:")
print(String1*3)"""

#3.Searching
"""String=input("enter the String:")
n=input("what u want to search:")
print(n in String)"""

#4.finding length
"""String=input("Enter the string:")
print(len(String))"""

#5.format string
"""name=input("Enter your name:")
print(f"My name is {name}")"""

#6.slicing
"""string="My name is Sonali"
print(len(string))
print(string[::])#My name is Sonali
print(string[1::])#y name is Sonali
print(string[1:5:])#y na
print(string[1:17:2])#ynm sSnl
print(string[1:17:])#y name is Sonali
print(string[-5:-2:1])#ona
print(string[::-1])#reverse,ilanoS si eman yM
print(string[-5:-2:-1])#no output"""

#String methods
#1.count()
"""string=input("Enter the string")
n=input("Enter the which char u want to count:")
print(string.count(n))"""

#2.len()
"""string=input("Enter the string:")
print(len(string))"""

#3.replace()
"""string1="Good moring"
string2=string1.replace("Good","bad")
print(string2)"""

#4.join()
"""a="#"
string="Welcome"
print(a.join("welcome"))"""

#4.startswith()
"""string="My name is Sonali"
print(string.startswith("my"))"""

#5.endswith()
"""string="My name is Sonali"
print(string.endswith("Sonali"))"""

#6.split()
"""string="My name"
s=string.split()
print(s)#['My', 'name']
a="-".join(s)
print(a)#My-name"""

#7.swapcase()
"""string1="ISM University"
print(string1.swapcase())#ism uNIVERSITY"""

#8.capitalize()
"""string1="ISM University"
print(string1.capitalize())#Ism university"""

#9.zfill()
"""string1="ISM"
print(string1.zfill(10))#0000000ISM"""

#10.upper()
"""string1="ism"
print(string1.upper())#ISM
"""
#11.lower()
"""string1="ism"
print(string1.lower())#ism"""

#isdigits()
"""string1="ism"
print(string1.isdigit())#False"""

#tile
"""string1="ism university"
print(string1.title())#Ism University"""

#list Oparations
#1.concatination
"""list1=eval(input("enter the list1 element:"))
list2=eval(input("enter the list2 element:"))
print(list1+list2)"""

#2.Reapetation
"""list=eval(input("enter the list to repeate:"))
print(list*2)"""

#3.Searching
"""list=eval(input("enter the list:"))
n=int(input("enter what u want to search:"))
print(n in list)
"""

#4.finding length
"""list=eval(input("enter the list:"))
print(len(list))"""

#5.slicing
list=[8,4,5,7,9,1]
print(list[::])#[8, 4, 5, 7, 9, 1]
print(list[1::])#[4, 5, 7, 9, 1]
print(list[2::])#[5, 7, 9, 1]
print(list[-1::])#[1]
print(list[-3:-1:])#[7, 9]
print(list[-4:-1:])#[5, 7, 9]
print(list[-4:-1:2])#[5, 9]
print(list[-4:-1:-2])#[]
print(list[-1:-4:-2])#[1, 7]


"""#list functions
#1.count()
list=[8,4,5,7,9,1,8]
print(list.count(8))

#2.len()
list=[8,4,5,7,9,1,8]
print(len(list))

#3.append()
list=[8,4,5,7,9,1,8]
list2=[8,5,4]
list.append(list2)
print(list)

#4.insert()
list=[8,4,5,7,9,1,8]
list.insert(2,10)
print(list)

#5.pop()
list=[8,4,5,7,9,1,8]
print(list.pop())
print(list.pop(4))

#6.remove()
list=[8,4,5,7,9,1,8]
list.remove(4)
print(list)

#7.sort()
list=[8,4,5,7,9,1,8]
list.sort()
print(list)

#8.extend()
list=[8,4,5,7,9,1,8]
list2=[8,5,4]
list.extend(list2)
print(list)

#9.reverse()
list=[8,4,5,7,9,1,8]
list.reverse()
print(list)

#10.sum()
list=[8,4,5,7,9,1,8]
list2=sum(list)
print(list2)

#11.min()
list=[8,4,5,7,9,1,8]
print(min(list))

#12.max()
list=[8,4,5,7,9,1,8]
print(max(list))"""