
#from calc.oldSubcalc.oldSubcalc  import *
from calc.oldSubcalc  import *

__all__ = ['Calc__', 'calc_test_func']


class Calc:

    def __init__(self):
        pass

    def add(self, a, b):
        print('\n[Calc]/Add')

    def sub(self, a, b):
        print('\n[Calc]/Sub')

    def mul(self, a, b):
        print('\n[Calc]/Mul')

    def div(self, a, b):
        print('\n[Calc]/Div')



class Calc__:

    def __init__(self):
        pass

    def add(self, a, b):
        print('\n[Calc__]/Add')

    def sub(self, a, b):
        print('\nCalc__]/Sub')

    def mul(self, a, b):
        print('\nCalc__]/Mul')

    def div(self, a, b):
        print('\nCalc__]/Div')


#=====================================================
def calc_test_func():
    '''High Package calls to subpackage service.'''

    print('\n From level-0 package: ''calc'', Functuin ''calc_test_func()'' ')

    #create object
    print('\n From level-0 package: ''calc'', Functuin ''calc_test_func()'' - Create object from class of level-1 package: OldSubCalc__')
    obj = OldSubCalc__()

    #call an instance method
    print('\n From level-0 package: ''calc'', Functuin ''calc_test_func()'' - Call an instance method of a class of level-1 package: OldSubCalc__')
    obj.oldAdder__(66, 8)

    #call __str__ method
    print('\n From level-0 package: ''calc'', Functuin ''calc_test_func()'' - Call an instance method __str__ of a class of level-1 package: OldSubCalc__')
    print(OldSubCalc__)

