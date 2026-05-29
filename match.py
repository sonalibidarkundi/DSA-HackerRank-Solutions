#*Match–Case* 

#1. Use match to print day name from day number (1–7).
"""day=int(input("Enter the day number:"))
match day:
    case 1:print("Sunday")
    case 2:print("Monday")
    case 3:print("Tuesday")
    case 4:print("Wednesday")
    case 5:print("Tuesday")
    case 6:print("Friday")
    case 7:print("Saturday")
    case _:print("No day")"""

#2. Use match to implement a simple calculator (+, −, ×, ÷).
number1=int(input("Enter the day number:"))
number2=int(input("Enter the day number:"))
op=input("Enetr the opataratar(+,-,*,/)")
match op:
    case "+":print(number1+number2)
    case "-":print(number1-number2)
    case "*":print(number1*number2)
    case "/":print(number1/number2)
    case _:print("invalid")

#3. Use match to print month name from month number (1–12).

#4. Use match to categorize input 1 → Start, 2 → Stop, 3 → Pause, else Invalid.

#5. Use match to print season based on month number.

#6. Use match to check input character'a' | 'e' | 'i' | 'o' | 'u' → vowelany letter → consonantotherwise → not a letter