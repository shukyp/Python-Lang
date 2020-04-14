#===========================================================================
#                           Files Module
#===========================================================================
"""
# Demonstrates some topics that pertain to functions definitions and invocation
#
# Author: Shuky Persky
#
"""

#===========================================================================
# Regular function: variables with default values and others with no default values
# non-default value parameter must come before ALL default value parameter(s)
def func_example(font='Arial', bg_color='yellow', font_size = 14, font_color = 'red'):
    '''Regular function: variables with default values and others with no default values'''
    print('font:', font)
    print ('bg_color:', bg_color)
    print ('font_size:', font_size)
    print ('font_color:', font_color)


#===========================================================================
# function that accepts variable number of arguments
def func_multiple_args(*args):

    print ('\n\n')

    #arguments are passed as tuple
    print('\n args type:', type(args))
    print('\n args:', args)

    #access args - travers container's elements
    print('\n travers container''s elements')
    for arg in args:
        print ('\n arg: {}'.format(arg))

    #access args - travers container using iterator
    print('\n travers container''s uising iterator')
    iterator = iter (args)
    while (True):
        try:
            elem = next (iterator)
            print ('\narg: ', elem, ',')
        except StopIteration as SI_e:
            print ('\n... Done')
            break


#===========================================================================
# function that accepts variable number of arguments
def func_multiple_kwargs(**kwargs):

    print ('\n\n')

    #arguments are passed as tuple
    print('\n kwargs type:', type(kwargs))
    print('\n kwargs:', kwargs)

    #access args - travers container's elements
    print('\n travers container''s elements')
    for elem in kwargs.items():
        print ('\n {obj[0]} : {obj[1]}'.format(obj=elem))


    #access args - travers container's elements
    print('\n travers container''s elements')
    for key, value in kwargs.items():
        print ('\n {} : {}'.format(key, value))


    #access args - travers container using iterator
    print('\ntravers container''s uising iterator')
    iterator = iter (kwargs.items())
    while (True):
        try:
            elem = next(iterator)
            print ('\n {obj[0]} : {obj[1]}'.format(obj=elem))
        except StopIteration as SI_e:
            print ('\n... Done')
            break


#===========================================================================
def func_01(arg1, arg2, *arg3):
    print(arg1, arg2, arg3)


#===========================================================================
def func_02(arg1, arg2, **arg3):
    print(arg1, arg2, arg3)


#===========================================================================
#module entry point function
def funcs_mdl():

    print ('\n\n ======== Funcs Module is Running ')

    # init
    font = 'TMN'
    bg_color = 'white'
    font_size = 11
    font_color = 'black'

    # call func with arguments
    print ('\n\n default order, explicit values / no default values \n')
    func_example (font, bg_color, font_size, font_color);

    # call func with params:arguments pairs
    print ('\n\n free order, explicit values / no default values \n')
    func_example (bg_color='white',
                  font='TMN',
                  font_color='black',
                  font_size=11)

    # call func with partial set of arguments
    print ('\n\n default order, partiall explicit values / partial default values) \n')
    func_example ('TMN_new', 'white')

    #call a function with regular multiple arguments
    func_multiple_args(1, 2, 5, 5, 6, 99, -12)

    # call a function with keyword multiple arguments
    func_multiple_kwargs (first='xxx', second='yyyy', last='zzz')

    # interesting case
    t = (1, 2, 3, 4, 5)
    #func (t)       #error
    func_01 (*t)       #only this will work: output: 1 2 (3, 4, 5)

    # interesting case
    # notice to the signature: def func_02(arg1, arg2, **arg3):
    k0 = {'arg1':22, 'arg2':33, 'arg3':44, 'arg4':55, 'arg5':66, 'arg7':88}
    k1 = {'arg3':44, 'arg4':55, 'arg5':66, 'arg7':88}
    func_02(**k0)
    func_02(arg1 = 22, arg2 = 33, **k1)


    print ('\n ----------- Funcs Module is Done >>>> ')


