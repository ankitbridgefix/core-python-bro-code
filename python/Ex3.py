#Vovel And Consonant
# vowel =['a','i','o','e','u','A','I','O','E','U']
# vo = []
# co =[]
# n = input("Enter Any choice:")
# for i in n:
#     if(i  in vowel):
#         #print("this Is vowel")
#         vo.append(i)
#     else:
#         #print("This is consonant")
#         co.append(i)
    
# else:
#     print("Vovel",vo)
#     print("\n")
#     print("cons",co)


l = ['1,2,3,4',5,6]
#print(l)
l2=[]
for i in str(l):
    a = str(i)
    d= "".join(a.split("'"))
    d = "".join(d.split("["))
    d = "".join(d.split("]"))
    #d = "".join(d.split(","))
    print(d,end="")

    
#print(l2)
    