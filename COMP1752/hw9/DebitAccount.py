from Account import Account

class debitAccount(Account):
    def __init__(self, name='', balance=0, id=0, MAX_amount=0, limit=0):
        super().__init__(name, balance, id, MAX_amount)
        self.limit = limit






