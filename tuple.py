#tuple oparation
#1.concatination
"""tuple1=eval(input("Enter the elements:"))
tuple2=eval(input("Enter the elements:"))
print(tuple1+tuple2)
"""
#2.repeatation
"""tuple1=eval(input("Enter the elements:"))
print(tuple1*3)"""

#3.indexings
"""tuple1=eval(input("Enter the elements:"))
index=int(input("Enter the index:"))
print(tuple1[index])"""

#4.slicling
tuple=(5,4,8,10,6,7)
print(tuple[1:4])

#5.finding the length
tuple=(5,4,8,10,6,7)
print(len(tuple))

#6.searching
tuple=(5,4,8,10,6,7)
print(5 in tuple)
 
#methods of tuple
#1.count()
tuple=(5,4,8,10,6,7)
print(tuple.count(10))

#2.index()
tuple=(5,4,8,10,6,7)
print(tuple[1])

#3.sum()
print(sum(tuple))
#4.min()
print(min(tuple))
#5.max()
print(max(tuple))

#addition of tuple
tuple=(5,4,8,10,6,7)
tuple1=(5,4,8)
print(tuple+tuple1)
print(tuple[2])
