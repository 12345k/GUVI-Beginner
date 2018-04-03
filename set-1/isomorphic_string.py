a=str(input())
b=str(input())
for i in range(len(a)):
    a=a.replace(a[i],b[i])
if(a==b):
    print("true")
else:
    print("false")