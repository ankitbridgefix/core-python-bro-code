def voter(value):
    if value>=18:
        return "Voter"
    else:
        return "Not Voter"

d = {"Ram":19,"Ravina":20,"kriti":18,"Jeqline":15,"Aish":12}

new = {key:value if value>=18 else "You are child" for key ,value in d.items()}
print(new)

print("*"*50)
f_d = {key:voter(value)for key ,value in d.items()}
print(f_d)