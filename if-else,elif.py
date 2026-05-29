#Assignment*
#If–Else*

#1. Write a program to check whether a number is positive or negative.

#2. Ask the user for their age and print whether they are an adult (18+) or minor.

#3. Input a number and check if it is even or odd.

#4. Ask the user for a password; print “Access Granted” only if it matches "python123".
"""Auth="python123"
Password=input("Enter the password:")
if Password==Auth:
    print("Access Granted")
else:
    print("Access Denied")"""


#5. Check whether a given year is a leap year or not using simple if–else (not the full rule).
"""year=int(input("Enter the year:"))
if year%4==0:
    print(f"{year} is year leap ")
else:
    print(f"{year} is not leap year")"""

#6. Take a temperature value and print “Hot” if it’s above 30, otherwise “Cold”.


#*If–Elif*

#1. Input a number and print whether it’s positive, negative, or zero.
"""n=int(input("Enter the number:"))
if n>0:
    print("positive number")
elif n<0:
    print("Negative number")
else:
    print("number is zero")"""

#2. Ask for marks and print Grade A (≥90), B (≥75), C (≥50), or Fail.
"""marks=int(input("Enter the number:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("fail")"""

#3. Input the day number (1–7) and print the weekday name.
"""day=int(input("Enter the day:"))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("Thuesday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")
else:
    print("No day")"""

#4. Ask the user for a character and identify if it is a vowel, consonant, or not a letter.
"""ch=input("Enter the day:")
if ch in "aeiou" or "AEIOU":
    print("charceter is vowel")
elif ch.isdigit():
    print("charceter is digits")
else:
    print("consonents")"""

#5. Input someone’s age and categorize as Child, Teen, Adult, or Senior.
"""age=int(input("Enter the number:"))
if age<=12:
    print("Child")
elif age<=22:
    print("Teen")
elif age<=25:
    print("Adult")
else:
    print("SeniorS")"""

#6. Enter a month number and print the number of days in that month.
"""Month=input("Enter the Month Number/Name:")
if Month=="1" or "Jan" or "jan":
    print(31)
elif Month=="2":
    print(28)
elif Month=="3":
    print(30)
elif Month=="4":
    print(30)
elif Month=="5":
    print(31)
elif Month=="6":
    print(30)
elif Month=="7":
    print(30)
elif Month=="8":
    print(31)
elif Month=="9":
    print(30)
elif Month=="10":
    print(31)
elif Month=="11":
    print(30)
elif Month=="12":
    print(31)
else:
    print("No Month")"""

#*If–Elif–Else*

#1. Input a number and print whether it is small (1–10), medium (11–50), or large (>50).
"""number=int(input("Enter the number:"))
if number<=10:
    print("number is small")
elif number<=50:
    print("number is medium")
else:
    print("Number is large")"""

#2. Ask the user for their income and compute tax bracket (e.g., Low, Medium, High).
"""income=int(input("Enter the income:"))
if income<=10000:
    print("number is low")
elif income<=30000:
    print("number is Medium")
else:
    print("Number is High")"""

#3. Input 3 numbers and print the largest.
"""n1=int(input("Enter the n1:"))
n2=int(input("Enter the n2:"))
n3=int(input("Enter the n3:"))
if n1>n2 and n1>n3:
    print(f"{n1} is largest")
elif n2>n3:
    print(f"{n2} is largest")
else:
    print(f"{n3} is largest")"""

#4. Take a speed value and categorize as normal, speeding, or overspeed penalty.


#5. Input a student’s score and give A / B / C / D / F using elif ladder.
"""marks=int(input("Enter the number:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("fail")"""

#6. Ask for temperature and categorize as Cold, Warm, or Hot.
"""temp=int(input("Enter the temparature:"))
if temp<=30:
    print("temperature is Cold")
elif temp<=50 and temp >=30:
    print("temparature is Warm")
else:
    print("temperature is hot")"""

