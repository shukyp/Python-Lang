#===========================================================================
#                           Equality / Identitiy Module
#===========================================================================
"""
# Expains and Demonstrates the topics of value equality and Identification equality
#
# Author: Shuky Persky
#
"""


#==================================================================================
#equality of floats
def equality_identity_of_ints():

    # the 2 integers are not equal with data
    int01 = 4
    int02 = 5

    print('\nThe values of the 2 integers: int01= %d, int02= %d' % (int01, int02))

    print('\n Are they equal? (int01 == int02) %s', str((int01 == int02)))              # data equality
    print('\n Are they identical? id(int01) == id(int02)', (id(int01) == id(int02)))    # identity checking
    print('\n Are they identical? (int01 is int02)', (int01 is int02))                  # identity checking

    # the 2 integers are equal with data
    print('\n\n Now set int02 to be %d (as int01)\n' % int01)
    int02 = 4

    print('\nThe values of the 2 integers: int01= %d, int02= %d' % (int01, int02))

    print('\n Are they equal? (int01 == int02)', (int01 == int02))                      # compare data
    print('\n Are they identical? id(int01) == id(int02)', (id(int01) == id(int02)))    # identity checking
    print('\n Are they identical? (int01 is int02)', (int01 is int02))                  # identity checking


#==================================================================================
#equality of integers
def equality_identity_of_floats():

    # the 2 floats are not equal with data
    flt01 = 4.56723
    flt02 = 5.98567

    print('\nThe values of 2 the floats: flt01= %f, flt02= %f' % (flt01, flt02))

    print('\n Are they equal? (flt01 == flt02)', (flt01 == flt02))                      # data equality
    print('\n Are they identical? id(flt01) == id(flt02)', (id(flt01) == id(flt02)))    # identity checking
    print('\n Are they identical? (flt01 is flt02)', (flt01 is flt02))                  # identity checking

    # the 2 floats are equal with data
    print('\n\n Now set flt02 to be %f (as flt01)\n' % flt01)
    flt02 = 4.56723

    print('\nThe values of the 2 floats: flt01= %f, flt02= %f' % (flt01, flt02))

    print('\n Are they equal? (flt01 == flt02)', (flt01 == flt02))                      # compare data
    print('\n Are they identical? id(flt01) == id(flt02)', (id(flt01) == id(flt02)))    # identity checking
    print('\n Are they identical? (flt01 is flt02)', (flt01 is flt02))                  # identity checking


#==================================================================================
#equality of integers
def equality_identity_of_strings():

    # the 2 strings are not equal with data
    str01 = "Aron is walking along the road"
    str02 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    print('\nThe values of the 2 strings: str01= "%s", str02= "%s"' % (str01, str02))

    print('\n Are they equal? (str01 == str02)', (str01 == str02))                      # data equality
    print('\n Are they identical? id(str01) == id(str02)', (id(str01) == id(str02)))    # identity checking
    print ('\n Are they identical? (str01 is str02)', (str01 is str02))                 # identity checking

    # the 2 strings are equal with data
    print('\n\n Now set str02 to be "%s" (as str01)\n' % str01)
    str02 = "Aron is walking along the road"

    print('\nThe values of the 2 strings: str01= "%s", str02= "%s"' % (str01, str02))

    print('\n Are they equal? (str01 == str02)', (str01 == str02))                      # compare data
    print('\n Are they identical? id(str01) == id(str02)', (id(str01) == id(str02)))    # identity checking
    print('\n Are they identical? (str01 is str02)', (str01 is str02))                  # identity checking


global_int_var = 22

#-------------------------------------------------
#reports identity of argument and a global variable
def func_01(val):
    global int_var;

    print('\n ')
    print('Passed val is int_var? %s' % str(val is global_int_var))

#-------------------------------------------------
#just returns what it gets
#purpose is to support its caller to find identity between
#what is passed to function and what is recieved from function
def func_02(val):
    return (val)


#==================================================================================
#module entry point function
def equality_identity_mdl():

    global global_int_var
    local_int_var = 8


    print ('\n\n ======== Equality Module is Running ')

    equality_identity_of_ints()

    print('\n-------------------------------')

    equality_identity_of_floats ()

    print ('\n-------------------------------')

    equality_identity_of_strings ()

    print ('\n-------------------------------')


    print('\n ----------------- ATTENTION : Containers ----------------------')
    print('\n Identical containers are equal by value but are not identical as with non-contaiber objects')
    print('\n Identical containers are equal by value but are not identical as with non-contaiber objects')
    print('\n e.g. ')
    print('\n   Lists x= [1, 2, 3], y= [1, 2, 3]. (x == y):True,  (x is y):False')
    print('\n   Tuple x= (1, 2, 3}, y= (1, 2, 3}. (x == y):True,  (x is y):False')


    print('\n ----------------- ATTENTION : Functions ----------------------')
    print('\n Function arguments are passed by reference, so is the return value ')

    print('Passing int_var to function ')
    func_01(global_int_var)

    int_var = func_02 (local_int_var)
    print('\n Is passed arg equivalent to returned obj? %s' % str(int_var is local_int_var))


    print ('\n ----------- Equality Module is Done >>>> ')
