#===========================================================================
#                               Variable Scope
#===========================================================================

"""
# Demonstrates issues that pertain to variable scope
#
#   Scope in Python (LEGB rule)
#
#   Local       - inside current function
#   Eclosing    - inside enclosing function
#   Global      - At the top level of the module
#   Built-in    - part of the the special 'builtins' module
#
#   Thus:       - scopes are not defined by blocks (according identation)
#
# Author: Shuky Persky
#
"""

#global variable
xx = 7


#===========================================================================
#function that refers a global variable
# it shoul dbe noticed that
# (a) if a locally uninitialized variable is being read
#     python will look for it in the enclosing scope
# (b) if a loacl cariable is set it is initialized
#     if that variable is not declared of global scope it will be created locally
#     and will shadow the global variable for all further references (read & write)
#     if 'global' is used for that variable all references will access the variable
#     of the global space
def func_global():
    global xx   # referring to the global scope x

    print ('[func_global] global xx=', xx) # print global xx
    xx += 1                 # increment global xx
    print ('[func_global] global xx=',xx)  # print global xx


#===========================================================================
#function that refers a local variable
#that has the same shadows/name of global variable
def func_local():

    #print (xx)             #won't work since no local x declared/defined
    xx = 9                  #local local xx declared/defined
    print ('[func_local] global x=', xx) #will work


#===========================================================================
#module entry point function
def scope_mdl():

    print ('\n\n ======== SCOPE Module is Running ')

    print('\n\n Calling functions that refer global/local variables \n')
    print('\nGlobal xx=', xx)
    func_global()
    func_local()

    print ('\n ----------- SCOPE Module is Done >>>> ')
