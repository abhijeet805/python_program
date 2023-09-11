def f(x):
    if x in('a','e','i','o','u'):
        print(x,'is owvel')
    elif x in('a','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','x','y','z'):
        print(x,"is consonent")
    else:
        print(x,"is not alphabet")


a=str(input("Enter alpha charcter:"))
f(a)
