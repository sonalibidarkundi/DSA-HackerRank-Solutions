"""#Bitwise oparation
#1.Bitwise AND
number1=45
number2=60
print(number1 & number2)
"""

"""#1.Bitwise OR
number1=45
number2=60
print(number1 | number2)"""

"""#1.Bitwise XOR
number1=45
number2=60
print(number1 ^ number2)"""

"""#Compliment(~)
x=5
print(~x)#6

y=-4
print(~y)#3
"""

"""#left shift and right shift
x=10
shift=4
print(shift<<x)
print(shift>>x)
print(x<<4>>x)"""

"""#Extra oparator
x=-5.2
print(abs(x))

x=5.0
print(abs(x))

a=10
b=5
c=2
print(divmod(a,b,c))#TypeError"""

"""#1.Write a program to add two numbers and print the result.
number1=int(input("Enter the number1-:"))
number2=int(input("Enter the number2-:"))
print(number1+number2)
"""

"""#2.Write a program to find the remainder when one 
# number is divided by another
number1=int(input("Enter the number1-:"))
number2=int(input("Enter the number2-:"))
print(number1%number2)"""

"""#3.Write a program to calculate the 
# square of a number using operators.
number1=int(input("Enter the number1-:"))
for i in range(number1):
    n=i**2
    print(f"{i}={n}")"""

"""#4.Write a program to swap two numbers without
#using a third variable.
a=5
b=4
print(a)
print(b)
print("Before swapping the value of a and b are:",a,b)
a,b=b,a
print(a)
print(b)
print("Before swapping the value of a and b are:",a,b)"""


"""#5.Write a program to check whether a 
# number is even or odd using operators.
n1=int(input("Enter the number"))
print("Even number" if (n1%2==0) else "Odd number")"""

"""#6. Write a program to find the 
# largest among two numbers using relational operators.
n1=10
n2=5
print(n1>n2)"""

"""#7. Write a program to 
# check whether a number is positive, negative, or zero.
number=int(input("enter the number:-"))
if number>0:
    print("positive")
elif number<0:
    print("Negative")
else:
    print("equal to zero")"""

"""#8.Write a program to check whether two numbers are equal or not.
n1=int(input("enter the number1:-"))
n2=int(input("enter the number2:-"))
if n1==n2:
    print("n1 is equal to n2")
else:
    print("n1 is not equal to n2")
"""

"""#9. Write a program to calculate area and perimeter of a rectangle.
length=int(input("Length of the rectangle:-"))
width=int(input("width of the rectangle:-"))
p=2*length+2*width
print("Perimeter of Rectangle:-",p)
"""

"""#10.Write a program to perform all arithmetic operations on two numbers.
n1=int(input("enter the number1:-"))
n2=int(input("enter the number2:-"))
print("Addition:-",n1+n2)
print("Subtraction:-",n1-n2)
print("multiplication:-",n1*n2)
print("Division:-",n1/n2)
print("Modulus:-",n1%n2)"""

"""#11.Write a program using assignment operators (+=, -=, *=, /=)
a=50
a+=10
a-=5
a*=2
a/=4
print(a)"""

"""#8.Write a program to check whether a person 
# is eligible to vote using relational operators.
age=int(input("Enter your age:-"))
if age >= 18:
    print("Person is eligible to vote")
else:
    print("Person is not eligible to vote")"""


"""#14. Write a program to demonstrate membership operators
# using a list.
list=[5,4,8,7,4,2]
print(4 in list)
print(10 in list)"""


"""#15.Write a program to demonstrate identity 
# operators using two variables.
a=50
b=20
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
"""

"""
#16.Write a program to convert string input into
#  integer and float using typecasting.
name="Sonali"
print(int(name))#ValueError
print(float(name))"""

"""n=int(input("Enter the number:-"))
print(int(n))
print(float(n))"""

"""#17.Write a program to perform bitwise
#AND, OR, XOR operations on two numbers.
n1=20
n2=50
print(f"Bitwise AND:{n1 & n2}\
      \nBitwise OR:{n1 | n2}\
      \nBitwise XOR:{n1^n2} ")"""

"""#Write a program to check whether a number
#lies between 1 and 100 using logical operators.
n=int(input("Enter the number:-"))
if n>=1 and n<=100:
    print("Number is lies between 1 and 100")
else:
    print("Number is not lies between 1 and 100")"""

"""n=232
print(2 in n)"""