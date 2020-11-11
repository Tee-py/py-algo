class Dog:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    
    def setBuddy(self, buddy):
        if self.__dict__.get("buddy"):
            pass
        else:
            self.buddy = buddy
            buddy.setBuddy(self)
    
    def __repr__(self):
        return self.name

dog_1 = Dog("Kyrie", "Male")
dog_2 = Dog("Tyler", "Female")
dog_1.setBuddy(dog_2)
dog_2.setBuddy(dog_1)

print(dog_1.buddy.__dict__)
print(dog_2.buddy.__dict__)


class CreditCard:

    def __init__(self, customer, bank, card_no, limit):
        self._customer = customer
        self._bank = bank
        self._card_no = card_no
        self._balance = 0
        self._limit = limit

    def __repr__(self):
        return f"{self._customer} - {self._card_no}"

    def get_customer(self):
        return self._customer

    def get_balance(self):
        return self._balance

    def get_bank(self):
        return self._bank

    def get_card_no(self):
        return self._card_no

    def get_limit(self):
        return self._limit

    def credit(self, amount):
        if amount + self._balance > self._limit:
            print("Limit Exceeded")
        else:
            self._balance += amount
            print("Credit Successfull")


print("\n")
card = CreditCard("Emmanuel Oluwatobi", "Kuda Bank", "3124105657", 100000)
print(card)
card.credit(56000)
print(card.get_balance())
card.credit(56000)
print(card.get_balance())