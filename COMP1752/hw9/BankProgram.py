import random
from NormalAccount import normalAccount
from DebitAccount import debitAccount
from VIPAccount import VIPAccount
from Menu import Menu

class BankProgram(Menu):
    def __init__(self):
        super().__init__()
        
    #3 ham add account ae
    def add_normal_account(self, a):
        self.normal_account.append(a)

    def add_vip_account(self, a):
        self.vip_account.append(a)

    def add_debit_account(self, a):
        self.debit_account.append(a)

    def run(self):
        self.running = True
        while self.running:
            self.print_menu()
            self.do_task(self, self.get_option(self))
            if self.get_option() == 7:
                self.running = False
                break
            

    def do_task(self, option):
        if option == 1:
            a = normal_account_config()
            BankProgram.add_normal_account(self, a)
            print("Normal account added!")
        elif option == 2:
            a = vip_account_config()
            BankProgram.add_vip_account(self, a)
            print("VIP account added!")
        elif option == 3:
            a = debit_account_config()
            BankProgram.add_debit_account(self, a)
            print("Debit account added!")
        elif option == 4:
            result = BankProgram.search()
            if result == None:
                print("Account not found!")
            else:
                print("Account found!", result)
        elif option == 5:
            BankProgram.withdraw()
        elif option == 6:
            BankProgram.deposit()


    def search(self, id):
        for acc in self.normal_account:
            if acc.id == id:
                print("Found", acc)
                return acc
        for acc in self.vip_account:
            if acc.id == id:
                print("Found", acc)
                return acc
        for acc in self.debit_account:
            if acc.id == id:
                print("Found", acc)
                return acc
        return None

    def withdraw(self, id, amount):
        acc = self.__get_id(id)
        if acc == None:
            print("wtf bro")
        else:
            acc.withdraw(amount)

    def deposit(self, id, amount):
        acc = self.__get_id(id)
        if acc == None:
            print("Don't be greedy, dear customer...")
        else:
            acc.deposit(amount)

def random_number():
    a = []
    for i in range(1, 6):
        a.append(random.randint(0, 9))
    return a

def normal_account_config():
    name = input("Enter name account: ")
    id = random_number()
    balance = 0
    MAX_amount = 0
    a = normalAccount(name, balance, id, MAX_amount)
    return a

def vip_account_config():
    name = input("Enter name account: ")
    id = random_number()
    balance = 0
    MAX_amount = 0
    a = VIPAccount(name, balance, id, MAX_amount)
    return a

def debit_account_config():
    name = input("Enter name account: ")
    id = random_number()
    balance = 0
    MAX_amount = 0
    a = debitAccount(name, balance, id, MAX_amount)
    return a

menuprogram = Menu
menuprogram.run(menuprogram)