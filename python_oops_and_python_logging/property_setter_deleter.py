# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:28:18 2020

@author: akash
"""


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property                                                                 # known as property decorator we can use that method as attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')


emp_1.fullname = "Corey Schafer"                                              # without setter method we cant set the fullname method after doing @property also
                                                                              # for updating method we use setter,deleter method
print(emp_1.first)
print(emp_1.email)                                                            # due to @property we are using email method as a attribute
print(emp_1.fullname)

del emp_1.fullname