arr=[1,2,3,4,5]
k=-1
m=0
for i in range(0,len(arr)):
    if(arr[i]==k):
        print("Found at "+str(i+1)+" position")
        m=1
if m==0:
    print("Not found")