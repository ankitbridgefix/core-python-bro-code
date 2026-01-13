"""def Outer_fun(func):
    print('Call Outer Function:',func)
    
    def Inner_func(*args):
        print("call INNer FUnc:",func)
        print(func(*args))
    
    
    return Inner_func
        
def add(x,y):
    return x+y       
    
a=Outer_fun(add)
a(2,412)

"""
# for j in range(1, 5):
#     print("J",j)
#     for i in range(1,5):
#         if(i<=2):
#           print("if",i)
#         else:
#             break

for i in range(2,0,-1):
    print(i)