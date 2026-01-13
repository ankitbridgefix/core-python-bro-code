a= [(1, 2, 3), (1, 2, 3), (1, 2,3)]

for i in range(len(a)):
    #print(a[i])
    print("======")
    l =[]
    k = a[i]
    t =0
    for j in range(len(a[i])):
        #print(a[j][i])
        t+=a[j][i]
        l.append(t)
print(l)

