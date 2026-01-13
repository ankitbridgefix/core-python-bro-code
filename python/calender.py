"""nums = ['121','252','221']
z =any(map(lambda x :x==x[::-1],num))
print(z)
n =any(map(lambda x:int(x)>0,num))
print(n)
print(all(map(lambda x:int(x)>-1,nums)) and any(map(lambda x:x==x[::-1],nums)))"""

# s ="indore"
# z =lambda x : x.upper()[::-1]
# print(z(s))

"""s=10
print(f"Your Roll No Is {s:e}")

form_numeric = lambda x : f"{x:e}" if isinstance(x,int) else f"{x:.2f}"

print(form_numeric(105))
print(form_numeric(105.25745))"""
# l = [1,2,3,2,4,3,2,5,6]
# big =list(map(lambda x,y: x if x>y else y,*l))
# print(big())

"""is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
#print(is_even_list)
for i in is_even_list:
    print(i())"""
# iterate on each lambda function
# and invoke the function to get the calculated value
# for item in is_even_list:
# 	print(item())

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# final_list = list(filter(lambda x: (x % 2 != 0), li))
# print(final_list)

# Python code to demonstrate
# Sorting a string
# using sorted() + reduce() + lambda

s = "Sorting1234"
a = "".join(sorted(s))
d =""
al=""
u=""
o =""
e=""
print(a)
for i in a:
    if(i.isdigit()):
        if(int(i)%2!=0):
           o+=i
        else:
            e+=i
    if(i.isalpha()):
        if(i.islower()):
         al+=i
    if(i.isupper()):
        u+=i
print(al+u+o+e)
print(d)












