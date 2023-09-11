nterm=int(input("term="))
n1,n2=0,1
count=0

if(nterm==1):
    print("series=",n1)

else:
    print('fabonacci sequence')
    while(count<nterm):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count += 1
    
    
