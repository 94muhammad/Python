# class method

import datetime

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


    # using classmethod
    @classmethod
    def raise_pay_amnt(cls, amount):
        cls.raise_pay = amount

    @classmethod
    def from_string(cls, str):
        first, last, pay = str.split('-')
        return cls(first, last, pay)

    # regular method pass instance as the first argument which we called 'self', class methods pass class as the
    # first arguemnt which we called 'cls'. Staic methods dont need such arguments to operate i.e they don't pass
    # the instance or the class

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

# check Class method output
Employee.raise_pay_amnt(1.05)
print(emp_1.raise_pay)
print(emp_2.raise_pay)

# check Static Method output

my_date = datetime.date(2016,7,9)

print(Employee.is_workday(my_date))
