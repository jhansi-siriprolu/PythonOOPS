class BankAccount:
    def __init__(self, account_name, account_number, account_balance):
        self.name = account_name
        self.number = account_number
        self.balance = account_balance

    def __str__(self):
        return f"Bank account details for {self.name} with account number {self.number} has a balance of {self.balance}"

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdrawal(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
        else:
            print("NOT ENOUGH BALANCE")
