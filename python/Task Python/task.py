class A:
    d={}
    def add(self,name,value):
        self.name = name
        self.value = value
        if self.name in self.d.keys():
            v =self.d[self.name] 
            self.d[self.name] = v+self.value
        else:
            self.d[self.name]=self.value
    
    def read_all(self):
        print(self.d)
        

a = A()
a.add("rice",1)
a.add("Wheat",2)
a.add("rice",3)
a.add("other",1)
a.add('other',5)

a.read_all()
        