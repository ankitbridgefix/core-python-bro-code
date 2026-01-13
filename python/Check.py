# d="#$%@^&*"
# alnum = []
# alpha = []
# digit =[]
# low= []
# up = []
# for s in d:
#     if s.isalnum():
#         alnum.append("True")
#     else:
#         alnum.append("False")
#     if d.isdigit() == False:
#         if s.isalpha():
#             alpha.append("True")
#         else:
#             alpha.append("False")
#     if s.isdigit():
#         digit.append("True")
#     else:
#         digit.append("False")
#     if d.isdigit() == False:
#         if s.islower():
#             low.append("True")
#         else:
#             low.append("False")
#         if s.isupper():
#             up.append("True")
#         else:
#             up.append("False")
# print(any(alnum))
# print(any(alpha))
# print(any(digit))
# print(any(low))
# print(any(up))
"""string = '123456fdghghU'
print(any(s.isalnum() for s in string))
print(any(s.isalpha() for s in string))
print(any(s.isdigit() for s in string))
print(any(s.islower() for s in string))
print(any(s.isupper() for s in string))"""

#Replace all ______ with rjust, ljust or center. 

"""thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))"""
    

from textwrap import TextWrapper
# texts = """This method wraps the input paragraph such that each line is at most width characters long in the paragraph. If the input has some content, it returns a list of lines as output."""

# wrapper = TextWrapper(width=10)
# wrap_list  = wrapper.wrap(text=texts)
# print(wrap_list)
# for line in wrap_list:
#     print(line)
#     print(len(line))
import textwrap
    
# def wrpa():
#     texts = """This method wraps the input paragraph such that each line is at most width characters long in the paragraph. If the input    has some content, it returns a list of lines as output."""
#     l=""
#     #wrapper = TextWrapper(width=20)
#     wrap_list  = textwrap.fill(texts,20)
#     #print(wrap_list)
#     return wrap_list
    
         
# print(wrpa())

"""from itertools import product
A =list(map(int,input().split()))
B =list(map(int,input().split()))
k = list(product(A,B))
for j in k:
    print(j,end=" ")"""
    
# from itertools import permutations
# a="HACK"
# z =permutations(a,2)
# for i in z:
#     print(i)
from itertools import permutations

"""perm = permutations('HACK', 2)
perm =sorted(perm)
for p in perm:
    print("".join(p))"""

txt = "HACK"
for  i in txt:
    print(sorted(''.join(i)))
    





