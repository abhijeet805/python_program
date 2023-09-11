s1=input("Enter String")
s2=s1[::-1]
a=len(s1)
if(s1==s2):
    print("String is Palindrome")
else:
    print("String is not palindrome")
if s1[:a//2]==s1[a//2:]:  #dada(two part da & da are same) is a symetric
    print("String is Symmetric")
else:
    print("String is not Sysmmetric")
