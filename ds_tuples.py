#===========================================================================
#                           Tuple Module
#===========================================================================
"""
# Demonstrates accessing the builtin Tuple type (container)
# Tuple is immutable
# support the following protocols: Container, Size, Iterable, Sequence
#
# Author: Shuky Persky
#
"""

#---------------------------------------------------------------------------------
# tuple obj APIs:
# https://www.w3schools.com/python/python_tuples.asp
# https://www.tutorialspoint.com/python/python_tuples.htm
#---------------------------------------------------------------------------------

from math import *

#================================================================================
# Few ways to show a tuple
def tuple_show(tpl):

    #Show tuple length and all eleements
    print('\n[Show-1] Tuple elements (Len: %d): ' % len(tpl), tpl)
    print('\n[Show-2] Tuple elems:', *tpl, sep=", ")
    print('\n[Show-3] Tuple elems:', tpl[0:])

    print('\n-------------------------')

    #for loop on tuple elements
    print('\n Looping thru the tuple elements (for loop using range)\n')
    for i in range(len(tpl)):
        print(tpl[i], ',')

    print('\n Looping thru the tuple elements (for loop using kind-of-iterator)\n')
    for elem in tpl:
        print(elem, ',')

    print('\n Looping thru the tuple elements (for loop using enumerate)\n')
    for elem_info in enumerate(tpl):
        print(elem_info, ',')
        print(f'elem_info: indx={elem_info[0]}, data={elem_info[1]}')

    print ('\n Looping thru the tuple elements (for loop using enumerate & unpacking)\n')
    for i, d in enumerate(tpl):
        print(f'elem_info: indx={i}, data={d}')

    #Tuple of tuples
    mtrx = ((1, 3), (-9, 33), (111, -88), (62, 44), (-12, 56))
    for elem in mtrx:
        for subelem in elem:
            print(subelem, ',')
        print('\n**\n')

    for i in range(0, len(mtrx)):
        for j in range(0,len(mtrx[i])):
            print(mtrx[i][j])
        print('\n**\n')


#================================================================================
#Accessing to a single or subrange of tuple elements
def tuple_elems_access(tpl):

    #access tuple element
    idx = 2
    print("\n[Show-4] Accessing Tuple\'s %d element: %d of type %s" %( idx, tpl[idx], type(tpl[idx])))

    idx = -1
    print("\n[Show-5] Accessing last (-1) tuple\'s element: %d of type %s" %( tpl[idx], type(tpl[idx])))

    print('\n Slicing - positive index')
    _from = 2
    _to = 5
    print("\n[Show-6] Accessing range of tuple\'s element: [%d .. %d]" % (_from, _to), tpl[_from:_to])
    print("\n[Show-7] Accessing range of tuple\'s element: [%d:]" % (_from), tpl[_from:])
    print("\n[Show-8] Accessing range of tuple\'s element: [:%d]" % (_to), tpl[:_to])

    print('\n Slicing - negative index')
    _from = -2
    _to = 3
    _step = -1
    print("\n[Show-6] Accessing range of tuple\'s element: [%d .. %d]" % (_from, _to), tpl[_from:_to:_step])


#================================================================================
#just checking if elem is part of the list
def tuple_elem_in_tuple(tpl):

    #Checking if an element exist in the list
    val = 5
    msg = '' # though redundant
    if val in tpl:
        msg = 'found'
    else:
        msg = 'NOT found'
    print('val:%d %s in tuple' % (val, msg), tpl)

    val = 11
    msg = ''    # though redundant
    if val in tpl:
        msg = 'found'
    else:
        msg = 'NOT found'
    print ('val:%d %s in tuple' % (val, msg), tpl)


#================================================================================
#show how to serach for an element in a list
def tuple_elem_search_count(tpl):

    #find how many times a value in tuple
    val = 3 #appears twice in th elist
    print('\n Number of times %d appears in ' % (val), tpl, ' is %d' % (tpl.count(val)))

    #find how many times a value in tuple
    val = 933  # does NOT appears in th elist
    print('\n Number of times %d appears in ' % (val), tpl, ' is %d' % (tpl.count(val)))

    #-----------------------

    #Search an eleem known to be in the list
    val = 3 #appears twice in th elist
    _from = 0
    _to = -1
    try:
        idx = tpl.index(val, _from, _to)

    except Exception as e:
        idx = -1

    if (idx != -1):   #found
        print('\n %d found in tuple at position %d' % (val, idx))
    else:           #not found
        print('\n %d NOT found in tuple ' % (val))


    #Search an eleem known to not be part of the list
    val = 933  # does NOT appears in th elist
    _from = 0
    _to = -1
    try:
        idx = tpl.index (val, _from, _to)

    except Exception as e:
        idx = -1

    if (idx != -1):  # found
        print ('\n %d found in tuple at position %d' % (val, idx))
    else:  # not found
        print ('\n %d NOT found in tuple ' % (val))


#================================================================================
# Clear and delete a list
def tuple_delete(tpl):

    # create a copy of tpl
    print('\n Create a tuple ')
    tuple_copy = tuple(tpl)

    #deleting the tuple
    print('\n Deleting the tuple ')
    del tuple_copy


#================================================================================
# Joining 2 lists
def tuples_join (tpl):

    tpl2 = tuple(tpl)  # create a tuple
    tpl3 = tpl + tpl2
    print ('\nThe result of joining by adding ', tpl2, ' to end of ', tpl, ' is ', tpl3)

    #tpl4 = tpl.copy();     ????
    #tpl4 += tpl2
    #print ('\nThe result of joining by adding ', tpl2, ' to end of ', tpl, ' is ', tpl4)

    # tuples can be duplicated few times by multiplication
    mul_tpl = tpl * 4  #multiply 4 times
    print ('\nThe result of joining by multiply ', tpl, ' 4 times is ', mul_tpl)


#================================================================================
def minmax(tpl):
    """Finds and returnd the Max and the Min of the input tuple
    :arg: tpl(Tuple)
    :return: (Tuple) min, max
    """

    #if emply, return
    if (len(tpl) == 0):
        return None, None

    # init
    min = max = tpl[0]

    #traverse thru, find min/max
    for elem in tpl:
        if (elem < min):
            min = elem
            continue

        if (elem > max):
            max = elem

    #advise caller
    return (min, max)


#================================================================================
def tuples_unpack(tpl):
    """Unpacks tuple into scalars
    :arg: None
    :return: None
    """

    min, max = minmax(tpl)      # returned tuple is unpacked
    print('\n min=%d, max=%d' % (min, max))

    #unpacking
    a, b, c, d, e, f = tuple (range (100, 123, 4))

    #swap
    min, max = max, min
    print('\n After swap: min=%d, max=%d' % (min, max))


#================================================================================
def tuples_iterator(tpl):
    '''Shows how to implement list iterator

    :arg        tpl(tuple)
                    just data

    :return:    none

    :raises     none
    '''

    #create iiterator
    iterator = iter(tpl)

    while (True):
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration as SI_e:
            print(f'=> {SI_e!r})')
            break

    print('\n We are done with iterator traverse')


#================================================================================
#module entry point function
def ds_tuples_mdl():

    '''
    The Tuple is an ordered collection of immutable objects.
    tuple allows duplicate elements. Elements can be of different types
    '''

    print ('\n\n ======== Tuples Example Module is Running ')

    #init
    tpl = (6, 2, 3, 6, 8, 5, 9, 4, 3, 12, 17, 24, -12, 56, -10, 13)
    tpl_elems_diff_types = (6, 2, 3, 6, 8, 9, 4, 3, 'string')
    tuple_of_one_elem = (4, )

    print('\n-------------------------')

    #show the tuple
    tuple_show(tpl)

    print('\n-------------------------')

    tuple_elems_access(tpl)

    print('\n-------------------------')

    tuple_elem_in_tuple(tpl)

    print('\n-------------------------')

    tuple_elem_search_count(tpl)

    print('\n-------------------------')

    tuple_delete(tpl)

    print('\n-------------------------')

    tuples_join(tpl)

    print('\n-------------------------')

    tuples_unpack(tpl)

    print('\n-------------------------')

    tuples_iterator (tpl)


    print ('\n ----------- Tuples Module is Done >>>> ')
