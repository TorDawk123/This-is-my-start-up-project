#osanotes2 pt 3
class A:

    #static variables belong to the whole class
    static = 0

    def __init__(self,inst):
        #instance---> attribute it belongs rto
        #instance of class
         self.instance = inst
   
    #self key word in () is mandatory
    #get method/instance method
    def get(self):
        return self.instance

    #class method
    @classmethod
    def change(cls):
        cls.static = "apple"

    #static method
    #calculates three numbers
    @staticmethod
    def calculate_sum(x,y,z):
        return x + y + z
   
    #anther static mathod
    @staticmethod
    def display():
        print("this is a static mehtod")
   
    #set method with key word (self) is mandatory
    #is an instance method
    def set(self,data):
        self.instance = data

    def update_static(self):
        # refer to staic variables
        A.static = 100

a1 = A("apple")
a2 = A(200)

#instantiate the class
#use an object to access the value of an attribute
print(a1.instance)

#static variables
#an instance or the class to access the value of it
print(a1.static)
print(A.static)

#to update the static variable
#a1.static = 2000 < this is not static variable but a local variable
A.static = 50
