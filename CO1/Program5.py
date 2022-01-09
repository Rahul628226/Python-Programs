#Prompt the user for a list of integers. For all values greater than 100,store 'over' instead

num=int(input("Enter the limit"))
a=[]
for i in range(num):
    k=(int(input("Enter the number")))

    if k<100:
        a.append(k)
    else:
        a.append("over")
print(a)
