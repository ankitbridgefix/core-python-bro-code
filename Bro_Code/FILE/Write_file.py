text = '\nn = int(input("enter Any Value"))\nprint(n)' #"Hello Ankit \n How Are You \n  You are looking Goood"
with open ('test2.txt','a') as file:  # IF file is not Exist then file Is created authomaticaly
    file.write(text)