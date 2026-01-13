##Filter Function
# positive  = lambda a : a>0
# l = [10,-5,8,7,9,0]
# f  = filter(positive,l)
# print(list(f))


##Map Function
# square = lambda a: a**2
# l=2,3,4,5,6
# res = map(square,l)
# print(list(res))

##reduce
big = lambda a,b: a if a>b else b
l = [1,5,4,7,8,9,10]
from functools import reduce
res = reduce(big,l)
print(res)
