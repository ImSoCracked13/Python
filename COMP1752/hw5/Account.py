class Account:
    def __init__(self, name ="Unknown", balance=0, id = 0):
        self.__name = name
        self.__balance = balance
        self.__id = id
    # Read property
    @property
    def name(self):
        return self.__name
    # Write property
    @name.setter
    def name (self, name):
        if name == "":
            print("Invalid name.")
        else:
            self.__name = name
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance.")
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        if id >= 0:
            self.__id = id
        else:
            print("Invalid ID.")
    def withdraw(self, amount):
        if amount < 0:
            print('Invalid amount. Transaction cancelled.')
        elif amount > self.balance:
            print('Not enough balance. Transaction cancelled.')
        else:
            self.balance -= amount
            print('Withdrawal Successfully! New balance:', self.balance )
    def deposit(self, amount):
        if amount < 0:
            print('Invalid amount. Transaction cancelled.')
        elif amount > self.balance:
            print('Not enough balance. Transaction cancelled.')
        else:
            self.balance += amount
            print('Deposition Successfully! New balance:', self.balance)
    def transfer(self, amount, other_account):
        if amount > self.__balance:
            print('Invalid amount. Transaction cancelled.')
        elif amount > self.balance:
            print('Not enough balance. Transaction cancelled.')
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f'Transaction successfully. Source balance currently:', self.balance)
    def show_info(self):
        print(f'Account id: {self.id}\
                Accoount name: {self.name}\
                Account balance: {self.balance}')


Selen_Tatsumaki = Account('Selen', 20000)
print(Selen_Tatsumaki.name)
print(Selen_Tatsumaki.balance)

Selen_Tatsumaki.name = 'Selen Tatsumaki'
print(Selen_Tatsumaki.name)

Selen_Tatsumaki.balance = 40000
print(Selen_Tatsumaki.balance)


class Bank:
    def __init__(self, name = "Vietcombank"):
        self.__accounts = []
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if name == '':
            print('Invalid name')
        else:
            self.__name = name
    def __get(self, id):
        for acc in self.__accounts:
            if acc.id == id:
                return acc
        return None
    def add(self, acc):
        if self.__get(acc.id) != None:
            print('Account already exists.')                  
        else:
            self.__accounts.append(acc)
            print('Account added to the system.')
    def withdraw(self, id, amount):
        acc = self.__get(id)
        if acc == None:
            print(f'Account id {id} not found.')
        else:
            acc.withdraw(amount)
    def deposit(self, id, amount):
        acc = self.__get(id)
        if acc == None:
            print(f'Account id {id} not found.')
        else:
            acc.deposit(amount)
    def transfer(self, source_id, destination_id, amount):
        source_acc = self.__get(source_id)
        dest_acc = self.__get(destination_id)
        if source_acc == None:
            print(f'Account id {source_id} not found')
        elif dest_acc == None:
            print(f'Account id {destination_id} not found')
        else:
            source_acc.transfer(amount, dest_acc)
    def show(self, id):
        acc = self.__get(id)
        if acc == None:
            print(f'Account id {id} not found')
        else:
            acc.show()
    def show_all(self):
        for acc in self.__accounts:
            acc.show()


class BankProgram:
    def __init__(self, bank):
        self.bank = bank
    def print_menu(self):
        input(int("Choose any number below to proceed the transaction:\
                    1. Add account.\
                    2. Show all accounts.\
                    3. Show account.\
                    4. Withdraw currency.\
                    5. Deposit currency.\
                    6. Transfer currency."))
    def get_option(self):
        option = 0
        if option == 1:
            Bank.add()
            print("Your account is: {acc} and ID is: {id}")
        elif option == 2:
            print("Here are the current accounts exists in the database:")
            Bank.show_all()
        elif option == 3:
            print("Your account is: {acc} and ID is: {id}.")
            Account.show_info()
        elif option == 4:
            Account.withdraw()
            print("The money has been withdrawn successfully. Current balance is {self.balance}.")
        elif option == 5:
            Account.deposit()
            print("The money has been deposited successfully. Current balance is {self.balance}.")
        elif option == 6:
            Account.transfer()
            print("The money has been transferred successfully. Current balance is {self.balance}.")
        else:
            print("Invalid Number! Pick again.")
            return
    def do_task(self):
        BankProgram.print_menu()
        BankProgram.get_option()
        return 