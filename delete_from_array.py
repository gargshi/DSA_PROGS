a=[1,2,3,4,5]
e=2
b=[]
for i in range(len(a)):
    if(a[i] != e):
        b.append(a[i])

if b==a:
    print("element not found.")
else:
    print("element deleted. array :",b)