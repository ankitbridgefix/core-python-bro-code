# n=int(input("Enter Any number:"))
# temp = n
# rev = 0
# while(n>0):
#     digit = n%10
#     rev =rev*10+digit
#     n=n//10

# if(temp==rev):
#     print("This Number is Palindrome Number:",rev)

# else:
#     print("This Number is Not Palindrome Number:",temp)

a="12322"
B=a[::-1]
print(B)
if(a==B):
    print("Ther Are")
else:
    print("NOT")