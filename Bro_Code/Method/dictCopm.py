cit = {"India":20,"New_york":30}
ne = {key:(value*2) for key,value in cit.items()}

print(ne)

user = ["ankit",'Ram',"priyanka"]
pwd = ["ank@123",'Ram@123',"priayanak@123"]

for u,p in zip(user,pwd):
    print({u:p})

use = zip(user,pwd)
print(dict(use))
for u in dict(use).items():
    print("******")
    print(u)