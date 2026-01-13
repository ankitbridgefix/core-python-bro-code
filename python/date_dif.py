"""def func1(*args,cname=None):
    sum =0
    print(cname)
    for arg in args:
        if(arg%2==0):
            print(arg)
        
func1(5,4,3,3,5,5,6,20,456,cname="python")"""


def func2(**kwargs):
    print("Key   Value")
    for key in kwargs:
        print(key)
        print(kwargs[key])
    

#func2(fname="Ankit",lanme = "Patidar")

def logIn(**kwargs):
    user_data = {'username':['ankit','ram','rahul','manoj'],'pwd':['11','22','33','44']}
    d = user_data["username"]
    p_i = user_data["pwd"]
    print(p_i[d.index(kwargs)])
    try:
        c = d.index(kwargs["username"])
        if(c):

            print(c)
            # c ='rahul'
            # if(c in d):
            #     print("hhh")
            for val in kwargs.values():
                #print(kwargs['username'])
                if(kwargs['username'] in d):
                    print("Username match  {}".format(kwargs["username"]))
                else:
                    print("Username Incorrect {}".format(kwargs["username"]))
        else:
            print("no")
    except ValueError:
        print("value")
        
logIn(username ="ankit")
logIn(username ="Rahul")
logIn(username = "ram")
logIn(username = "manoj")