# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:08:40 2020

@author: CSE
"""

import logging

# basic logging stuff
print("logging check")
logging.error("check 1")



#we can config the logging also using  basicConfig
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')

#set all parameters for basicconfig for logging
logging.basicConfig(filename='test4.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


#logging variable data
name = 'John'

logging.error('%s raised an error', name)

# basic of logger object
# steps
# Create a custom logger
# Create handlers
# Create formatters and add it to handlers
# Add handlers to the logger



"""

import logging
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('file.log')
f_handler.setLevel(logging.ERROR)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.warning('This is a warning')
logger.error('This is an error')

"""