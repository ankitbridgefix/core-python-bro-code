class Supermarket(object):
    product = "Milk Buttor"  # class attribute
    
    def __init__(self, product, best_before):
        self.best_before = best_before  # instance attribute
        self.product = product
    @staticmethod    
    def normalize_product_name(product):
        product = product.capitalize().strip()      
        return product
    

#print(Supermarket.normalize_product_name("milk   "))

# class Test:
#     @classmethod
#     def class_method(cls):
#         cls.name = "India"
#     def instance_method(self):
#         self.sname = "MP"
        
# Test.class_method()
# # print(Test.name)
# t = Test()
# t.instance_method()
# print(t.sname)

d = {"rice":1,'soil':2}

#for k in d.keys():
k ="rice"
if k in d.keys(): 
    v = d[k]
    d[k] = v+2
    
print(d)