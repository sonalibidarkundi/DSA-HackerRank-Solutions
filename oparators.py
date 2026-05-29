"""#1.	Arithmetic Operators 
num1=8
num2=2
print(f"Add:{num1+num2}\
\nSub:{num1-num2}\n Mul:{num1*num2}\n Div:{num1/num2}\
\nFloorDivision:{num1//num2}\n Power:{num1**4}")
"""

"""#Performing Arithmetic operators using list
list1=[4,5,6]
list2=[1,2,3]
print(f"Addition of list{list1+list2}")
#print(f"Subtraction of list{list1-list2}")#TypeError
#print(f"Multiplication of list{list1*5}")#TypeError
#print(f"Division of list{list1/list2}")#TypeError
#print(f"Floor division of list{list1//list2}")#TypeError
#print(f"power of list{list1**2}")#TypeError"""


"""#Comparsion Oparators/Relation oparation
n1=(input("Enter value of n1:"))
n2=(input("Enter value of n2:"))
print(f"Equal:{n1==n2}\nNot Equal:{n1!=n2}\
     \nlesser then:{n1<n2} \nlesser then equal:{n2<=n1}\
     \nGreater then:{n2>n1} \nGreater then equal:{n2>=n1}")
print(bin(4))
print(int(0b100))
print(int(0b101))"""

"""#Compareing of two string
name1="Sonali"
name2="Sonu"
print(ord("a"))#ord() used to convert char into ascii
print(ord("u"))
print(name1==name2)
print(name1>=name2)
print(chr(117))#chr() is used to converting the Ascii to char
"""

"""#Assigment oparator
n=5
n+=10 #15
n-=5 #10
n*=2 #20
n/=2 
#10 division operator in Python,
#and it always converts the result to a float.
print(n)
n//=3 #3
print(n)
print(n//3)"""




"""#Logical Oparator
a=100
b=200
c=7
print(f"AND:-{a and b and c}\
      \nOr:{a or b or c}\
      \nNOT:{not c}")"""


"""
#Membership oparator
tuple=(4,8,2,6)
print(40 in tuple)
print(4 in tuple)
print(40 not in tuple)
print(4 not in tuple)
"""


#Identity oparator
number1=40
number2=400
print(id(number1))
print(id(number2))

"""print(number1 is number2)
print(number1 is not number2)

name="sonali"
print("my name is"+ " "+name)

import math
a=5
b=2
print(math.ceil(a/b))

a=10
a+=50
a*=10
a/=2#300.0
a//10#300.0
print(a//10)#30.0

a=5
b=a
print(id(a))
print(id(b))

a=6
b=a
print(id(a))
print(id(b))

"""