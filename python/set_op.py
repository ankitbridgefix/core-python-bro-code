#Solved Problem 16/12/2022
"""n = int(input("Enter N Number of Elements:"))
s = set([int(i)  for i in input().split() if int(i)>=0 and int(i)<=9])
print(s)
c = int(input("Enter Command Number:"))
for i in range(c):
    c=input().split()
    
    #v = int(c[1])
    if(c[0]=="pop"):
        s.pop()
    elif(c[0]=="remove"):
        v = int(c[1])
        s.remove(v)
    elif(c[0]=="discard"):
        v = int(c[1])
        s.discard(v)
print(sum(s))
    """
    
#====================================

# n = int(input())
# n_r = set(map(int,input().split()))

n = int(input())
n_r = set(map(int,input().split()))

b = int(input())
b_r = set(map(int,input().split()))

print(n_r)
print(b_r)
z=n_r.symmetric_difference(b_r)
print("Z",z)
y = b_r.symmetric_difference(n_r)
print("Y",y)
print("Shortcut",n_r^b_r)