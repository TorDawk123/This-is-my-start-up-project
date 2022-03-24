#osa notes 4 pt 3

#class declare
class Automobile():

    def __init__(self,make,model,price,mileage=0):
        #dobule underscore makes it private
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    #update method 
    def set_make(self, make):
        self.__make = make

    #access method= it should current value
    #get methods
    def get_make(self):
        return self.__make
        

    def get_model(self):
        return self.__model
        
    def get_mileage(self):
        return self.__mileage

    def get__price(self):
        return self.__price

    #set methods
    def set_model(self,model):
        self.__model = model

    def set_mileage(self,mileage):
        self.__mileage = mileage

    def set_make(self,make):
        self.__make = make

    def set_price(self,price):
        self.__price = price

#instance of the class automobile
#create a variable then set it equal(=) to the class name with this () at the end
automobile1 = Automobile('Toyota','civic',10000,20000)
automobile2 = Automobile("BMW", 'x3', 30000, 40000)

#in the ide you will type automobile.get_whatever()

#next class for the problem
class car(Automobile):

    def __init__(self,doors=4,make,model,mileage,price):
        #create the attributes
        super().__init__(make,model,price,mileage)

    def get_door(self):
        return self.__doors

    def set__doors(self.data):
        self.__doors = data

car1 = Car("Honda", 'Accord',30000,1000)

class Truck(Automobile):

    def __init__(self,make,model,mileage,price,drivetype):
        super().__init__(make,model,price,mileage)
        self.__drivetype = drivetype
