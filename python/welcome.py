n = 7
m=21
"""for row in range(n):
    
    for col in range(m//2-row+1):
        print("-",end=" ")
    for i in range(row+1):
        print(".",end="")
    for i in range(1):
        print("|",end="")
        
    for i in range(row+1):
        print(".",end="")
    
    for col in range(m//2-row+2,2):
        print("-",end=" ")
        
    print()
    """

n = 7
m=21
def print_door(N, M):
        symbol = ".|."
        # Upper part
        for i in range((N//2)):
            print((symbol*((2*i)+1)).center(M, "-"))
        # Middle part
        print("WELCOME".center(M,"-"))
        # Lower part
        for i in reversed(range((N//2))):
                print((symbol*((2*i)+1)).center(M, "-"))

print_door(n,m)
#n, m = map(int, input().split())
#print_door(n, m)



"""N,M = input().split()
N=int(N)
M=int(M)
sym = ".|."
#Upper Part
for i in range(N//2):
    print((sym*((2*i)+1)).center(M,"-"))
else:
    print(("WELCOME").center(M,"-"))
for i in reversed(range(N//2)):
    print((sym*((2*i)+1)).center(M,"-"))"""
    
# for i in range(17+1):
#     b =bin(i).replace("0b","")
#     o =oct(i).replace("0o","")
#     h =hex(i).upper().replace("0X","")
#     print("{:^3}{:^3}{:^3}{:^3}".format(i,o,h,b))
"""def print_formatted(number):

    width = len("{0:b}".format(number))
    print(width)

    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))
"""
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)
"""while(True):
    n = int(input("Enter Any Number:"))
    le = len("{0:b}".format(n))
    print("len ",le)
    
    print("{0:{w}o}".format(n,w=le))
    """

# tex ="chris alan"
# tex2 = "1 w 2 r 3g ank"
# d_sp = tex.split()
# name=""
# for i in d_sp:
#     if(len(i)>0):
#         if(i[0].isdigit()):
#             name+=i+" "
#         else:
#             name+=i[0].upper()+i[1:]+" "
#     else:
#         name =name+" "
# # print(name)
# print(name[:-1])

"""def solve(s):
    for i in s.split():
        print (i)
        s = s.replace(i,i.capitalize())
    return s

print(solve(tex2))
"""
   








