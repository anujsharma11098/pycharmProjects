l1=[5,1,4,3,2]
high=max(l1)
l2=[]
while (high!=0):
    a = ""
    for i in l1:
        if(i>=high):
            a+="*"
        else:
            a+= " "
    l2.append(a)
    high-=1
for i in l2:
    print(i)

