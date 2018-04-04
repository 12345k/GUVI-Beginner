s=str(input())
s1 =s.split(" ")
a=int(s1[-1])
s1[-1]=""
for i in range(a):
    print(" ".join(s1))