l = {1,2,3,4,5,6,6}
# print(l)
# l.add(7)
# print(l,len(l))
# print(set("Ankit"))
# print(set(['H','a','c','k','e','r','r','a','n','k']))
# print(set({'Hacker' : 'DOSHI', 'Rank' : 616 }))
"""
#solved Problem 15/12/2022
total =0
le = len(l)
print(le)
for i in l:
    #print(l)
    total+=i
print(total)
avg = total/le
print(avg)"""

"""
#solved problem 15/12/2022
M =int(input())
a = set(map(int,input().split()))
N = int(input())
b = set(map(int,input().split()))
z = a.symmetric_difference(b)

for i in z:
    print(i)
"""
"""n,m = map(int,input().split())
ar=set()
A = set()
B = set()

for i in range(n):
    p =int(input("Enter arry"))
    ar.add(p)

for i in range(m):
    q = int(input("Enter A value"))
    A.add(q)
for i in range(m):
    q = int(input("Enter A value"))
    B.add(q)
    
print(ar)
print(A)
print(B)
z=ar.intersection(A)
y=ar.intersection(B)
print(z,len(z))
print(y,len(y))
l_z = len(z)
l_y = len(y)
if(l_z>l_y):
    print(l_z-l_y)
else:
    print(l_y-l_z)
    """
    
    
# Enter your code here. Read input from STDIN. Print output to STDOUT
"""n,m = map(int,input("N M").split())
ar=set()
A = set()
B = set()

for i in range(n):
    p =int(input("Arr"))
    ar.add(p)

for i in range(m):
    q = int(input("A"))
    A.add(q)
for i in range(m):
    q = int(input("B"))
    B.add(q)
z=ar.intersection(A)
y=ar.intersection(B)
l_z = len(z)
l_y = len(y)
print("Set A:",A)
print("Set B",B)
if(l_z>l_y):
    print("First",l_z-l_y)
else:
    print("Second",l_y-l_z)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""n,m = map(int,input().split())
a = [int(x) for x in input().split()]
ar=set(a)

b = [int(x) for x in input().split()]
A =set(b)

c = [int(x) for x in input().split()]
B=set(c)
z=ar.intersection(A)
y=ar.intersection(B)
l_z = len(z)
l_y = len(y)
if(l_z>l_y):
    print(l_z-l_y)
else:
    print(l_y-l_z)
"""
N = ['3','2']#input().split()
Arr =['1','5','3']    #input().split()
A ={'1','3'}
B ={'5','7'}

# A = set(input().split())
# B = set(input().split())
print("N==>",N)
print("Arr==>",Arr)
print("A==>",A)
print("B==>",B)
# c=0
# for i in Arr:
#     if i in A:
#      c+=1
#      print(c)
#     elif(i in B):
#         c-=1
#         print(c)
# print("Ans",c)

""""==========OR==========="""
x =sum([(i in A)-(i in B) for i in Arr])
print(x)
