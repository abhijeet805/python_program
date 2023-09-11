s1=input("Enter a string")
s2=""

for ch in s1:
    if ch not in s2:
        s2=s2+ch

print(s2)
