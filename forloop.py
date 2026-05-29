#Lab Assignments

#1. Print numbers from 1 to 10 using a for loop.
"""for i in range(1,11):
    print(i)"""

#2. Print numbers from 10 to 1 using a for loop.
"""for i in range(10,0,-1):
    print(i)"""

#3. Print even numbers from 1 to 20.
"""for i in range(1,21):
    if i%2==0:
        print(i)
    """

#4. Print odd numbers from 1 to 30.
"""for i in range(1,21):
    if i%2!=0:
        print(i)"""

#5. Print the multiplication table of 5 using a for loop.
"""for i in range(1,50):
    if i%5==0:
        print(i)"""

#6. Print each character in a string using a for loop.
"""string=input("Enter the string:")
for i in string:
    print(i)"""

#7. Print each element in a list using a for loop.
"""list=eval(input("Enter the list element:"))
for i in list:
    print(i)"""

#8. Print the sum of numbers from 1 to 50.
"""sum=1
for i in range(1,51):
    sum=sum+i
print(sum)"""

#9. Print the sum of all items in a list.
"""list=eval(input("Enter the list element:"))
for index,i in enumerate(list):
    print(index,i)"""

#10. Print the factorial of a number using a for loop.
"""Number=int(input("Enter the element:"))
fact=1
for i in range(1,Number+1):
    fact=fact*i
print(fact)
"""
#11. Count vowels in a string using a for loop.
"""string="Aishwarya"
vol=0
for char in string:
    if char.lower() in 'aeiou':
        vol+=1
        print(char,end="")
print("count of volwels",vol)"""
    
#12. Count consonants in a string using a for loop.
"""string="Aishwarya"
cons=0
for char in string:
    if char.lower() not in 'aeiou':
        cons+=1
        print(char,end=" ",)
print("count of consonants",cons)"""

#13. Print squares of numbers from 1 to 10.
"""for i in range(1,11):
    sq=i*i
    print(sq)"""

#14. Print cubes of numbers from 1 to 5.
"""for i in range(1,6):
    sq=i*i*i
    print(sq)
"""
#15. Count how many even numbers are in a list.
"""list=eval(input("enter the numbers:"))
even_count=0
for i in list:
    if i%2==0:
        even_count+=1
        print(i,end=" ",)
print("count of even numbers",even_count)"""

#16. Count how many odd numbers are in a list.
"""list=eval(input("enter the numbers:"))
odd_count=0
for i in list:
    if i%2==1:
        odd_count+=1
        print(i,end=" ",)
print("count of odd numbers",odd_count)"""

#17. Find the largest number in a list using a for loop.
"""list=eval(input("Enter the list"))
large=list[0]
for i in list:
    if i>large:
        large=i
print(f"{large} is largest")"""
    
#18. Find the smallest number in a list using a for loop.
"""list=eval(input("Enter the list:"))
small=list[0]
for i in list:
    if i<small:
        small=i
print(f"{small} smallest number")"""

#19. Count how many times a particular element appears in a list.
"""list=eval(input("Enter the elements of list"))
num=int(input("Enter the index value to count the occurence:"))
print(list.count(num))
"""

#20. Reverse a string using a for loop (without using slicing).
"""string="Sonali"
reversed_string=""
for char in string:
    reversed_string=char+reversed_string
print(reversed_string)"""


#21. Print numbers from 1 to 100 that are divisible by 5
"""for i in range(1,101):
    if i%5==0:
        print(i)"""

#22. Print numbers from 1 to 50 that are divisible by 3.
"""for i in range(1,51):
    if i%3==0:
        print(i)"""

#23. Print characters of a string along with their position.
"""input_data=input("Enter the string")
for index,char in enumerate(input_data):
    print(f"char {char} is stored in index of {index} ")"""

#24. Convert all letters of a string to uppercase using ASCII
# (without upper()).

"""
name="sonali"
"SONALI"
a-z -->97 to 122
A-Z -->65 to 90
"""
"""name="sonali"
output=""
for char in name:
       ascii=ord(char)    
       c=ascii-32
       output=output+chr(c)
print(output)   """



#25. Convert all letters of a string to lowercase using ASCII (without lower()).

"""name="AISHWARYA"
output=""
for char in name:
       ascii=ord(char)    
       c=ascii+32
       output=output+chr(c)
print(output)"""

#26. Print only positive numbers from a list.
"""list=[40,80,-91,-14]
for i in list:
    if i>=0:
        print(i)"""

#27. Print only negative numbers from a list.
"""list=[40,80,-91,-14]
for i in list:
    if i<=0:
        print(i)
"""
#28. Print the product of all numbers in a list.
"""list=[40,80]
pro=1
for i in list:
       pro=pro*i
print(pro)"""
        
#29. Print only alphabets from a string (skip numbers/symbols).
"""string="Sonu123"
for char in string:
    print(char)
    if char.isnumeric and  char=="@#$%^&*()+-/<>":
        continue
        print(char)
"""
"""string=input("Enter the string:")
for i in string:
       if i.isalpha():
            print(i)"""
              

#30. Print the length of a string using a for loop (without len()).
"""string=input("Enter the string:")
index=1
for i in string:
       print(i,index)
       index=index+1
"""

"""data={"name":"gulayya","age":28,"place":"bagalkot"}
for index,key in enumerate(data):  
    print(f"{index},{key}={data[key]}")"""
 

#Multiplication using for loop
"""for i in range(2,11):
       for j in range(1,11):
              print(f"{i}x{j}={i*j}")"""

"""number=int(input("enter the number"))
rev=0
temp=number
while temp>0:
       rem=temp%10
       rev=rev*10+rem
       temp//=10
if rev==number:
       print("palindrome")
else:
       print("not a palindrome") """      

"""num={10,20}
for i in {50,30,60}:
    print(num)"""
    

