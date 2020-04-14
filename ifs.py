#===========================================================================
#                           IFs Module
#===========================================================================
"""
# Demonstrates using 'if' flow control and refers the conditional expression
#
# Author: Shuky Persky
#
"""



#===========================================================================
def func_1():
    print('\nfunc is running --1--')

def func_2():
    print('\nfunc is running --2--')

def func_3():
    print('\nfunc is running --3--')

def func_4():
    print('\nfunc is running --4--')

def func_5():
    print('\nfunc is running --5--')


def func_6():
    print('\nfunc is running --6--')

#===========================================================================
option_vec = \
    {
        1: func_1,
        2: func_2,
        3: func_3,
        4: func_4,
        5: func_5,
        6: func_6
    }


#===========================================================================
def switch_like(ent):
    '''Implements a "switch" like operation
    '''

    func = option_vec.get(ent)      # fetch the right function

    if (func == None):              # if nothing found
        return 'Error'

    func()                          # execute
    return 'Ok'


#===========================================================================
def ifs_mdl():
    '''module entry point function.
    '''

    print ('\n\n ======== IFs Module is Running ')

    print ('\n\n If statement \n');
    x = 3
    y = 55
    z = 92

    # simple if
    if (x > y):
        print ("x:%d > y:%d" % (x, y))

    if (y > x):
        print ("y:%d > x:%d" % (y, x))

    # multiple if
    if (x < y < z):
        print ("x:%d < y:%d < z:%d" % (x, y, z))

    # if else (simple else)
    if (x > y):
        print ("[main] x:%d > y:%d" % (x, y))
    else:  # if the main if not fulfilled
        print ("[else] y:%d > x:%d" % (y, x))

    # if else (elif)
    if (x > y):
        print ("[main] x:%d > y:%d" % (x, y))
    elif (y > 50):  # elif if the main if not fulfilled
        print ("[elif] y:%d > 50" % (y))
    else:  # else if elif not fulfilled
        print ("[else follows elif]")

    # conditional expression
    immutable = True;
    obj = () if immutable else []
    type(obj)  #expected to list

    immutable = True;
    obj = () if immutable else []
    type(obj)  #expected to tuple

    #"switch" like
    switch_like (3)

    #lambda expression
    scientists = ['Marie Curie', 'Albert Einstein', 'Neilse Bohr', 'Isaac Newton', 'Dmitri Mendeleev', 'Alfred Wegener']

    sort1 = sorted(scientists, key=lambda name: name.split()[-1])
    print('\n sorted upwards by familiy name:', sort1)

    sort1_rvrs = sorted(scientists, key=lambda name: name.split()[-1], reverse=True)
    print('\n sorted downwards by familiy name:', sort1_rvrs)

    sort2 = sorted(scientists, key=lambda name: name.split()[0])
    print('\n sorted upwards by first name:', sort2)

    sort2_rvrs = sorted(scientists, key=lambda name: name.split()[0], reverse=True)
    print('\n sorted downwards by first name:', sort2_rvrs)


    print ('\n ----------- IFs Module is Done >>>> ')
