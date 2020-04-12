#===========================================================================
#                           Exceptions Module
#===========================================================================

"""
# Deals with the subhect of exceptions:
#   Raising, Catchingm Built-in and user exceptions
#   Exception Object is being used by above mechanisms
#
#   Protocols and exceptions
#       IndexError - Loops, Sequence:
#       ValueError (correct typw but inappropriate value)  e.g. int('hi') (non-numeric)
#       TypeError
#       KeyError:   lookup in a mapping fails (e.g. dictionary[key]
##
# Author: Shuky Persky
#
"""

import os
import sys
import math


DIGIT_MAP = {
    'zero'  :   '0',
    'one'   :   '1',
    'two'   :   '2',
    'three' :   '3',
    'four'  :   '4',
    'five'  :   '5',
    'six'   :   '6',
    'seven' :   '7',
    'eight' :   '8',
    'nine'  :   '9',
}


#===========================================================================
def convert(s):

    '''Coberts a string based digits into a number.
    The function handles its own excpetions and reports the error

    :param (str)s
                    string based numbers    e.g. "one two four"

    :return:(tuple)
                    (int) rc
                        0       - success
                        -1      - error
                    (str) msg
                        ''      - if rc == 0
                        'text'  - if rc == -1
                    (int) rslt   e.g. 124

    :raises:    None
    '''

    #init
    x = 0
    msg = ''
    rc = 0

    # conver
    rslt = ''
    try:
        for token in s:                 #run thru input
            rslt += DIGIT_MAP[token]
        x = int(rslt)                   # convert to int

    except (KeyError, TypeError) as e:  #exception catching
        x = -1                          #exception handling
        rc = -1
        msg = f"Convertion Error: {e!r}"

    return (rc, msg, x)                 #advise caller


#===========================================================================
def calc_sqrt(val):
    ''' Calculates the sqrt using the math library module

    :arg        val(float)
                    must be >= 0

    :return:
                (float) square roor of input

    :raises
                ValueError (Builtin Exception)
                Other exceptions are forwarded as is to the caller
    '''

    #is negative input
    if (val < 0):
        raise ValueError(f'QSRT: Negative input {val} is illegal')      #raising

    try:
        return(math.sqrt(val))

    except Exception as e:
        raise                                                           #re-raising


#===========================================================================
def finally_usage (path, folder):
    """Example on using Finally

    :arg    path(str)
                path which below 'folder' should be vreated

            folder(str)
                folder to create  below 'path'

    :raises
            OSError

    """

    pwd = os.getcwd()       # get current path

    try:
        os.chdir(path)      #change dir to path
        os.mkdir(folder)    #ctreate the folder

    except OSError as OS_e:
        print(f'\n\n{OS_e!r}')  #process exception
        raise

    finally:
        os.chdir(pwd)       #anyway return to pwd



#===========================================================================
def exceptions_mdl():
    '''
    #module entry point function
    Args-name(type) description
    :return(type)   description
    '''

    print ('\n\n ======== Exceptions Module is Running ')

    #-----------------------------------------------------------
    #                           convert
    #-----------------------------------------------------------

    #call the convert function / no exception
    rc, msg, rslt = convert("one two four".split())
    print ('\nRC={0}, Msg={1}, Value{2}'.format (rc, msg, rslt))

    #call the convert function / with exception
    rc, msg, rslt = convert("fail".split())
    print('\nRC={0}, Msg={1}, Value{2}'.format(rc, msg, rslt))


    #-----------------------------------------------------------
    #                             sqrt
    #-----------------------------------------------------------
    #calc_sqrt(9)
    #calc_sqrt(6.2)
    #calc_sqrt(0)
    try:
        calc_sqrt(-3)
        #calc_sqrt ('a')
        #calc_sqrt ('a')

    except ValueError as V_e:
        print(f'\n {V_e!r}')

    except:
        print('\nException took place')


    #-----------------------------------------------------------
    #                         finally_usage
    #-----------------------------------------------------------
    path = "t:\\calc"
    folder = 'aaa'
    try:
        finally_usage (path, folder)   #path doesn't exist

    except FileNotFoundError as FNF_e:
        print('\nPath doesn\'t exist {path}')

    except Exception as e:
        print(f'\n{e!r}')



    print ('\n ----------- Exceptions Module is Done >>>> ')