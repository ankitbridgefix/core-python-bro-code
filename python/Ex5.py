"""a = int(input("Enter Any Number:"))
b = int(input("Enter Any Number:"))
c = int(input("Enter Any Number:"))
if(a>b) and (a>c):
    print("A Large Number:{}".format(a))
if(b>a) and (b>c):
    print(" B Large Number:{}".format(b))
if(c>a) and(c>b):
    print("C Large Number:{}".format(c))"""

# Check To Age of person Eligible in vote

"""age = int(input("Enter Person age:"))
if(age>=18) and (age<=100):
    print("You are Eligible to vote:")
elif(age>100):
    print("You are Old Age")
else:
    print("Sorry! You are not Eligible to vote")
"""

"""n = int(input("Enter Any Number:"))
if(n==10):
    print("Number Are Equals To 10")
elif(n==50):
    print("Number Are Equals To 50")
elif(n==100):
    print("Number Are Equals to 100 ")
else:
    print("Sorry Not Match Any ")
"""

"""

==========DOubt==================================
# Python code to demonstrate the working of
# dropwhile()



import itertools


# initializing list
li = [2, 4, 5, 7, 6,9,8]

# using dropwhile() to start displaying after condition is false
print ("The values after condition returns false : ", end ="")
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li)))


"""

#print Grade of report card
marks = int(input("Enter Marks:"))
if marks>85 and marks<=100 :
    print("Congrats ! You scored grade A")
elif marks>60 and marks<=85:
    print("You scored Grade B")
elif marks>45 and marks<=60:
    print("You scored grade C")
else:
    print("Sorry You are Fail")
