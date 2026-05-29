#*Nested If* 

#1. Check if a number is even; if yes, also check whether it's divisible by 4.
"""n=int(input("Enter the number:"))
if n%2==0:
    print(f"{n} is even")
    if n%4==0:
        print(f"{n} is divisible by 4")
    else:
        print(f"{n} is not divisible by 4")
else:
    print("number is odd")"""

#2. Ask for year; if it’s divisible by 4, check additional leap-year conditions.
"""year=int(input("Enter the year:"))
if year%4==0:
    print(f"{year} is divisible by 4 ")
    if year%400:
        print(f"{year} is year leap")
    else:
        print(f"{year} is not leap year")
else:
    print(f"{year} is not divisible by 4")"""


#3. Input username; if correct, check password; if both match print Login Successful.
"""usename="Guido"
pswd="python123"
Password=input("Enter the password:")
usename1=input("Enter the username:")
if Password==pswd or usename1==usename:
    if Password==pswd and usename1==usename:
        print("Login successful")
    else:
        print("password and usename are invalid")
else:
    if Password!=pswd or usename1!=usename:
        print("inavlid username and passward")"""

#4. Input 3 sides of a triangle; first check if they form a triangle, then if equilateral,
# isosceles, or scalene.


#5. Ask a user for age; if 18+, ask if they have an ID; allow entry only if both true.
"""age=int(input("Enter your age:"))
if age>=18:
    id=input("Do you have ID(Yes/No):")
    if id.lower()=="yes":
        print("You have Entry")
    else:
        print("Id dont have id")
else:
    print("No entry")"""

#6. Input a number; if positive, check if it's greater than 100, otherwise if less than 10.
"""n=int(input("Enter number:"))
if n>0:
    if n>=100:
        print("number is greater then 100")
    elif n<=10:
        print("Number is less then 10")
    else:
        print("number is in between 10 and 100")
else:
    print("no number")"""


