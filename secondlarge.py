#Find the second largest number in a list.
list=eval(input("Enter the list elements:"))
large=list[0]
for i in list:
    if i>large:
        large=i
        print(large)