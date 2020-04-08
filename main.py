#===========================================================================
#                          MAIN - application entry point
#===========================================================================

"""
# IMPORTANT
# - In Python everything is an object - even so is the module and a function
# - you can find the objects of a another objects by dir(object)
#   e.g.        import module
#               dir(module)
#               help(module)
#               help(module.object)     i/e/ object can be functions, variable
#
#   example (referring THIS modile - main.py)
#   go to Python console and hit
#       >>> import main
#       >>> dir(main)
#
#       The respoonse:
#       ['BASICS_MDL', 'CLASS_XMPL_MDL', 'DS_DICTS_MDL', 'DS_LISTS_MDL', 'DS_SETS_MDL', 'DS_TUPLES_M ....
#       ... '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__'
#       ... 'getopt', 'ifs_mdl', 'importer_mdl', 'loops_mdl', 'main', 'scope_mdl', 'show_menu', 'sys']
#
#   We can
#       help(main), or
#       help(main.__name__)
#           and get much information about this module (incl. THIS text as well)
#
#       main.main.__name_
#       main.main.__doc_
#       help(main.main)         whicj will show main.main.__doc_
#
#
# Author: Shuky Persky
#
"""

#imports
#---- system level ----
import sys
import getopt

#---- appl. level ----
from basics import basics_mdl
from loops import loops_mdl
from ifs import ifs_mdl
from funcs import funcs_mdl
from var_scope import scope_mdl
from files import files_mdl
from class_xmpl import class_xmpl_mdl
from importer import importer_mdl
from ds_lists import ds_lists_mdl
from ds_tuples import ds_tuples_mdl
from ds_dicts import ds_dicts_mdl
from ds_sets import ds_sets_mdl
from eql_id import equality_identity_mdl
from date_time import date_time_mdl
from strings import strings_mdl
from exceptions import exceptions_mdl



#--- modules list ---
BASICS_MDL          = 1
IFS_MDL             = 2
LOOPS_MDL           = 3
FUNCS_MDL           = 4
SCOPE_MDL           = 5
FILES_MDL           = 6
CLASS_XMPL_MDL      = 7
IMPORTER_MDL        = 8
DS_LISTS_MDL        = 9
DS_TUPLES_MDL       = 10
DS_DICTS_MDL        = 11
DS_SETS_MDL         = 12
EQL_ID_MDL          = 13
DT_TM_MDL           = 14
STRINGS_MDL         = 15
EXCEPTIONS_MDL      = 16


#globals
gMenu = {  # menu options
    BASICS_MDL: basics_mdl,
    IFS_MDL         : ifs_mdl,
    LOOPS_MDL       : loops_mdl,
    FUNCS_MDL       : funcs_mdl,
    SCOPE_MDL       : scope_mdl,
    FILES_MDL       : files_mdl,
    CLASS_XMPL_MDL  : class_xmpl_mdl,
    IMPORTER_MDL    : importer_mdl,
    DS_LISTS_MDL    : ds_lists_mdl,
    DS_TUPLES_MDL   : ds_tuples_mdl,
    DS_DICTS_MDL    : ds_dicts_mdl,
    DS_SETS_MDL     : ds_sets_mdl,
    EQL_ID_MDL      : equality_identity_mdl,
    DT_TM_MDL       : date_time_mdl,
    STRINGS_MDL     : strings_mdl,
    EXCEPTIONS_MDL  : exceptions_mdl,
}


#==================================================================================
def show_menu():
    '''
    presents the main appl. menu
    :return: None
    '''
    print ('\n\n Python Language Elements \n========================= \n')
    print('{mdl:-02d}. Basics               '.format(mdl=BASICS_MDL))
    print('{mdl:-02d}. IFs control          '.format(mdl=IFS_MDL))
    print('{mdl:-02d}. Loops                '.format(mdl=LOOPS_MDL))
    print('{mdl:-02d}. Functions            '.format(mdl=FUNCS_MDL))
    print('{mdl:-02d}. Var scope            '.format(mdl=SCOPE_MDL))
    print('{mdl:-02d}. Files                '.format(mdl=FILES_MDL))
    print('{mdl:-02d}. Class example        '.format(mdl=CLASS_XMPL_MDL))
    print('{mdl:-02d}. Importer             '.format(mdl=IMPORTER_MDL))
    print('{mdl:-02d}. Lists                '.format(mdl=DS_LISTS_MDL))
    print('{mdl:-02d}. Tuples               '.format(mdl=DS_TUPLES_MDL))
    print('{mdl:-02d}. Dictionaries         '.format(mdl=DS_DICTS_MDL))
    print('{mdl:-02d}. Lists                '.format(mdl=DS_SETS_MDL))
    print('{mdl:-02d}. Equality & Identity  '.format(mdl=EQL_ID_MDL))
    print('{mdl:-02d}. Date/Time            '.format(mdl=DT_TM_MDL))
    print('{mdl:-02d}. Strings              '.format(mdl=STRINGS_MDL))
    print('{mdl:-02d}. Exceptions           '.format(mdl=EXCEPTIONS_MDL))
    print('#. Otherwise ... exit ')


#==================================================================================
#main function of project
def main():
    """ This the main function.
    multiple line comment
    is very good sometimes
    """

    #show the (entry point scripr) script pathname
    print('\nRunning %s' % sys.argv[0])

    # command line arguments parse
    argv = sys.argv[1:]
    sum = 0

    try:
        # Define the getopt parameters
        opts, args = getopt.getopt (argv, 'a:b:', ['foperand', 'soperand'])
        # Check if the options' length is 2 (can be enhanced)
        if len (opts) == 0 and len (opts) > 2:
            print ('usage: add.py -a <first_operand> -b <second_operand>')
        else:
            # Iterate the options and get the corresponding values
            for opt, arg in opts:
                sum += int (arg)
            print ('Sum is {}'.format (sum))

    except getopt.GetoptError:
        # Print something useful
        print ('usage: add.py -a <first_operand> -b <second_operand>')
        sys.exit (2)


    #init
    exit = False    #main loop control

    #loop until exhausted
    while(not exit):

        #present menu to user
        show_menu()

        #get user input, verify that the input is numeric
        #if option is not numeric - advise and present menu
        try:
            option = int(input('\nPlese select an option: '))
        except:
            print('\ninput MUST be numeric')
            continue;

        #assure that input is numeric
        #if (isinstance(option, int)):
        #if (type(option) is int)
        # if (type(option) == int)
        #if (type(option) != int):

        #get the selection's associated function
        func = gMenu.get(option, "Exit")

        #if option is not supported by the menu - quit
        if (func  == "Exit"):
            exit = True;
            print("\nMenu Invalid option ... Quit...")
            continue;

        #execute function & handle exceptions
        try:
            func ()

        except TypeError as T_e:
            msg = "Type Error: {}".format(str(T_e))
            exit = True;

        except ValueError as V_e:
            msg = "Value Error: {}".format(str(V_e))
            exit = True;

        except Exception as E_e:
            msg = "Exception: {}".format(str(E_e))
            exit = True;

        except:
            msg  = "General Exception"
            exit = True;

        finally:
            if (exit == True):
                print("Error Occured ... %s" % msg)


#==================================================================================
# 'entry point' whe invoked from command line
if __name__ == '__main__':
    main()