n = (1,4,6),(2,9,5),(6,8,8)

#print(type(n))
w =[]
h=[]
out =[]
#print((n))
for i in n:
    print(i[:2])
    s=min(i[:2])
    print('min',min(i))
    w.append(min(i[:2]))
    #print('max',max(i))
    w.append(max(i[:2]))
    h.append(i[-1]) #h

mi = min(w)
mx = max(w)

for j in range(len(n)):
    if mx in n[j]:
        print('mx',n[j][-1])
        oh = n[j][-1]
        out.append(oh)
    
out.extend([mi,mx])
out.extend(h)

print(min(w),max(w))
print(out)

            
    

