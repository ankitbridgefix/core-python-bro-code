# if __name__ == '__main__':
#     x = int(input("printx"))
#     y = int(input())
#     z = int(input())5
#     n = int(input())
#     lst = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
#     print(lst)


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

#     #print(sorted(set(arr), reverse=True)[1])
#     s = set(arr)
#     lst= list(s)
#     lst.reverse()
    
#     if lst[0]<=0:
#       print(lst[-1])
#     elif lst[1]==0:
#         print(lst[-1])
#     else:
#         print(lst[1])

#     print(lst)




"""Solved This Problem 9/12/2022 """
# if __name__ == '__main__':
#     lst = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
      
#         lst.append([name,score])
#         #x =sorted(set(score), reverse=False)[1]
#     print(lst)
"""lst = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
score_lst  =[]
for score in lst:
    print(score[1])
    score_lst.append(score[1])
print(score_lst)
print("Score",sorted(set(score_lst),reverse=False)[1])
x=sorted(set(score_lst),reverse=False)[1]
name_lst=[]
for i in lst:
    if x ==i[1]:
        print(i)
        name_lst.append(i[0])
print(name_lst)
print(sorted(name_lst,reverse=False))"""






#solved This Problem 09/12/2022 =16:35

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# #query_name = input()
# print(student_marks)

"""stu ={'ravi': [20.0, 30.0, 32.0], 'ram': [25, 25, 50]}
name  =input("Enter Student Name:")
search_stu = stu[name]
print(search_stu)
sum_marks = 0
for marks in search_stu:
    sum_marks+=marks
avg =sum_marks/3
print(avg)

print("%.2f"% avg)
    
print(sum_marks)"""

"""class Test:
    def i_m(self):
        print("this Is Is Instance Method") 
    @classmethod
    def c_m(cls):
        print("this Is CLASSS")
    
    @staticmethod
    def s_m():
        print("This Is Static Mthdoe")
    
t =Test()
t.i_m()
Test.c_m()
t.s_m()"""


"""#o['efg', 'is', 'bGst', 'for', 'eGGks']
l=['Gfg', 'is', 'best', 'for', 'Geeks']
out_lst=[]
for i in l:
    x = i.replace('G','_')
    #print(x)
    y  =x.replace('e','G')
    #print(y)
    z =y.replace('_',"e")
    out_lst.append(z)
print("Input==>",l)
print("Output==>",out_lst)
    """
def myFun(*args, **kwargs):
    print("args: ", args)
    l=list()

    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")


    

