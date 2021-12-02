n=int(input("Enter the limit"))
a=[]
for i in range(n):
    k = input("Enter the Names")
    a.append(k)
s=0
for x in a:
    b=x.count('a')
    s=s+b
print(s)
