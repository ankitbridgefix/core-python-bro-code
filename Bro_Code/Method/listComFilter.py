stud = [20,403,40,493,300,100,120]

passed = list(filter(lambda x:x>100,stud))
print(passed)
print("==========================")
passed_stud = [ i for i in stud if  i>100]
print(passed_stud)
print("==========================")
status = [i if i>100 else "Failed" for i in stud]

print(status)
