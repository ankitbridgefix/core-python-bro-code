# import shutil
# shutil.copy2('test2.txt','text.txt')
l = [["Ankit","Ram"],[1,2,3],["@","$","&"]]

c = 1
while c <=len(l):
    for i in l[c-1]:
        print(i)
    print("+=======================+")
    c = c+1

if __name__ =="__main__":
    print("Module Run Directly")

else:
    print("Module Not run Directly")