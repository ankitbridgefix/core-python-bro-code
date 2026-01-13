n =int(input("Enter You want to Print:"))
import time
s =time.time()
a=0
b=1
if(n==0):
    print(a)
elif(n==1):
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
        print(c)
e =time.time()
print(e-s)