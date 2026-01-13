from collections import Counter

X= int(input("Enter Number of Shoes: "))
print("Number Of Shoes:",X)
l_size = [int(i) for i in input("Enter the shoes Size WIth Space Seprater:").split()]
print(l_size)
print(Counter(l_size))
sizes = Counter(l_size)
n_o_c = int(input("Enter Number of Customer: "))
print("nter Shoes Size And Price")
earned = 0
for i in range(n_o_c):
    s,price = input().split()
    price=int(price)
    s = int(s)
    if(sizes[s]):
        sizes[s] = sizes[s]-1
        print("price",price)
        earned = earned + price
    
print(earned)