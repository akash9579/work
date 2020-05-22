# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:05:04 2020

@author: akash
"""


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):                                     # special method
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):                                                       # instance method or regular method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod                                                              # class method
    def set_raise_amt(cls, amount):                                           # A class method takes cls as first parameter while a static method needs no specific parameters.
        cls.raise_amt = amount

    @classmethod                                                              #A class method is a method which is bound to the class and not the object of the class
    def from_string(cls, emp_str):                                            #we can say that its a constructor
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)                                          # class method return object

    @staticmethod
    def is_workday(day):                                                      # in static method we are just passing parameter and excuting function thats it
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)                                        # instead of this we include in class method
new_emp_1 = Employee.from_string(emp_str_1)                                   # it return object

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))