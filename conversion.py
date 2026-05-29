def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print(f"{i},{oct(i)[1:]}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



""" 
print(i,oct(i),hex(i),bin(i))

"""