'''
#1.Identifiers can contains alphabets,digits,underscore
Name_52="Sonali"
print(Name_52)


#2.Identifiers can not start with digits
8Name="Sonali"
print(8Name)
# Its shows the error 


#3.Identifiers can not be a Keywords
import keyword
print(dir(keyword))

['__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__',
'__spec__', 'iskeyword', 'issoftkeyword', 'kwlist', 'softkwlist']

print(keyword.kwlist)
print(len(keyword.kwlist))


#3.Identifiers can not be a Keywords
def=" sonali"
print(def)

#4.identifiers is case-sensitive
name="Sonali"
Name="Sonu"
NaMe="Shrusti"
namE="Samarth"
print(name,Name,NaMe,namE)

#5.identifiers can not contain special charecters
@name="sonali"
$name="sonali"

#Syntax error

#6.No length limit for identifiers
Name="Sonali"
Nameeeeeeeeeeeeeeeeeeeeeeeeeee="Sonali"
print(Name,Nameeeeeeeeeeeeeeeeeeeeeeeeeee)

#7.identifers should starts with single underscore and double underscore
_name="sonali"
__name="Sonali"
print(_name,__name)


_num1=10
__num2=20
print(_num1+__num2)

___name="sonali"
print(___name)

#input/output functions
Name=input("Enter your name:")
print("My name is " + Name)

Num1=int(input("First numeber:"))
Num2=int(input("Second number:"))
print(f"The sum is: {Num1 + Num2}")

Name="Sonali"
print(f"{Name}")


#2.Identifiers can not start with digits
8Name="Sonali"
print(8Name)
# Its shows the error 



#3.Identifiers can not be a Keywords
import keyword
print(dir(keyword))

['__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__',
'__spec__', 'iskeyword', 'issoftkeyword', 'kwlist', 'softkwlist']

import keyword
n=keyword.kwlist
print(n)
print(n.count('True'))
print(len(keyword.kwlist))


import keyword
print(dir(__doc__))
print(keyword.iskeyword("True"))
print(dir(keyword.softkwlist))
'''
