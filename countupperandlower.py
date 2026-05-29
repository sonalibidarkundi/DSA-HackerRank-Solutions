# Count uppercase and lowercase letters in a string.
count_upper=0
count_lower=0
string=input("Enter the string:")
for i in string:
    if i.isupper():
        count_upper+=1
print(f"upper letter = {count_upper}")
for j in string:  
    if j.islower():
        count_lower+=1
print(f"lower letter = {count_lower}")
