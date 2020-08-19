# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:04:02 2020

@author: akash
"""


class Employee1: 
    
    raise_amount = 1.04
    num = 0
    
    def __init__(self, first, last, pay):                           # special init methode or construstor
        self.first = first                                          # ir recive the instance as 1st argument
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        #by using def function we reduce code size 
        Employee1.num = Employee1.num+1
        
    def fullname(self):                                            # 1st rgument is instance itself
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount 
        #self.pay = self.pay * Employment.raise_amount 
        


emp_3 = Employee1('Corey', 'Schafer', 50000)
emp_4 = Employee1('Test', 'Employee', 60000) 


emp_3.pay
#Employee1.apply_raise(emp_3) this is giving error beacuse we can access class varivable by class name or instance name    


Employee1.apply_raise(emp_3)
emp_3.pay



print(emp_3.__dict__)   # print out the namespace of instance
                        #Python itself maintains a namespace in the form of a Python dictionary.
print(Employee1.__dict__)   # print out the namespace of class

Employee1.raise_amount = 1.07  # here we can change the class variable

emp_3.raise_amount = 1.19   # only affect instance



# how to check no of instance created for that
# just add  self.num = self.num+1

Employee1.num
