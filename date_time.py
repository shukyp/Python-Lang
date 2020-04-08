#===========================================================================
#                           Date Time Module
#===========================================================================
"""
# Demonstrates using the Date/Time services of the Python Standard Library
#
# Author: Shuky Persky
#
"""

#===========================================================================
# Python standard library
# datetime: https://docs.python.org/3/library/datetime.html#module-datetime
# time      https://docs.python.org/3/library/time.html
# calendar  https://docs.python.org/3/library/calendar.html#module-calendar
#===========================================================================

import time         # Python Standard Library
import datetime     # Python Standard Library

#===========================================================================
#Accesses service provided ny Python Standard Library
def date_time_mdl():

    print ('\n\n ========  Date-Time Module is Running ')

    #shoe current date/time
    print('\nCurren Time: %s' % time.ctime())


    print ('\n -----------  Date-Time Module is Done >>>> ')
