n=int(input("Enter limit="))
j=2
print(j,end=" ")
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break;
    if(i==j+1):
        print(i,end=" ")
