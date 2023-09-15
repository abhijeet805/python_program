a=["ruby","php","python","nitin","AbhiiiA"]
c=0
for s in a:
    if len(s)>2 and s[0]==s[-1]:
        c=c+1

print("Count String=",c)
