s1=input("Enter String")
s2=s1.split(" ")

for i in range(0,len(s2)):
    if(len(s2[i])%2==0):
        print(s2[i],end=' ')
