a=[2,3,1,5,6]
a=[1,1,1,1,1]
b=[]

for i in range(len(a)):
    s=0
    for x in range(i,len(a)-1):
        
        if a[x]<=a[x+1]:
            s=s+1
        else:
            break
    for y in range(i,0,-1):
    
        if a[y]<=a[y-1]:
            s=s+1
        else:
            break   
    b.append(s)
    #s=s*0
print(max(b))
