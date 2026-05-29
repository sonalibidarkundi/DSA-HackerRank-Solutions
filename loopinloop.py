"""for x in range(1,4):
    for y in range(1,6):
        print(x,end=" ")
        """

"""
1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 
"""

"""for x in range(1,4):
    for y in range(1,6):
        print(y,end=" ")
        """
"""
1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 
"""

#while-while-loop
"""i=0
while i<=3:
    j=0
    while j<=3:
        print("Hello")
        j+=1
    i+=1
    """
"""
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
"""

"""name="Sonali"
x=0
while x<len(name):
    y=0
    while y<len(name):
        print(name[x]+name[y])
        y+=1
    x+=1
"""


"""
SS
So
Sn
Sa
Sl
Si
oS
oo
on
oa
ol
oi
nS
no
nn
na
nl
ni
aS
ao
an
aa
al
ai
lS
lo
ln
la
ll
li
iS
io
in
ia
il
ii
"""

#check the Armstrong No. from 1 to 101
"""l=[]
for i in range(1,101):
    number=i
    s=str(number)
    length=len(s)
    temp=number
    sum=0
    while temp>0:
        rem=temp%10
        sum=sum+rem**length
        temp//=10
    if sum==number:
        l.append(i)
print(l)
"""

"""[1, 2, 3, 4, 5, 6, 7, 8, 9]"""