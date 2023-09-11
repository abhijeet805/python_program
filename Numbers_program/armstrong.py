n=int(input("Enter number"))
s=0
num=n
while(n>0):
    d=n%10
    s=s+d**3
    n//=10
if s==num:
    print("Armstrong")
else:
    print("Not")
