from bankaccount import BankAccount

acc1 = BankAccount("Jhansi", 123, 50)
print("Printing an objct acc1")
print(acc1)


print(type(acc1))

print(acc1.name)
print(acc1.number)
print(acc1.balance)

acc1.deposit(100)
print(acc1.balance)

acc1.withdrawal(10)
print(acc1.balance)

acc1.withdrawal(200)

print("Printing an objct acc1")
print(acc1)
