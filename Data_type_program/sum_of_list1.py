def add(a):
    return sum(a)

l1=[]
n=int(input("Enter Limit"))
for i in range(0,n):
    num=int(input("Enter number="))
    l1.append(num)

print("Sum of List=",add(l1))
