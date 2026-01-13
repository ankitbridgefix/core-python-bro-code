class A:
    d = 100
    
    def example_ins(self):
        self.b =200
        print("This is Instance Method",self.b) #A.b ==>Error
        #print("Hello! from %s" % self.__class__.__name__)
    
    @classmethod    
    def example_class(cls):
        cls.c = 300
        print("This is Class Method",cls.c,A.c)
    
    
    
    @staticmethod
    def exmaple_static():
        s = 400
        print("This is Static Method:",A.c)
        

#===INSTANCE METHOD
A.example_class()
obj = A()
#A.example_ins()  #TypeError: example_ins() missing 1 required positional argument: 'self'
obj.example_ins()  
print("=================================================")
#CLASS METHOD
A.example_class()
obj.example_class()
print("===============")
#STATIC METHOD

A.exmaple_static()
obj.exmaple_static()

