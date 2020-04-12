#===========================================================================
#                           Package Module
#===========================================================================

"""
#Shows how to import a package and use its services.
#
# Author: Shuky Persky
#
"""

# import calc package
from calc import *
# import subpackage subCalc
from calc.subcalc import *


#===========================================================================
def pckg_mdl():
    '''package usage.

    Args-name   None
    :return(    None
    '''

    print ('\n\n ======== Package Module is Running ')

    # we'll be using a package named calc and its subpackega called
    #
    # we firsy verify whether the package folder is under a path which is included in the sys.path
    #
    # assume that 'folder' is a path which is included in sys.path, and 'pckg' is the package's folder
    # then the following path must exist and be valid: folder/package/<package files>
    #
    # import sys
    #
    # if folder NOT in sys.path:
    #   sys.path.append('folder')
    #
    # import pckg       # or from pckg import  *
    #
    # pckg.func ()      # call an exposed service of the package


    #call a function that is part of the high level package which
    #accesses a calss and its method which is part of a lower-level package
    print('\n Calling a service function from level-0 package: calc')
    calc_test_func()

    #----------- Package: Calc -----------

    #The below service can't be called
    # # as it isn't exposed (by __all__)
    #Calc()

    #call a service
    calc_obj = Calc__()
    calc_obj.add(2, 3);         # => [Calc__]/Add'


    #----------- SubPackage: SubCalc -----------

    #call a service
    subcalc_obj = SubCalc()
    subcalc_obj.adder(22, 33)     # => [SubCalc]/Add


    #The below service can be called
    #as it isn't exposed (by __all__)
    #SubCalc__()


    print ('\n ----------- Package Module is Done >>>> ')



