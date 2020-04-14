#===========================================================================
#                           Decorator Module
#===========================================================================

"""
#Demonstrates how decorstor works: function, class, stacked
#
# Author: Shuky Persky
#
"""

import functools

#===========================================================================
class DecoratorClass:
    '''Class Decorator.
    '''
    def __init__(self):
        pass

    def __call__(self, original_func):
        '''Wrapper method.
        '''
        @functools.wraps(original_func)
        def wrapper(*args, **kwargs):
            print ('\n wrapprt [Class/__call__] running just before calling the wrapped function {}'.format(original_func.__name__))
            x = original_func(*args, **kwargs)      #calling the decorated function
            return ascii(x)

        return wrapper


decorater_class = DecoratorClass()      # create an instance

#===========================================================================
def decorator_func(original_func):
    '''Function Decorator.
    '''
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        '''Wrapper function.
        '''
        print ('\n wrapper function running just before calling the wrapped function {}'.format(original_func.__name__))
        x = original_func(*args, **kwargs)      #calling the decorated function
        return ascii(x)

    return wrapper


#===========================================================================
# Using Function Decorators
@decorator_func
def get_name_title(name, title):
    '''Decorated function
    '''
    return '{}, {}'.format(name, title)


@decorator_func
def display_some_text():
    '''Decorated function
    '''
    return 'KUKU is a nice person'


#===========================================================================
# Using Function Decorators
@decorater_class
def get_name_title__(name, title):
    '''Decorated function
    '''
    return '{}, {}'.format(name, title)


@decorater_class
def display_some_text__():
    '''Decorated function
    '''
    return 'KUKU is a nice person'



#===========================================================================
# Using Stacked Decorators
@decorator_func
@decorater_class
def __get_name_title__(name, title):
    '''Decorated function
    '''
    return '{}, {}'.format(name, title)


@decorator_func
@decorater_class
def __display_some_text__():
    '''Decorated function
    '''
    return 'KUKU is a nice person'



#===========================================================================
#module entry point function
def decorator_mdl():
    '''
    Shows how a Decorator wraps an existing function
    '''

    print ('\n\n ======== Closure Module is Running ')


    #-----------------------
    # Function Decorator
    #-----------------------
    print ('\n\n\n Function Decorator\n------------------------')

    text =  get_name_title('James', 'VP R&D')
    print('\n After calling the decorated func: {}'.format(text))

    print ('\n')
    text =  display_some_text()
    print('\n After calling the decorated func: {}'.format(text))

    # -----------------------
    # Class Decorator
    # -----------------------
    print ('\n\n\n Class Decorator\n------------------------')

    text =  get_name_title__('James', 'VP R&D')
    print('\n After calling the decorated func: {}'.format(text))

    print ('\n')
    text =  display_some_text__()
    print('\n After calling the decorated func: {}'.format(text))


    # -----------------------
    # Stacked Decorator
    # -----------------------
    print ('\n\n\n Stacked Decorator \n------------------------')

    text =  __get_name_title__('James', 'VP R&D')
    print('\n After calling the decorated func: {}'.format(text))

    print ('\n')
    text =  __display_some_text__()
    print('\n After calling the decorated func: {}'.format(text))




    print ('\n ----------- Closure Module is Done >>>> ')



