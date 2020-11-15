import re

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

class CreditCard:

    def __init__(self, customer, bank, card_no, limit):
        self._customer = customer
        self._bank = bank
        self._card_no = card_no
        self._balance = 0
        self._limit = limit

    def __repr__(self):
        return f"{self._customer} - {self._card_no}"
    #Overloading the addition operator for the class
    def __add__(self, cl):
        return self._balance + cl._balance

    #Overloading the boolean operator for the class Instances
    def __bool__(self):
        return True if self.get_balance()>0 else False


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

    def debit(self, amount):
        if amount > self.get_balance():
            print("Insufficient Funds")
        else:
            self._balance -= amount
            print(f"a sum of {amount} was debited successfully")

class Vector:

    def __init__(self, dim):
        self._coords = [0]*dim

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, index, val):
        self._coords[index] = val
    
    def __add__(self, other):
        if len(self._coords) != len(other._coords):
            raise ValueError("Length must be the same!!!")
        output = Vector(len(self))
        for i in range(len(output)):
            output[i] = self[i] + other[i]
        return output

    def __eq__(self, other):
        return len(self) == len(other)
    
    def __ne__(self, other):
        return not len(self) == len(other)

    def __delitem__(self, k):
        self._coords = [mem for mem in self._coords if mem != self[k]]


    def __str__(self):
        return f"<{str(self._coords)[1:-1]}>"


class Polynomial:

    def __init__(self, expr):
        self._expr = expr
        self._members = self.extract_members()

    def extract_members(self):
        member_regex = re.compile("")



class Sequence:

    def __init__(self, seq_type):
        self.type = seq_type
        print("Initiated sequence object")

