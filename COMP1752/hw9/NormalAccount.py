from Account import Account

class normalAccount(Account):
    def __init__(self, name='', balance=0, id=0, MAX_amount=0, fee = 1):
        super().__init__(name, balance, id, MAX_amount)
        self.fee = fee