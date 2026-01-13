vowel = ['a','e','i','o','u','A','E','I','O','U']
N = input("Enter Any Character:")
vowel_c =0
cons = 0
for N in N:
    if N in vowel:
        #print("This Character Is Vowel:: ",N)
        vowel_c+=1
    else:
        print("This Character Is Cons:: ",N)
        cons+=1
print(len(N))
print("Vovel Count ",vowel_c)
print("Cons Count ",cons)
        