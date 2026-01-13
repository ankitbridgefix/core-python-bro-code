
"""a = 10  
print("a =", a,sep='dddd', end='\n\n\n')  
print("a =", a, sep='0', end='$$$$$')  

print("\n================LIST=====================")

L1 = ["John", 102, "USA"]      
L2 = [1, 2, 3, 4, 5, 6] 
L1[0]=12
L1.append("iNDIA")
print(L1)
print(type(L1))


print("\n================Tuple=====================")

tup = ("Apple", "Mango" , "Orange" , "Banana")  
print(type(tup))  

print(tup[0])  
print(len(tup))

print("\n=====================DICT================")

employee = {"Name": "John", "Age": 29, "salary":250000,"Company":"GOOGLE"}      
print(type(employee))      
print("printing Employee data .... ")   
employee['Name'] = "MR John"  
print(employee)

print("\n=====================SET================")

Month = {"January", "February", "March", "April", "May", "June", "July"} 
 
print(Month)  
print(type(Month))

"""

"""a=10
def the_outer_function(): 
    global a 
    print(a+10)
    var = 10  
    def the_inner_function(): 
        global a
        a=a+100
        print("Inner funtion Inside Global Variab:",a) 
        var = 14  
        print("Value inside the inner function: ", var)  
    the_inner_function()  
    print("Value inside the outer function: ", var)  
  
the_outer_function()"""

"""for i in range(15):  
    
    print( i, end = " ")  
        
    # breaking the loop when i = 9  
    if i == 9:  
        break     
print() """ 

i = 0 # initial condition  
while i < 15:  
        
    # When i has value 9, loop will jump to next iteration using continue. It will not print  
    if i == 9:  
        i += 3  
        continue  
    else:  
        # when i is not equal to 9, adding 2 and printing the value  
        print( i+2, end = " ")  
            
    i += 1  