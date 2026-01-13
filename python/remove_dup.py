# l =[1,2,1,3,4,4,5,6,7]
# l2 = []
# for i in l:
#     if i not in l2:
#         l2.append(i)
    
# print(l2)

# first = "Ankit"
# last = "Patidar"

# email = first[:2] + last[:4:-1] + "@gmail.com"
# print(email)

arr =[34,45,1,34,56,2,12,4,90]
# for i in range(0, len(arr)):    
#     for j in range(i+1, len(arr)):    
#         if(arr[i] > arr[j]):    
#             temp = arr[i];    
#             arr[i] = arr[j];    
#             arr[j] = temp;  
        
# for i in range(0, len(arr)):    
#     print(arr[i], end=" ");    
    
s =sorted(arr)
print(s[2])
   