a =int(input())
b = int(input())
l=0
count=0
count = a if a<b else b
for i in range(1,count):
    if(a%i==0&b%i==0):
         l=i
print(l)