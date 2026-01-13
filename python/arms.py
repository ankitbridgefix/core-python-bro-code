r = int(input("Enter Limit: "))
import time
s =time.time()
arm = []
not_arm =[]
for m in range(1,r+1):

    n = m  #int(input("Enter Any Number: "))
    if n<=0:
        print("Please Enter Positive Number:")
    else:
        original = n

        le = len(str(n))
        #print(le)
        total =0
        while(n>0):
            digit = n%10
            #print(digit)
            total =total+digit**le
            n = n//10
            #print(n)
        if(total==original):
           # print("This Number Is Armstrong Number",total)
            arm.append(total)

        else:
           # print("This Number is Not Armstrong Number:",original)
            not_arm.append(original)
e =time.time()
print(e-s)           
print("THis is Armstrong Number:",arm)
#print("THis Is Not Armstrong Number:",not_arm)
