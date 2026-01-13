def Main_func(func):

    def Second(a,b):
        print("Hi I am a Secon func Start:")
        #func()
        print("Hi  i am a Second Func End:")

    return Second()

@Main_func
def Parm_func(a,b):
    #return "hello Friend"
    print("I am Param Function Decborator")
    return a+b

print(Parm_func(1,2))
    

