l =[2,3,1,5,6]
#l=[2,1,1,2,1]
#l=[22,3,4,44,4,]
l=[5,5,4,4,3,2]

le = len(l)-1
count =1
for i in range(le):
    if(l[i+1]>=l[i]<=l[i-1] if l[i-1] else l[i+1]):
        #print(l[i+1]-l[i])
        count+=1
print(count)

#############
l =[1,2,3,4,4]
# l =[1,1,1,1]
l=[5,5,4,4,3,2]
le =len(l)
k =[]
for r in range(le):
    for c in range(le):
        if(l[r]<=l[c]):
            z =l[c]-l[r]
            k.append(z)
        
print(k)

print(max(k))