# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:27:36 2020

@author: CSE
"""

# basic of logging
# there are 5 basic logging level
# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

"""only higher logging level greater than warning level apear in log file by default

   we also change the log message format by using format 
   check this-->https://docs.python.org/3/library/logging.html#logrecord-attributes
   
   

"""






import logging

"""#logging.basicConfig(filename='test.log', level=logging.DEBUG)   for changing logging level and store logs in log file
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
"""

logger = logging.getLogger(__name__) # create new logger
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')


file_handler = logging.FileHandler('test2.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)


def function():
    print("1st function")
    
    
def function1():
    print("2nd function")
    
    
def add(a,b):
    num=a+b;
    
    
    
a=10
b=46

add(a, b)    
logger.error("add function completed succesfully")
function()
function1()

