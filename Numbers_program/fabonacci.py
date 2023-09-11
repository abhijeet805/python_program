n=input("Enter number to print Fabonacci=")
n=int(n)
f=0
s=1
print(f,s,end=" ")

while n-1>0:
    t=f+s
    print(t,end=" ")
    f=s
    s=t
    n-=1

