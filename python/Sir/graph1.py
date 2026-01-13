a =[44,13,1,5,6,6]
#a=[22,3,4,44,4]
a=[1,1,1,1]
l=[]
print("List A: ",a)
b=a[::-1]
print("List B: ",b)

#LIST A Operation
s=1
for i in range(len(a)-1):
    if(a[i]<=a[i+1]):
        #print(a[i+1])
        s=s+1  
        print("IF=>S",s)
    else:
        l.append(s)
        print("Else S",s)
        s=s*0
        s=s+1
l.append(s)
print(l)
f =0
for j in range(len(b)-1):
    if(b[j]<=b[j+1]):
        print(b[j+1])      
        f=f+1
        print("IF F",f)
    else:
        l.append(f)
        print("ELSE F",f)
        f =f*0
l.append(f)
    
print(max(l))
        
        