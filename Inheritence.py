class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birtday(self):
        print("Happy Birthday: You were", self.age, 'years old')


class Employee(Person):
    def __init__(self, name, age, eid):
        super().__init__(name, age)
        self.eid = eid

    def calculate_pay(self, hours_worked):
        pay = self.age * hours_worked
        print('You earned: ', pay)

class Manager(Employee):
    def __init__(self, name, age, eid, pay):
        super().__init__(name, age, eid)
        self.pay = pay

    def givepay(self):
        print('Pay given')


p = Person('Ahmad', 24)
e = Employee('Hamid', 27, 5)
m = Manager('Hamid', 27, 5, 4000)
# p.birtday()
e.birtday()
e.calculate_pay(24)
m.birtday()
m.givepay()