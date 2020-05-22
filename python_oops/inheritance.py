# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:26:34 2020

@author: akash
"""


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'Employee', 60000)

print(dev_1.email)
print(dev_2.email)


class Developer(Employee):                                                    # here we are using inheritance
    raise_amt=1.88
    
    def __init__(self, first, last, pay, prog_lang):                          # here we are using special method with extra parameters
        super().__init__(first, last, pay)                                    # this function passing all 3 parameters to Employee classs
        self.prog_lang = prog_lang                                            # we are using new parameter here



dev_1 = Developer('akash', 'kamerkar', 50000)
dev_2 = Developer('Test', 'bhava', 60000)


print(help(Developer))                                                        # this function used to find developer class information


print(dev_1.pay)                                                              # 50000 which is basic
Employee.apply_raise(dev_1)                                                   # but here we are using basic class method
print(dev_1.pay)                                                              # 5200


print(dev_1.pay)                                                              # 50000 which is basic
Developer.apply_raise(dev_1)                                                  # here we are using subclass
print(dev_1.pay)                                                              ## 94000             



dev_1 =  Developer('Corey', 'Schafer', 50000 , 'python')                      # here we are checking subclass special function
print(dev_1.pay)
print(dev_1.prog_lang)  



class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):                     # here we are passing deafult argument None
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
            
            
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')




mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])                               # here we are using manager subclass

print(mgr_1.email)                                                            # its running beacuse manager class inherited from employee class

mgr_1.add_emp(dev_2)                                                          # here we can add emp to manager class list
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()                                                            # print available employee in the list



print(isinstance(dev_1, Manager))                                            ### checking instace , it is build in method


print(issubclass(Developer ,Employee))                                       ### checking subclass , it is build in method