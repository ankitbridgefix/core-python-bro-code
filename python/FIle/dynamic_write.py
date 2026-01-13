#Dyanamic write

with open("web.info","a") as wp:
    print("Enter The data from Kbd stop")
    print("-"*50)
    while True:
        kbddata = input()
        if kbddata != 'stop':
            wp.write(kbddata+"\n")
        else:
            break
        print("*"*50)
        print("\n Data witten to filesuccess")