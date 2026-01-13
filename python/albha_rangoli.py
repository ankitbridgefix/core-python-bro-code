# import string
# des = string.ascii_lowercase
# for i in range(3):
#     print("-".join(des[i:3]))
    
"""n,m = map(int,input().split())
A=[]
B=[]
for i in range(n):
    A.append(input())
for j in range(m):
    B.append(input())

print("Group Of A",A)
print("Group Of B",B)"""


# test_list = [5,2,1,4,4]
# test_list =[1,2,3,4]



# print ("The original list is : " + str(test_list))

# res = [test_list[i + 1] - test_list[i] for i in range(len(test_list)-1)]

# # printing result
# print ("The  : " + str(res))


# Enter your code here. Read input from STDIN. Print output to STDOUT
# n,m  = map(int,input().split())
# from collections import defaultdict
# d = defaultdict(list)
# for i in range(n):
#     d[input()].append(i+1)
# for j in range(n):
#     B =input()
#     if B in d:
#         # for i in d[B]:
#         #     print(*i,end=" ")
#         # print()
#         print(*d[B])
       


# c=0
# for i in A:
#     if(i in B):
#         for j in B:
#          if(j==i):
#            a=A.index(i,c)
#            print(a+1)
#            c+=1
# n = int(input("Len of Lst"))
# lst =list(map(int,input().strip().split()))[:n]
# print(lst)

a =2
n =4
s= 0
for i in range(n):
    s +=a**i 

print(s)

