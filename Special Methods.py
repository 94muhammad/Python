# __init__ is an example of dunder which is sometimes referred to as dunder init
# repr() is an unambiguous representation of the object (used for debugging etc)
# str() is more readable (used for display for the end user)
# there are other dunder methods such as add, sub, len etc. more on https://docs.python.org/3/reference/datamodel.html

class Employee:

    total_emp = 0
    raise_pay = 1.04 #class variable to be used for method below

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Total number of employees
        Employee.total_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def raise_amount(self):
        self.pay = int(self.pay * self.raise_pay)

    def __repr__(self):
        return "Employee('{}','{}',{})". format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
