#===========================================================================
#                           String Module
#===========================================================================
"""
# Demonstrates strings APIs
# Strings are immutable
#
# Author: Shuky Persky
#
"""


#===========================================================================
def strings_concat_split():
    '''
    Shows how strings are concatentaed/splitted.
    Args-name(type) na
    :return(type)   na
    '''
    #string objects concat using '+'
    s = 'aaa' + 'bbb' + 'ccc'
    print('\n aaa + bbb + ccc = %s' % s)

    #string objects concat using '+='
    s1 = s  #should be 'aaabbbccc"
    s1 += 'ddd' #yields 'aaabbbcccddd'

    #string class joint (more efficient than using '+')
    s = ''.join(['aaa', 'bbb', 'ccc'])      # s = 'aaabbbccc'

    #other usage
    s_join = ';'.join(['you', 'we', 'them', 'me', 'us'])    # 'you;we;them;me;us'
    print('\n joined: %s ' % s_join)

    #split
    s_split = s_join.split(';')                             # => ['you', 'we', 'them', 'me', 'us']
    print('\n splitted: %s ' % s_split)

    #partition
    print('\n Partion: ')
    "convolutional".partition('vol')                        # => ('con', 'vol', 'utional')


#===========================================================================
def string_format():
    '''Demos fprmatting a string.
    Args-name(type) na
    :return(type)   na
    '''

    #replacement fields are substitueed by the values of the format arguments
    #field names (e.g. {0}) are matched with the format positional args
    s1 = 'The age of {0} is {1}'.format('Adma', 31)

    #if format args are used only once, ordinals can be omitted
    s1 = 'The age of {} is {}'.format('Adma', 31)

    #field names can be used more than once
    '{0} celebrated {1} of age {2}. Then {0} went home'.format('Jack', 'Birthday', 28)

    #keywords can be used instead of ordinals as field names where they will match
    #the format keyword arguments
    'Coming {day} of {month} is {desc}'.format(day='Monday', month='March', desc='Holiday')

    #keyword fields if are objects can be accessed thru index, fields
    'Spatial Coordinates x={pos[0]}, y={pos[1]}, z={pos[2]}'.format(pos=(12.456, 88.001, 111.34))

    import math
    'Some Math conatants pi={ml.pi} e={ml.e}'.format(ml=math)   #default precision control
    'Some Math conatants pi={ml.pi:.4f} e={ml.e:.4f}'.format(ml=math)   #defined precision control



#===========================================================================
def f_strings():
    '''f-strings (PEP-498).
    Deals with embedding expressions into atrings
    Expressions are evaluated at runtime
    :arg: na
    :return: na
    '''

    #example
    s1 = f'eight times eleven = {11 * 8}'
    print ('\n', s1);
    print (''.join (['\n', s1]))

    import time as tm
    s2 = f'curr date/time: {tm.ctime()})'
    print ('\n', s2)

    import math
    s3 = f'Some Math conatants pi={math.pi:.5f} e={math.e:.7f}'  # default precision control
    print ('\n', s3)


#===========================================================================
def strings_mdl():
    '''
    string module entry point function
    '''

    print ('\n\n ======== String Module is Running ')

    #Shows strings concatention/splitting
    strings_concat_split()

    print('\n------------------------------')

    #string formatting
    string_format()

    print('\n------------------------------')

    #f-strings (PEP-498)
    f_strings()

    print ('\n ----------- String Module is Done >>>> ')