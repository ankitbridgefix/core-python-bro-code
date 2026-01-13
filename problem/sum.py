a = 78
a = str(a)
s=0
for i in a:
    s=s+int(i)
if s>=10:
    l = str(s)
    s=0
    for j in l:
        #print(j)
        s=s+int(j)
print(s)
