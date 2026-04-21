'''CLASS deep diving
(1) ENCAPSULATION <
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("=======ENCAPSULATION=======")
# ENCAPSULATION > public __private _protected


class Account():
    # state
    description = "The class makes bank accounts"

    # consructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdrow(self, amount):
        print("withdrow:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account('Norman', 1000)
my_account.get_balance()

print("------")
my_account.deposit(4300)
my_account.withdrow(400)
my_account.get_balance()

my_account.amount = 100000
my_account.owner = "Daniel"
my_account.get_balance()

print("------")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)

# account_owner = my_account.holder
print("before account_owner:", my_account.holder)

# my_account.change_ownership("Daniel")
my_account.holder = "Alex"
print("after account_owner:", my_account.holder)
