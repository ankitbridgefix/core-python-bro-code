friend = [("Ram",12),("Anand",21),("Kiara",23),("Aish",34),('Kriti',18)]
print(friend)
age = lambda ages : ages[1]>=18
mutual = list(filter(age,friend))
print(mutual)