#===========================================================================
#                           Basic Module
#===========================================================================
"""
# deals with builtin types: scalar & strings
#
# Author: Shuky Persky
#
"""


#===========================================================================
#module entry point function
def basics_mdl():

    print('\n\n ======== Basics Module is Running ')

    #init
    intVar = 12
    floatVar = 13.22
    strVar = 'We are studying Python'
    boolVar = True #or False

    print("hello")

    # full concatenation
    print('Hello'+'World')

    # concatenation with blank
    print('Hello', 'World')

    print('My age is', 32)          # works
    #print('My age is', 32)         # won\t work. Can't add int to string
                                    # requires implicit conversion

    # Using single quote
    print('It\'s the 2nd time')     #using Escape
    print("It's the 2nd time")      #using double quote
    print('He said "Hi"')           #using single quote
    print('c:\\path\\filename')     #escape backslash of windows based path

    # print variables
    print(intVar)
    print(floatVar)
    print(strVar)
    print(boolVar)

    #swap
    a = 7
    b = 12
    print('\n Before swap: a=%d, b=%d' % (a, b))

    a, b = b, a
    print('\n After swap: a=%d, b=%d' % (a, b))

    print('\n ----------- Basics Module is Done >>>> ')

