
#---------------------------------------------------------------------------------
# list obj APIs:
# https://www.w3schools.com/python/python_lists.asp
# https://www.tutorialspoint.com/python/python_lists.htm
#---------------------------------------------------------------------------------


#================================================================================
# Few ways to show a list
def list_show(lst):

    #Show list length and all eleements
    print('\n[Show-1] List elements (Len: %d): ' % len(lst), lst)
    print('\n[Show-2] List elems:', *lst, sep=", ")
    print('\n[Show-3] List elems:', lst[0:])

    print('\n-------------------------')

    #for loop on list elements
    print('\n Looping thru the list elements (for loop)\n')
    for elem in lst:
        print(elem, ',')


#================================================================================
#Accessing to a single or subrange of list elements
def list_elems_access(lst):

    #access list element
    idx = 2
    print("\n[Show-4] Accessing list\'s %d element: %d of type %s" %( idx, lst[idx], type(lst[idx])))

    idx = -1
    print("\n[Show-5] Accessing last (-1) list\'s element: %d of type %s" %( lst[idx], type(lst[idx])))

    _from = 2
    _to = 5
    print("\n[Show-6] Accessing range of list\'s element: [%d .. %d]" % (_from, _to), lst[_from:_to])
    print("\n[Show-7] Accessing range of list\'s element: [%d:]" % (_from), lst[_from:])
    print("\n[Show-8] Accessing range of list\'s element: [:%d]" % (_to), lst[:_to])


#================================================================================
#just checking if elem is part of the list
def list_elem_in_list(lst):

    #Checking if an element exist in the list
    val = 5
    msg = ''    # though redundant
    if val in lst:
        msg = 'found'
    else:
        msg = 'NOT found'
    print('val:%d %s in list' % (val, msg), lst)

    val = 11
    msg = ''    # though redundant
    if val in lst:
        msg = 'found'
    else:
        msg = 'NOT found'
    print ('val:%d %s in list' % (val, msg), lst)


#================================================================================
#show how to serach for an element in a list
def list_elem_search_count(lst):

    #find how many times a value in list
    val = 3 #appears twice in th elist
    print('\n Number of times %d appears in ' % (val), lst, ' is %d' % (lst.count(val)))

    #find how many times a value in list
    val = 933  # does NOT appears in th elist
    print('\n Number of times %d appears in ' % (val), lst, ' is %d' % (lst.count(val)))

    #-----------------------

    #Search an eleem known to be in the list
    val = 3 #appears twice in th elist
    _from = 0
    _to = -1
    try:
        idx = lst.index(val, _from, _to)

    except Exception as e:
        idx = -1

    if (idx != -1):   #found
        print('\n %d found in list at position %d' % (val, idx))
    else:           #not found
        print('\n %d NOT found in list ' % (val))


    #Search an eleem known to not be part of the list
    val = 933  # does NOT appears in th elist
    _from = 0
    _to = -1
    try:
        idx = lst.index (val, _from, _to)

    except Exception as e:
        idx = -1

    if (idx != -1):  # found
        print ('\n %d found in list at position %d' % (val, idx))
    else:  # not found
        print ('\n %d NOT found in list ' % (val))


# ================================================================================
def list_elem_value_set(lst):

    #change element value
    idx = 4
    print('\nChnaging value of List element (position: %d): ' % lst[idx], lst)
    lst[idx] += 3
    print('\nChnaged value of List element (position: %d): ' % lst[idx], lst)


# ================================================================================
#Reversing list elements
def list_elems_reverse(lst):

    #reverse all list elements
    print('\nOriginal List elements (Len: %d): ' % len(lst), lst)
    reversed_lst = lst[-1::-1]
    print('\nReversed List elements (Len: %d): ' % len(reversed_lst), reversed_lst)
    lst.reverse();
    print ('\nReversed List elements (Len: %d): ' % len (lst), lst)
    lst.reverse (); # reverse back


#================================================================================
# add an element to list using Append or Insert
def list_elem_add(lst):

    #Appending element to list
    val = 133
    print('\n Appending element %d' %(val), lst)
    lst.append(val)
    print('\n After appending element %d' %(val), lst)

    print('\n-------------------------')

    #Insert an element to list
    val = 111
    pos = 3
    print('\n Adding element %d in position %d' %(val, pos), lst)
    lst.insert(pos, val)
    print('\n After adding element %d in position %d' %(val, pos), lst)


#================================================================================
# Dismiss an element of the list: remove, pop, del
def list_elem_dismiss(lst):

    # Remove an element from list
    # remove (by content value)- removes element from list
    val = 111
    if (val in lst):
        print('\n Removing element %d' %(val), lst)
        lst.remove(val)
        print('\n After removing element %d ' %(val), lst)

    print('\n-------------------------')

    # pop - removes by index or the first index if no index is given
    # negative index support as well
    idx = 2
    print('\n Popping valid position %d' %(idx), lst)
    poped = lst.pop(idx)
    print('\n After popping element %d from position %d' %(poped, idx), lst)

    print ('\n Popping 1st element, at index 0', lst)
    poped = lst.pop ()
    print ('\n After popping the first element %d from position %d' % (poped, 0), lst)

    try:
        idx = 55  #deliberatly out of range
        print('\n Popping invalid index %d (out-of-range)' %(idx), lst)
        lst.pop(idx)
        print('\n After popping element of index %d in position %d' %(idx), lst)

    except Exception as e:
        print('\n Error with popping: %s' % (str(e)))


#================================================================================
# delete a list element
# delete (differs from pop by that it doesn't return the popped element
# negative index support as well
def list_elem_del(lst):

    #valid position
    idx = 2
    print('\n Deleting valid position %d' %(idx), lst)
    del lst[idx]
    print('\n After deleting element of position %d' %(idx), lst)

    #Invalid position
    try:
        idx = 55  #deliberatly out of range
        print('\n Deleting invalid index %d (out-of-range)' %(idx), lst)
        del lst[idx]
        print('\n After deleting element of position %d' %(idx), lst)

    except Exception as e:
        print('\n Error with deleting %s' % (str(e)))


#================================================================================
# create a copy of a list
def list_copy(lst):

    #copy  a list
    # should be noticed that new_list = existing list
    # just creates a new reference to the existing list
    # any change using one of the references is seen thru the other
    # as they point the same object
    print('\n Copyin the list', lst)
    list_copy_1 = lst.copy()
    print('\n the copy (by lst.copy()) of list', lst, 'is ', list_copy_1)

    list_copy_2 = list(lst) # makes a list
    print('\n the copy (by list(lst)) of list', lst, 'is ', list_copy_2)


#================================================================================
# sort a list
def list_sort(lst):

    # creat e2 copies of lst
    list_copy_1 = lst.copy()
    list_copy_2 = lst.copy()

    #sort a list
    # list.sort (reverse=True | False, key=myFunc)
    print('\n Soring the list:', list_copy_1)
    list_copy_1.sort()  # (reverse=False) defalt
    print ('\n The list after being sorted:', list_copy_1)

    print('\n Soring reverse the list:', list_copy_2)
    list_copy_2.sort(reverse=True)
    print ('\n The list after being sorted:', list_copy_2)


#================================================================================
# Clear and delete a list
def list_clear_delete(lst):

    # create 2 copies of lst
    print('\n Create 2 lists ')
    list_copy_1 = lst.copy()
    list_copy_2 = lst.copy()

    #clear a list - leaves the list empty with no elements
    print('\n Clearing the list:', list_copy_1)
    list_copy_1.clear()
    print('\n The list after being cleared:', list_copy_1)

    #deleting a list
    print('\n Deleting the 2 copy lists ')
    del list_copy_1
    del list_copy_2


#================================================================================
# Joining 2 lists
def lists_join (lst):

    lst2 = lst.copy ()  # create a copy
    lst2.reverse ()  # reverse the copy
    lst3 = lst + lst2
    print ('\nThe result of joining by adding ', lst2, ' to end of ', lst, ' is ', lst3)

    # join by extend
    lst4 = lst.copy ()
    lst4.extend (lst2)
    print ('\nThe result of joining by extending ', lst, ' list by ', lst2, ' is ', lst4)

    # join by append - the appended list becomes a single element of type list
    # as last element of the list it is appended to, jsut like appending a single value
    lst5 = lst.copy ()
    lst5.append (lst2)
    print ('\nThe result of joining by appending ', lst2, ' list to', lst, ' is ', lst5)


#================================================================================
#module entry point function
def ds_lists_mdl():
    '''
    The List is an ordered collection of mutable objects.
    List allows duplicate elements. Elements can be of different types
    '''

    print ('\n\n ======== Lists Example Module is Running ')

    #init
    lst = [6, 2, 3, 6, 8, 5, 9, 4, 3, 12, 17, 24, -12, 56, -10, 13]
    lst_elems_diff_types = [6, 2, 3, 6, 8, 9, 4, 3, 'string']
    empty_list = []

    print('\n-------------------------')

    #show the list
    list_show(lst)

    print('\n-------------------------')

    list_elems_access(lst)

    print('\n-------------------------')

    list_elem_in_list(lst)

    print('\n-------------------------')

    list_elem_search_count(lst)

    print('\n-------------------------')

    list_elem_value_set(lst)

    print('\n-------------------------')

    list_elems_reverse(lst)

    print('\n-------------------------')

    list_elem_add(lst)

    print('\n-------------------------')

    list_elem_dismiss(lst)

    print('\n-------------------------')

    list_elem_del(lst)

    print('\n-------------------------')

    list_copy(lst)

    print('\n-------------------------')

    list_sort(lst)

    print('\n-------------------------')

    list_clear_delete(lst)

    print('\n-------------------------')

    lists_join(lst)

    print ('\n ----------- Lists Module is Done >>>> ')
