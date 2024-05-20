class BankAccount:
    interest_rate = 0.08
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
    def calculate_iterest(self):
        self.balance += (self.balance * BankAccount.interest_rate)
        return self.balance
b1 = BankAccount("Jhansi",123,100)
b2 = BankAccount("Srikanth", 321, 100)

print(b1.interest_rate)
print(BankAccount.interest_rate)

print(b1.calculate_iterest())
BankAccount.interest_rate = 0.1
print(b1.calculate_iterest())
print(BankAccount.interest_rate)
print(b2.calculate_iterest())