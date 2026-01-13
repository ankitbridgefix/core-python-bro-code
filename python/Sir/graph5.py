a=[2,3,2,1,5,6]
#a=[1,1]
b=0
i=0
while(i<len(a)):
    s=0
    x=i
    while(x<len(a)-1):  
        if a[x]<=a[x+1]:
            s=s+1
        else:
            break
        x+=1
    y=i
    while(y>0):
        if a[y]<=a[y-1]:
            s=s+1
        else:
            break   
        y-=1
    if s>b:
        b=s
    i+=1
print(b)
