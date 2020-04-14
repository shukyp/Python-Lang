#===========================================================================
#                           Closure Module
#===========================================================================

"""
#Demonstrates how closure works
#
# Author: Shuky Persky
#
"""

def multiply_by(factor):        # closure
    '''Functiion Factory.
    '''
    def multiply_by_factor(val):
        return(val*factor)      # local function uses local data: factor

    return multiply_by_factor   # return local function


#===========================================================================
#module entry point function
def closure_mdl():
    '''
    Shows how a loal function can be called since its closure is maintained
    '''

    print ('\n\n ======== Closure Module is Running ')

    mul_by_11 = multiply_by(11)                                             #call the outer func to create a closure

    print(mul_by_11.__closure__)                                            #show the closure exists. this is a python object

    print('\n Calling mul_by_11(7): {}'.format(mul_by_11(7)))               #call the local function to mul: 7 * 11
    print('\n Calling mul_by_11(9): {}'.format(mul_by_11(9)))               #call the local function to mul: 9 * 11


    print ('\n ----------- Closure Module is Done >>>> ')