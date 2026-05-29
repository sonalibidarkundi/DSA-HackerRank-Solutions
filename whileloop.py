#*Lab Assignments*

#1. Write a program to print numbers from 1 to 10 using a while loop.
"""i=1
while(i<=10):
    print(i,end=" ")
    i+=1"""

#2. Print even numbers from 2 to 20 using a while loop.
"""i=2
while(i<=20):
    if i%2==0:
        print(i,end=" ")
    i+=1"""

#3. Print odd numbers from 1 to 15 using a while loop.
"""i=2
while(i<=15):
    if i%2==1:
        print(i,end=" ")
    i+=1"""

#4. Print numbers from 10 to 1 (reverse order) using a while loop.
"""i=10
while(i<=1):
    if i%2==0:
        print(i,end=" ")
    i-=1
"""

#5. Print your name 5 times using a while loop.
"""i=1
while i<=5:
    print("sonali")
    i+=1"""

#6. Print the multiplication table of 5 using a while loop.
"""i=1
while i<=50:
    if i%5==0:
        print(i)
    i+=1"""


#7. Print all multiples of 3 between 1 and 30 using a while loop.
"""i=1
while i<=30:
    if i%3==0:
        print(i)
    i+=1"""


#8. Print numbers from 50 to 60 using a while loop.
"""i=50
while i<=60:
    print(i)
    i+=1"""

#9. Take a number from user and print numbers from 1 to that number using a while loop.
"""num=int(input("Enter the number:"))
i=1
while i<=num:
    print(i)
    i+=1"""

#10. Print squares of numbers from 1 to 10 using a while loop.
"""i=1
while i<=10:
    print(i*i)
    i+=1"""

#11. Print the sum of numbers from 1 to 10 using a while loop.
"""i=1
sum=1
while i<=10:
    sum=sum+i
    i+=1
print(sum)"""


#12. Print the sum of even numbers between 1 and 20 using a while loop.
"""i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1
"""

#13. Print the sum of odd numbers between 1 and 15 using a while loop.
"""i=1
while i<=20:
    if i%2==1:
        print(i)
    i+=1"""

#14. Count how many digits a number has using a while loop.
"""number=input("enter the number:")
count=len(number)
print(count)"""

"""number=int(input("Enter the number:"))
count=0
while number>0:
    number=number//10
    count+=1
print("number of digits:",count)
"""

#15. Reverse a number using a while loop.
"""reversed_string=""
for char in string:
    reversed_string=char+reversed_string
print(reversed_string)"""

"""string="sonali"
reversed_string=""
i=len(string)-1
while i>=0:
    reversed_string+=string[i]
    i-=1
print(reversed_string)"""

#16. Print each digit of a number separately using a while loop.
"""number=int(input("Enter the numer:"))#123 1 2 3
temp=number
list=[]
while temp>0:
    rem=temp%10
    list.append(rem)
    temp=temp//10
# print(list) 
list.reverse()
# print(list) 
for x in list:
    print(x)  """

    


    
"""number=int(input("Enter the numer:"))
string=str(number)
print(string)
i=0
while i<len(string):
    print(string[i])
    i+=1"""



#17. Check if a number is palindrome using a while loop.
"""number=int(input("Enter the number:"))
rev=0
temp=number
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
print(rev)
if number==rev:
    print("number is palindrome")
else:
    print("Number is not palindrome")
"""



#18. Find factorial of a number using a while loop.
"""number=int(input("Enter the number:"))
fact=1
i=1
while i<=number:
    fact=fact*i
    i+=1
print(fact)"""
    


#19. Print Fibonacci series up to 10 terms using a while loop.
"""num=int(input("Enter the number:"))
f1=0
f2=1
i=1
while i<=num:
    print(f1)
    f3=f1+f2
    f1=f2
    f2=f3
    i+=1"""

#20. Print all numbers divisible by 5 between 1 and 100 using a while loop
"""i=1
while i<=100:
    if i%5==0:
        print(i)
    i+=1"""

#21. Keep asking the user for a password until they enter "admin".
"""while True:
    Password=input("Enter the password:")
    if Password=="admin":
        print("Your Password is correct")
        break"""
    

"""password=""
while password!="admin":
    password=input("enter the password")
   
print("correct")"""



#22. Keep reading numbers from the user until they enter 0.
"""while True:
    number=int(input("Enter the number:"))
    if number==0:
        print("number is 0")
        break"""

#23. Print menu options continuously until the user chooses "Exit".

"""print("Menu")
print("______________________")
print("Fruits")
print("Vegitable")
print("Satationary items")
print("soft drinks")
print("dresses")
print("Exit")
while True:
    choice=input("Enter the menu options to buy the product:")
    if choice=="Exit" or choice=="exit":
        break
    match choice:
        case "Fruits":print("Fruits is added to bag")
        case "Vegitable":print("veggies is added to bag")
        case "Satationary items":print("stationary itmes are added to bag")
        case "soft drinks":print("soft is added to bag")
        case "dresses":print("dresses is added to bag")
        case "Exit":print("Exit")
        
"""

#24. Take numbers from the user and find the largest number entered (stop on -1).
"""n=eval((input("ENter the number:")))
l=list(n)
large=l[0]
for i in l:
    if large<i:
        large=i
    print(large)"""


"""while True:
    n=input("Enter the list")
    large=str(n)
    for i in large:
        if i>large:
            large=i
    print(f"{large} is largest")
"""

"""largest=0
num=int(input("enter the number"))
while num!=-1:
    if num>largest:
        largest=num
    num=int(input("enter the number"))  
print(largest)      
"""


#25. Keep printing a countdown timer from 10 to 1 using a while loop.
"""count=0
i=10
while i>=1:
    count+=1
    print(i,count)
    i-=1
"""

#26. Simulate ATM: keep asking for PIN until user enters correct PIN (e.g., 1234).
"""while True:
    Pin=int(input("Enter the Pin:"))
    if Pin==1234:
        break"""


#27. Ask the user to enter marks until they enter -1, then print the average.
"""count=1
sum=1
Marks=int(input("Enter the marks:"))
while Marks!=-1:
    sum=sum+Marks
    avg=sum/count
    count+=1
    Marks=int(input("Enter the marks:"))
print(avg)"""


#28. Generate random numbers until number 5 appears (use while + random).

"""import random
import time
while True:
    number=random.randint(1,10)
    time.sleep(1)
    print(number)
    if number==5:
        break"""
     

#29. Keep adding numbers given by user until the sum reaches 100 or more
"""
sum=0
while sum<100:
    Marks=int(input("Enter the marks:"))
    sum=sum+Marks
print(sum)
"""

