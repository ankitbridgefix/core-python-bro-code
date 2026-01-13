try:
    with open('test.tx1t') as file:
        print(file.read())

except FileNotFoundError:
    print("File Does Not Exits:")