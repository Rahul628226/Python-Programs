a=int(input("Enter the number of first element"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>c:
    print(b)
else:
    print(c)

