#*Assignments questions on break, continue and pass*

#1. Write a Python program to print numbers from 1 to 20, 
#but skip multiples of 3 using continue."""

"""for i in range(1,21):
    if i%3==0:
        continue
    print(i)"""

#2. Write a program to print numbers from 1 to 50 and stop the loop when the
 #number becomes 25 using break."""

"""for i in range(1,51):
    if i==25:
        break
    print(i)"""
#3. Write a program to print all even numbers between 1 and 30 using continue.

"""for i in range(1,31):
    if i%2!=0:
        continue
    print(i)"""

#4. Write a Python program to ask the user for numbers continuously
#and stop when the user enters -1 using break."""

"""n=int(input("Enter the number:"))
while True:
    if n==-1:
        break
    n=int(input("Enter the number:"))"""


#5. Write a program to print characters of a string except vowels using continue.
"""string=input("Enter the string:")
for i in string:
    if i=='a' or i=="e" or i=="i" or i=="o" or i=="u" or i=="A"or i=="E"or i=="I" or i=="O"or i=="U":
        continue
    print(i)"""

#6. Write a program to search for a particular number in a list. 
#If the number is found, display "Found" and stop searching using break."""

"""list=eval(input("Enter the list elements:"))
fount=int(input("Enter the element to be found:"))
for i in list:
    if fount in list:
        print("Element is found")
        break"""

#7. Write a program to print multiplication tables from 1 to 5, but skip
#the table of 3 using continue."""

"""for i in range(1,6):
    for j in range(1,11):
        if i==3:
            continue
        print(f"{i}*{j} = {i*j}")
    print("\n")"""

#8. Write a Python program to display numbers from 1 to 100, but stop 
#when a number divisible by both 5 and 7 is found using break."""

"""for i in range(1,101):
    if i%5==0 or i%7==0:
        break
    print(i)"""

#9. Write a program to print only positive numbers from a
#list and skip negative numbers using continue."""

"""list=eval(input("Enter te number of list:"))
for i in list:
    if i<=0:
        continue
    print(i)"""

#10. Write a Python program to create an empty loop using pass.
"""for i in [1,2,3,4]:
    pass"""
   


#11. Write a program using pass inside an if statement for future implementation.
"""i=1
while i<=10:
    if i%2==0:
        pass
    print(i)
    i+=1"""

#12. Write a Python program to check each character in a string and 
 #skip spaces using continue.

"""string=input("enter the string:")
for i in string:
    if i==" ":
        continue
    print(i,end="")"""

#13. Write a program to print numbers from 1 to 20
#and stop if the square of a number is greater than 200 using break."""


"""for i in range(1,21):
    square=i**2
    if square>200:
        break
    print(f"{i} = {square}")
"""