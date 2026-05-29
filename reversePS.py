input_data="hello Soundarya How Are You?"
elements=input_data.split()
print(elements)
list=[]
for x in range(len(elements)):#(5)# 0 1 2 3 4
    if x%2!=0:
        list.append(elements[x][::-1])

    else:
        list.append(elements[x])  

print(list)        
output=" ".join(list)
print(output)
