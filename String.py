#1.String concatenation
"""greet="Good"
substring="Afternoon"
print(greet+" "+substring)
"""
#2.String Repitation
"""name=input("Enter your name:")
repeat=name*5
print(repeat)"""

#3.Finding Length 
"""user_input=input("Enter the input:")
print(len(user_input))
"""

#4.Indexing
"""user_input=input("Enter the input:")
print(user_input[5])
"""
#5.Slicing
user_input=input("Enter the input:")
print(user_input[1:4])
print(user_input[-1::])#print only last char
print(user_input[::1])#print whole given string
print(user_input[::2])#leaves only 1 char 
print(user_input[1:-1:1])
print(user_input[::-1])#reverse the string


#6.Searching
"""greet="Good morning"
substr="Good"
print(substr not in greet)"""



#7.Format string 
"""name=str(input("Enter your name:"))
print(f"my name is:{name}")"""


#Methods /Functions of string
#1.count()
"""name="hello morning morning sonali"
print(name.count("morning"))

name=input("Enter string:")#"hello morning morning sonali"
substr=input("Enter substr:")
print(name.count(substr))
"""


#2.upper()
"""name="Sonali Bidarkundi from vijaypur distict"
print(name.upper()) 
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.startswith("Sonali"))
print(name.endswith("Sonali"))
print(name.endswith("distict"))"""


#3.join()
"""name="Sonali"
name1="*".join(name)
print(name1) """

#4.split
"""name="Sonali Bidarkundi"
name1=name.split()
print(name1)
name2="*".join(name1)
print(name2)"""


#9.casefold()
"""text = "ß"
text1=","
print(text.lower())
print(text.casefold())
print(text1.lower())
print(text1.casefold())"""


#10.center
"""string="sonali"
print(string.center(10,"#"))"""


#11.find
"""
string=input("Enter the string: ")
string1=input("Enter the string: ")
print(string.find(string1,2,5))
"""
"""
n1="banana"
print(n1.find("n",3,5))
"""

#12.index()
"""list=[88,35,40,2,82,80,35]
print(list.index(35,0,4))"""

"""list=eval(input("Enter the number: "))
num=int(input("Enter the number : "))
print(list.index(num,0,4))
"""

#13.isalpha
"""string=input("Enter the string: ")
print(string.isalpha())"""

#14.isupper()
"""string=input("Enter the string: ")
print(string.isupper())"""

#15.islower()
"""string=input("Enter the string: ")
print(string.islower())"""

#16.isdigit()
"""digits=input("Enter the digits: ")
print(digits.isdigit())"""

#17.isnumeric
"""numeric=input("Enter the numeric: ")
print(numeric.isnumeric())"""

#18.isalpnum
"""alpnumeric=input("Enter the alpnumeric: ")
print(alpnumeric.isalnum())"""

#19.istitle
"""title=input("Enter the string: ")
print(title.istitle())"""

#20.isspace
"""space=input("Enter the space: ")
print(space.isspace())"""

#21.replace
"""s="good morning"
s1=s.replace("morning","Afternoon")
print(s1)"""


"""s=input("Enter the string: ")
ss=input("Enter the string2: ")
s1=ss.replace(ss,s)
print(s1)"""

#22.strip
"""s=" Good Moring "
print(s.strip())"""

#23.swapcase
"""s="good moring"
print(s.swapcase())
"""
#24.zfill
"""s="good moring"
print(s.zfill(15))"""
