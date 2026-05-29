## Beginner Level – For Loop Questions

#1. Print numbers from 1 to 10 using a for loop.
#2. Print numbers from 10 to 1 in reverse order.
#3. Print all even numbers from 1 to 50.
#4. Print all odd numbers from 1 to 50.
#5. Print the multiplication table of a given number.
#6. Find the sum of numbers from 1 to 100.
"""sum=0
for i in range(1,101):
    sum=sum+i
print(sum)"""

#7. Find the product of numbers from 1 to n (factorial).
"""number=int(input("Enter the number u want to find product:"))
fact=1
i=1
while i<=number:
    fact=fact*i
    i+=1
print(fact)"""

#8. Count how many digits are present in a number.
"""number=int(input("Enter the number:"))
s=str(number)
count=0
for i in s:
    count+=1
print("count of digits are",count)"""
    
#9. Find the sum of digits of a number.
#10. Reverse a number using a loop.
"""number=int(input("Enter the number:"))
rev=0
temp=number
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp//=10
print(rev)
"""

## String-Based Questions

#11. Print each character of a string using a for loop.
#12. Count vowels in a string.
"""string=input("Enter the string")
for i in string:
    if i in "aeiou":
        print(i)"""

#13. Count consonants in a string.
"""string=input("Enter the string")
for i in string:
    if i not in "aeiou":
        print(i)"""

#14. Reverse a string using a for loop.
#15. Check whether a string is a palindrome.
"""rev_string=""
string=input("Enter the string:")
for char in string:
    rev_string=char+rev_string
print(rev_string)
if string==rev_string:
    print("String is palindrome")
else:
    print("String is not palindrome")
"""
#17. Print characters at even indexes.
"""string=input("Enter the string:")
for i,index in enumerate(string):
    if i%2==0:
        print(index,end="")"""



#18. Remove spaces from a string using a loop.
"""string=input("enter the string:")
for i,n in enumerate(string):
    if n==" ":
        i=i-1
    print(n,end="")"""

#19. Find the frequency of a character in a string.
#20. Convert lowercase letters to uppercase without using `.upper()`.


## List-Based Questions

#21. Find the largest number in a list.
"""list=eval(input("Enter the list elements:"))
large=list[0]
for i in list:
    if i>large:
        large=i
        print(large)"""

#22. Find the smallest number in a list.
"""list=eval(input("Enter the list elements:"))
large=list[0]
for i in list:
    if i<large:
        large=i
print(large)"""

#23. Find the sum of all elements in a list.
"""list=eval(input("Enter the number of the list:"))
sum=0
for i in list:
    sum=sum+i
print(sum)"""

#24. Count even and odd numbers in a list.
"""even_count=0
odd_count=0
list=eval(input("Enter the numbers in the list:"))
for i in list:
    if i%2==0:
        even_count+=1
print(f"Even count = {even_count}")
for j in list:
    if j%2!=0:
        odd_count+=1
print(f"Odd count = {odd_count}")"""
    
    
#25. Print duplicate elements in a list.
"""list=eval(input("Enter the numbers in the list:"))
num=list[0]
for i in list:
    if list[0]==i:
        print(i)
        break"""

#26. Remove duplicates from a list.
"""list=eval(input("Enter the numbers in the list:"))
num=list[0]
for i in list:
    if list[0]!=i:
        print(i)
        """

#27. Reverse a list using a loop.
#28. Find the second largest number in a list.
#29. Count positive and negative numbers in a list.

#30. Merge two lists using a loop.
"""list1=eval(input("Enter the numbers in the list1:"))
list2=eval(input("Enter the numbers in the list2:"))
merge=[]
for i in list1:
    merge.append(i)

for j in list2:
    merge.append(j)
print(merge)"""
        



## Pattern Programs

#31. Print a square star pattern.

"""python
*****
*****
*****
*****
*****

"""
#32. Print a right triangle pattern.

"""python
*
**
***
****
*****"""


#33. Print an inverted triangle pattern.

"""python
*****
****
***
**
*"""


#34. Print a pyramid pattern.
#35. Print Floyd’s triangle.
#36. Print multiplication pattern tables.
#37. Print alphabet patterns (A, B, C...).
#38. Print number triangle patterns.



## Intermediate Level Questions

#39. Check whether a number is prime.
#40. Print all prime numbers between 1 and 100.
#41. Find Fibonacci series up to n terms.
#42. Find Armstrong numbers in a range.
#43. Check whether a number is Armstrong or not.
#44. Find GCD of two numbers using loops.
#45. Find LCM of two numbers.
#46. Print factors of a number.
#47. Count frequency of elements in a list.
#48. Find common elements between two lists.


## Nested For Loop Questions

#49. Print matrix rows and columns.
#50. Print all combinations of two lists.
#51. Create a chessboard-like pattern.
#52. Print multiplication tables from 1 to 10.
#53. Print all pairs from a list.
#54. Find transpose of a matrix.
#55. Print diamond star pattern.



## Advanced Practice Questions

#56. Bubble sort using loops.
#57. Selection sort using loops.
#58. Find missing number in a list.
#59. Rotate a list using loops.
#60. Create a simple menu-driven calculator using loops.
