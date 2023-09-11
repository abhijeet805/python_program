s1=input("Enter String")
s2=s1.split(" ")

print("Reverse word in given string")
for i in range(len(s2)-1,-1,-1):
    print(s2[i],end=' ')
