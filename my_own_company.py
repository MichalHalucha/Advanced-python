class Employee:
    def __init__(self, x, y):
        self.name = x
        self.surname = y

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class Programmer(Employee):
    def __str__(self):
        return super().__str__() + " - Programmer"

class Manager(Employee):
    def __str__(self):
        return super().__str__() + " - Manager"

class Company:
    def __init__(self, e):
        self.employees = e

    def __str__(self):
        return "\n".join([str(e) for e in self.employees])

m = Manager("Steve", "Jobs")
p1 = Programmer("Guido", "van Rossum")
p2 = Programmer("Rowan", "Mr.Bean")
c = Company([m, p1, p2])
