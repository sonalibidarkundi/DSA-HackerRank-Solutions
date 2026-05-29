"""a=20
B=20
print(id(a),id(B))"""
#In some cases, you may see the same id for x and y because 
#Python reuses small immutable objects (like small integers or short strings).

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print(a==b)
print(a is b)