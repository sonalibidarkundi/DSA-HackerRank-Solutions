"""a="how are you"
print(a[-1:-7:1])
"""

"""a="::"
print(a.join("*"))

"""

"""print("a"+"b"+"c")"""

#listOparations
#1.concatination
"""list1=eval(input("Enter the list1:"))
list2=eval(input("Enter the list1:"))
print(list1+list2)"""

#2.Repetation
"""list1=eval(input("Enter the list1:"))
r=int(input("Enter number how many time u want to repeate:"))
print(list1*r)
"""
#indexing
"""list1=eval(input("Enter the list1:"))
i=int(input("Enter the index u want to access:"))
print(list1[i])"""

#sliceing
#list=eval(input("Enter the list1:"))
list=[8,7,6,2,1]
print(list[-1::])
print(list[::-1])
print(list[::-2])
print(list[-3:-1:2])
print(list[-5:-4:])
print(list[-2:])

"""list=[4,7,4,6,8,4,0,3]
print(list[-3::])#8
print(list[-4:-1:])#[8,4,0]
print(list[-5:-3:])#[6,8]
print(list[-5:-1:])
print(list[0:-1:1])
print(list[0:-1:1])
print(list[-4:-3:1])
print(list[-1:-1:-1])
print(list[-3:-4:-1])
print(list[4:6:1])"""

#Finding the length
"""list=eval(input("Enter the list1:"))
print(len(list))"""

#searching using memebership oparations
"""list=eval(input("Enter the list1:"))
n=int(input("Enter the list1:"))
print(n in list)"""

#list Methods
#1.append
"""list1=[4,7,4,6,8,4,0,3]
list2,list3=4,5
list1.append(list2,list3)
print(list1)
print(list1[8])"""

"""list1=["sonali","aishu","shrusti","samarth"]
list2="soundarya","Arpita"
list1.append(list2)
print(list1)"""

#2.pop
"""list1=eval(input("Enter the list:"))
print(list1.pop())
print(list1)"""

"""list1=eval(input("Enter the list:"))
n=int(input("Enter the index value: "))
print(list1.pop(n))
print(list1)"""

#3.remove
"""list1=eval(input("Enter the list:"))
n=int(input("Enter the index value: "))
print(list1.pop(n))
print(list1)"""

#4.insert
"""list1=eval(input("Enter the list:"))
n=input("Enter the integer to insert: ")
m=int(input("Enter the index to insert: "))
list.insert(m,n)
print(list1)"""

#5.copy
"""list1=eval(input("Enter the list:"))
list2=" "
list1.copy()
print(list1)
print(list2)"""

#6.clear
"""list1=eval(input("Enter the list:"))
list1.clear()
print(list1)"""

#7.extend
"""list1=eval(input("Enter the list:"))
list2=eval(input("Enter the list:"))
list1.extend(list2)
print(list1)"""

#8.reverse
"""list1=eval(input("Enter the list:"))
list1.reverse()
print(list1)"""

#9.sort
"""list1=eval(input("Enter the list:"))
list1.sort()
print(list1)"""

#10.Sum
"""list1=eval(input("Enter the list:"))
print(sum(list1))
print(min(list1))
print(max(list1))"""

#index
"""list1=eval(input("Enter the list:"))
n=int(input("enter the index value:"))
print(list1.index(n))"""
