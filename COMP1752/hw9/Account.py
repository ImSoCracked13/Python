class Account:
    def __init__(self, name='', balance = 0.0, id = 0, MAX_amount = 0):
        self.__name = name
        self.__balance = balance
        self.__id = id
        self.__MAX_amount = MAX_amount

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == '':
            print("Invalid")
        else:
            self.__name = name
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print("Invalid")
        else:
            self.__balance = balance 

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id


    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough")
        if amount <= 0:
            raise ValueError("you can not withddraw 0")
        if amount > self.__MAX_amount:
            raise ValueError("Too much")
        else:
            self.__balance -= amount
            print("Account balance now: ",self.__balance,"-",amount)


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("you can not deposit 0")
        else:
            self.__balance += amount
            print("Account balance now: ",self.__balance,"-",amount)