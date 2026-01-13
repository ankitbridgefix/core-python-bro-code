def divident(x):
    def divisor(y):
        return y/x
    
    return divisor

d = divident(2)
print(d(10))