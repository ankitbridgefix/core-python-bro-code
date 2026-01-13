stud = [("Ram","F",80),("Ankit","B",98),("Zainam","A",89)]

grade = lambda grades:grades[1]
stud.sort(key=grade,reverse=True)
for i in stud:
    print(i)
    
    