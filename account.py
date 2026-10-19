class Account:
    def __init__(self, number, owner, balance=0):
        if balance < 0:
            raise ValueError("Начальный остаток не может быть отрицательным")
        self.number = number
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"
