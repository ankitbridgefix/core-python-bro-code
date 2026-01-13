stud = [("Ram","F",20),("Ankit","B",28),("Zainam","A",19)]
#conver Euro 

euro  = lambda data: (data[0],data[1],data[2]*2)
store_euro = list(map(euro,stud))
print(store_euro)
