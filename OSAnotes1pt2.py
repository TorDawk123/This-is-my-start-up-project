#OSA notes 1 pt 2
#classes

class Cat:

    #attribute/intializer
    def __init__(self, a, b, c=1000):

        self.__a = a
        self.__b = 100
        self.__c = c

class creditcard:

    def __init__(self,card_owner, limit=7000):
        self.__card_owner = card_owner
        self.__credit_limit = limit
        self.__balance = 0

    def get_card_owner(self):

         return self.__card_owner

    def set_card_owner(self, data):
        self.__card_owner = data

    def charge(self, amount):

        if amount + self.__balance > self.__credit_limit:
            print("error you have reached your limit" )
        else:
            self.__balance += amount

    def make_payment(self, amount):
        self.__balance -= amount


card1 = creditcard("david", limit=3000)
card2 = creditcard("emily")
card1.get_card_owner()
card2.get_card_owner()
        
        
