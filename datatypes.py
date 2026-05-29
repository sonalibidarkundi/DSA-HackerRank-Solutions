#datatypes
#1.Integers
n1=200
n2=2000
sum=n1-n2
print(n1,type(n1))
print(n2,type(n2))
print(sum,type(sum))

#we can represent integers in binary,octal,hexadecimal
#1.Binary
n1=0b000011
print(n1,type(n1))
n2=0b000011
print(n2,type(n2))
sum=n1+n2
print(sum,type(sum))
print(0b0000110+0b0000110)
print(oct(3))
print(hex(2748))



#2.Ocatal
n2=0o123
print(n2,type(n2))

#3.Hexadecimal
n3=0x1AB
print(n3,type(n3))


#2.float

n1=40.5
n2=50.6
sum=n1+n2
sub=n1-n2

print(sum,type(sum))
print(sub,type(sub))


A=10
name="Sonali"
#Sum=A+B
print(f"The sum is: {A}{name}")


#3.Complex numbers
C1=2+3j
C2=2+3j
sum=C1+C2
print(sum,type(sum))
print(sum.real)
print(sum.imag)

#4. Boolean
list1=[2,4,5,6,7,8,9,10]
print(5 in list1)
print(11 in list1)


list2=['Sonu','shrusti','samarth',100]
print('Sonu' in list2)
print(100 in list2)




#4. None
A=None
print(A,type(A))

A=100
print(A,type(A))


#String
S="Hello, I am Sonali"
print(S,type(S))
print(S[0])
print(S[0:4])
print(S[-9:])
print(S[0:17:3])


#S1[0]="g"  # This will raise an error because strings are immutable

del S
#print(S1)


