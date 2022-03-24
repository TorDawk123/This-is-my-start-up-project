#osanotes 4 pt 4
#inheritence

class parent1:

    def __init__(self,a):
        self.p1 = a

    def show_attribute(self):
        print(self.p1)

#class gives the initializer
class parent2:

    def __init__(self,a):
        self.p2 = a

    def show_attribute(self):
        print(self.p2)

#putting the previous class in the () establish the connections
#
class child1(parent1,parent2):

    #use the same parameters in the previous class
    #initializer
    #p1
    def __init__(self,a,b,c):
        super().__init__(a)
        parent1.__init__(self,a)
        parent2.__init__(self,b)
        self.c1 = c

    def show_c1(self):
        print(self.c1)
        
    
