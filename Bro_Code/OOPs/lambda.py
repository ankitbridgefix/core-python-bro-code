double = lambda x:x*2
print(double(5))

multi = lambda x,y,z:x*y*z
print(multi(2,3,4))

full_name = lambda first_name,last_name : f"{first_name} {last_name}"

print(full_name("Rahul","Singh"))

age_check = lambda age : True if age >18 else False

print(age_check(100))