# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:15:24 2020

@author: akash
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()


print(emp_1)   # emp1 and emp2 are the instance of class
print(emp_2)  

emp_1.first = 'akash'
emp_1.last = 'kamerkar'
emp_1.email = 'apkamerkar@gmail.com'
emp_1.pay = 300000


emp_2.first = 'shubham'
emp_2.last = 'kamerkar'
emp_2.email = 'apkamerkar@gmail.com'
emp_2.pay = 124546

print(emp_1.email)
print(emp_1.pay)


##### first,last,email are the instance variable which change with instance
#### its not same like class variable
#########  in the above code every time we have to assign value to variable but we can reduce this code 


class Employee1: 
    def __init__(self, first, last, pay):                           # special init methode or construstor
        self.first = first                                          # ir recive the instance as 1st argument
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        #by using def function we reduce code size 
        
    def fullname(self):                                            # 1st rgument is instance itself
        return '{} {}'.format(self.first, self.last)


emp_3 = Employee1('Corey', 'Schafer', 50000)
emp_4 = Employee1('Test', 'Employee', 60000) 

print(emp_1.email)

print(emp_4.fullname())      #this one
Employee1.fullname(emp_4)    # and this one both are same here we are passing instance as argument


# working of class concept is same as java in python 