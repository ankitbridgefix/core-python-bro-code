# N=7
# m = 21
# s = ".|."
# for i in range(N//2):
#     print((s*(2*i+1)).center(m,"-"))
# else:
#     print(("Welcome").center(m,"-"))
# for i in reversed(range(N//2)):
#     print((s*(2*i+1)).center(m,"-"))

# SOLVED Problem
# A =  16
# A_S  = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,24,52} #set(map(int,input().split()))

# N = int(input())
# for i in range(N):
#     op ,c = input().split()
#     s = set(map(int,input().split()))
#     if op == "intersection_update" :
#        A_S.intersection_update(s)
#        print("InterSection_Update",A_S)
#     elif op =="update":
#         A_S.update(s)
#         print("Update",A_S)
        
#     elif op =="symmetric_difference_update":
#         A_S.symmetric_difference_update(s)
#         print("Symetric di",A_S)
#     elif op == "difference_update":
#         A_S.difference_update(s)
#         print("Diff",A_S)
#     else:
#         print("inc")
# print(sum(A_S))
from collections import Counter
# k =5
# l = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
# l2 =[]

# for i in l:
#     if(l.count(i)==1):
#         print(i)

# k =Counter(l)
# d=dict(k)
# print(d)
# print(min(d, key=lambda k: d[k]))
# k = 5
# rooms = l
# print("Room List",rooms)
# roomSet = set(rooms)  
# print("RoomSet:",roomSet)
# roomSum = sum(rooms)
# print("Room Of Sum",roomSum)
# roomSetSum = sum(roomSet) * k
# print("Room Set Sum",roomSetSum)
# captiansRoom = (roomSetSum - roomSum) // (k - 1)
# print(captiansRoom)

# A ={1,2,3,4,5,6,7,8,9,10,11,12,23,45,84,78}
# n1 ={1,2,3,4,5}
#n2 = {100,11,12}]

# l=[]1

# for i in range(3):
#     n1 = set(map(int,input().split()))
#     z =A.issuperset(n1)
#     l.append(z)
# print(l)

# l =[True,True]
# from functools import reduce
# a =reduce(lambda a,b:a*b,l)
# print(a)
"""import cmath
a =int(input("Enter A:"))
b=int(input("Enter B:"))
z=complex(a,b)
d = cmath.polar(z)
print(d)
print(type(d))
d =list(d)
for i in d:
    print(i)
"""

"""import cmath
a =int(input())
b=int(input())
co =complex(a,b)
z =cmath.polar(co)
z =list(z)
for i in z:
    print(i)"""
"""from math import *
AB=int(input())
BC =int(input())
z=atan2(AB,BC)
print("Z=>:",z)
d =degrees(z)
print("DEGREE=>: ",d)
d = round(d)
print(u"{}\u00b0".format(d)) """

# N=5
# for row in range(1,N+1):
#     for col1 in range(1,row+1):
#         for col in reversed(range(1,row+1)):
#             print(col1,end="")
#     # for col in reversed(range(1,row+1)):
#     print()

for i in range(1, int(input()) + 1): 
    
    # printing the triangle of the number
    print((10 ** i - 1) ** 2 // 81)
