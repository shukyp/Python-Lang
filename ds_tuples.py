


#---------------------------------------------------------------------------------
# tuple obj APIs:
# https://www.w3schools.com/python/python_tuples.asp
# https://www.tutorialspoint.com/python/python_tuples.htm
#---------------------------------------------------------------------------------


#================================================================================
# Few ways to show a tuple
def tuple_show(tpl):

    #Show tuple length and all eleements
    print('\n[Show-1] Tuple elements (Len: %d): ' % len(tpl), tpl)
    print('\n[Show-2] Tuple elems:', *tpl, sep=", ")
    print('\n[Show-3] Tuple elems:', tpl[0:])

    print('\n-------------------------')

    #for loop on tuple elements
    print('\n Looping thru the tuple elements (for loop)\n')
    for elem in tpl:
        print(elem, ',')


#================================================================================
#Accessing to a single or subrange of tuple elements
def tuple_elems_access(tpl):

    #access tuple element
    idx = 2
    print("\n[Show-4] Accessing Tuple\'s %d element: %d of type %s" %( idx, tpl[idx], type(tpl[idx])))

    idx = -1
    print("\n[Show-5] Accessing last (-1) tuple\'s element: %d of type %s" %( tpl[idx], type(tpl[idx])))

    _from = 2
    _to = 5
    print("\n[Show-6] Accessing range of tuple\'s element: [%d .. %d]" % (_from, _to), tpl[_from:_to])
    print("\n[Show-7] Accessing range of tuple\'s element: [%d:]" % (_from), tpl[_from:])
    print("\n[Show-8] Accessing range of tuple\'s element: [:%d]" % (_to), tpl[:_to])


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

    print ('\n ----------- Tuples Module is Done >>>> ')
