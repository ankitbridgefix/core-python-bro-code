def Main_Program(func):
    def wrap(a,b):
        print(f"A=={a} ==B {b}")
        if a>b:
            print(f"{a}>{b}")
            #print(func(a,b))
            return func(a,b)
        else:
            print(f"{b}>{a}")
            #print(func(b,a))
            return func(a,b)
            
    
    return wrap


@Main_Program
def sum(x,y):
    return x+y
print(sum(100,120))
