#Welcome to ISM
print(__doc__)
print(__name__)

x="a"
#print(int(x)) # ValueError 
print(ord("A")) 

n=6
#print(n,type(n))
binnumber=bin(n)
print(binnumber)

#=========================================================================

n=eval(input("Enter a Number:"))
print(n,type(n))

#Collection Related Data Types
#1.List
List1=[1,2,3.0,"Sonali",True]
print(List1,type(List1))

#Accessing List Elements
#print(List1[])#SyntaxError

#updateing list elements
List1[1]=100
print(List1)

#appending elements to List
List1.append("ISM")
print(List1)

#Printing List inside the List
List1.append([1,2,3])
print(List1)

#Accessing list elements inside the list
print(List1[6][-1])

#Tuple inside the list
list2=[("Sonali","Shrusti","samarth"),5,10]
print(list2,type(list2))
#Accessing tuple elements inside the list
print(list2[0],type(list2[0]))

#set inside the List
list1=[{2,5},4,5]
print(list1,type(list1))

#dictionary inside the list
list1=[{2,5},4,5,{"name":"Sonali"}]
print(list1,type(list1))

del list1[2]
print(list1)

#=========================================================================

#2.Tuple
Tuple1=([1,2,3.0],"Sonali",True,5,5,{"name":"Sonali"})
print(Tuple1,type(Tuple1))

#accessing tuple elements
print(Tuple1[0])
print(type(Tuple1[0]))

#Updating tuple elemets
Tuple1[0][0]=100
print(Tuple1)

Tuple1[1]="ISM"
print(Tuple1)#TypeError

print(Tuple1[6])#IndexError

#set inside the tuple
#Tuple1=([1,2,3.0],"Sonali",True,5,5{8,9,8})
print(Tuple1)#SyntaxError

#Deleting tuple elements
del Tuple1[0]
print(Tuple1)#TypeError

#=========================================================================


#3.Sets 
#Tuple inside the set is allowed
Set1={(5,8,4),"ISM",5.0,5.0}
print(Set1,type(Set1))

#List inside the set is not allowed
Set2={[5,8,4],"ISM",5.0}
print(Set2,type(Set2))

#sets are unordered and unindexed
print(Set1[0])#TypeError

# sets returns a unique value
print(Set1)

#Accessing set Elements
for i in Set1:
    print(i)

#=========================================================================


#4. Dictionary
Dict={"name":"Sonali","age":25}
print(Dict,type(Dict))

#Accessing dictionary elements
print(Dict["name"])
print(Dict["age"])

#Updating Dictinary elements
Dict["name"]="ISM"
print(Dict)

#Adding new Key value pair to the dictionary
Dict["area"]="Bengaluru"
print(Dict)

#Deleting dictionary Elements
del Dict["age"]
print(Dict)

#taking input from user and storing in dictionary
name=input("Enter your name:")
age=int(input("enter your age:"))
username=({"name":name,"age":age})
print(username,type(username))

#takeing list inside the dictionary
Dict={"name":["Sonu","Aishu"],"marks":[90,95]}
print(Dict["name"][-1],type(Dict))

#==================================================================


#Type casting 
#Integer
n=50
print(float(n),type(float(n)))
print(str(n),type(str(n)))
print(bool(n),type(bool(n)))
print(complex(n),type(complex(n)))
print(bin(n),type(bin(n)))
print(oct(n),type(oct(n)))
print(hex(n),type(hex(n)))
#print(list(n),type(list(n))) #TypeError
#print(tuple(n),type(tuple(n))) #TypeError
#print(set(n),type(set(n))) #TypeError
#print(dict(n),type(dict(n))) #TypeError

#STring
#name="Sonali"
#print(int(name),type(int(name)))#ValueError
#print(float(name),type(float(name)))
#print(str(name),type(str(name)))
#print(bool(name),type(bool(name)))#True
#print(complex(name),type(complex(name)))

#List
#n=["Sonali","shrusti","Samarth"]
#print(int(n),type(int(n)))#TypeError
#print(float(n),type(float(n)))#TypeError
#print(bool(n),type(bool(n)))
#print(tuple(n),type(tuple(n)))
#print(set(n),type(set(n)))
#print(list(n),type(list(n)))
#print(dict(n),type(dict(n)))#valueError

#Tuple
#n=("Sonali","shrusti","Samarth")
#print(int(n),type(int(n)))#TypeError
#print(float(n),type(float(n)))#TypeError
#print(bool(n),type(bool(n)))
#print(tuple(n),type(tuple(n)))
#print(set(n),type(set(n)))
#print(list(n),type(list(n)))
#print(dict(n),type(dict(n)))#valueError

#Sets
#n={"Sonali","shrusti","Samarth"}
#print(int(n),type(int(n)))#TypeError
#print(float(n),type(float(n)))#TypeError
#print(bool(n),type(bool(n)))
#print(tuple(n),type(tuple(n)))
#print(set(n),type(set(n)))
#print(list(n),type(list(n)))
#print(dict(n),type(dict(n)))#valueError

#dictionary
#n={"name":"Sonali","age":22}
#print(bool(n),type(bool(n)))
#print(tuple(n),type(tuple(n)))
#print(set(n),type(set(n)))
#print(list(n),type(list(n)))
#print(dict(n),type(dict(n)))#valueError

