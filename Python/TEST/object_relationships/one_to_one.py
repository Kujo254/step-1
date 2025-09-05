class Person:
    def __init__(self, name):
        self.name = name
        self.passport = None

class Passport:
    def __init__(self, number):
        self.number = number
        self.owner = None

if __name__ == "__main__":
    p1 = Person("Alice")
    pass1 = Passport("A1234567")

    p1.passport = pass1
    pass1.owner = p1

    print(f"{p1.name} has passport {p1.passport.number}")
    print(f"Passport {pass1.number} belongs to {pass1.owner.name}")
