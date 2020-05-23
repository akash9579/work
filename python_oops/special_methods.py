# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:29:56 2020

@author: akash
"""


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):                                      # special methods
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):                                                        # special methods also acees bt repe()
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)                                                          # here we are adding object by using special method __add__

print(len('akash') )                                                          # for every build in function we can overright using dunder method __len__() so it can work on object to
print(len(emp_1))

print(emp_1)                                                                  # Corey Schafer - Corey.Schafer@email.com getting this output due to str methode

print(Employee.__repr__(emp_1))                                               # Employee('Corey', 'Schafer', 50000) getting this
print(repr(emp_1))                                                            #Employee('Corey', 'Schafer', 50000) getting same stuff
print(repr(emp_2))


# for extra refference check this https://docs.python.org/3/reference/datamodel.html#special-method-names