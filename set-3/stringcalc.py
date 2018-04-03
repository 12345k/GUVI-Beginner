n =input()
l=[]
a=0
d=0
s=0
for i in n:
    l.append(i)
for i in l:
    if i.isalpha()==True:
        a=a+1
    elif i.isdigit() == True:
        d=d+1
    else:
         s=s+1
print("alphabet",a,"digit",d,"special",s)

