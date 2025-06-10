# leaerning oops with some projects


from math import acos, sqrt, pi


class Line:

    def __init__(self, coord1: tuple, coord2: tuple):
        self.coord1 = coord1
        self.coord2 = coord2
        self.x1, self.y1 = coord1
        self.x2, self.y2 = coord2

    def distance(self):
        return sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)


class Cylinder:

    def __init__(self, height=1, radius=1) -> None:
        self.height = height
        self.radius = radius

    def volume(self):
        return pi * self.radius**2 * self.height

    def surface_area(self):
        return 2 * pi * self.radius * (self.radius + self.height)


class BankAccount:

    def __init__(self, owner: str, balance: int = 1) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"Account Holder name : {self.owner}\nCurrent Balance : $ {self.balance}"

    def deposit(self, amount: int = 0) -> str:
        self.balance += amount
        return f"Amount $ {amount} deposited in the Account"

    def withdraw(self, amount: int = 0) -> str:
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal of amount $ {amount} successful!!!"
        return (
            f"The Withdrawal amount $ {amount} is greater than the current Balance!!!!"
        )


coord1 = (3, 2)
coord2 = (8, 10)
line = Line(coord1, coord2)

print(line.distance())
print(line.slope())

cylinder = Cylinder(2, 3)
print(cylinder.volume())
print(cylinder.surface_area())

account = BankAccount("Shubham", 100)
print(account)
account.deposit(20)
print(account)
account.withdraw(110)
print(account)
account.withdraw(20)
