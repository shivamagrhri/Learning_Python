class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total amount =", self.getBalance())
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount , "was credited")
        print("Total amount =", self.getBalance())
    def getBalance(self):
        return self.balance

acc1 = Account(10000, 4539001500044180)
acc1.debit(1000)
acc1.credit(500)