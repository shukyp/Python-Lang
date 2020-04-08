#===========================================================================
#                           Sets Module
#===========================================================================
"""
# Demonstrates accessing the builtin Set type (container)
# unordered collection of unique elements (members cann't repeat in a set)
# Sets are mutable
# Elements in set are immutable
# supports the following protocols: Container, Size, Iterable, Mutable Set.
#
# Author: Shuky Persky
#
"""

#---------------------------------------------------------------------------------
# tuple obj APIs:
# https://www.w3schools.com/python/python_sets.asp
# https://www.tutorialspoint.com/python/python_sets.htm
#---------------------------------------------------------------------------------


#================================================================================
#module entry point function
def ds_sets_mdl():

    print ('\n\n ======== Sets Example Module is Running ')


    ds_set = {4, 5, 88, -12}

    ds_set_01 = set([1, 4])
    ds_set_02 = set((1, 4))


    for x in ds_set:
        print(x)

    bool_a = 5 in ds_set
    bool_b = 5 not in ds_set

    ds_set.add(56)      # added since not in set
    ds_set.add(88)      # added since not in set

    ds_set.update([533, 544])
    ds_set.update ((633, 644))

    if 533 in ds_set:
        ds_set.remove(533)

    if 1533 in ds_set:
        ds_set.remove (1533)

    #no need to assure membership
    #before removing member from set
    ds_set.discard(533)
    ds_set.discard(56)


    #create a set
    other_set = ds_set.copy()   # create d differenr set object
    another_set = set(ds_set)   # create d differenr set object

    #sets operation
    set_a = set((1, 2, 4, 6, 8))
    set_b = set ((2, 6, 9, 33))

    a_b_union = set_a.union(set_b)
    a_b_intersection = set_a.intersection(set_b)

    a_diff_b = set_a.difference (set_b)
    b_diff_a = set_b.difference (set_a)
    a_b_mutual_diff = set_a.symmetric_difference (set_b)

    #check if oine set is subset of another
    a_b_intersection.issubset(a_b_union)
    a_b_union.issuperset(a_b_intersection)

    #check if sets have empty intersection
    a_diff_b.isdisjoint(b_diff_a)


    print ('\n ----------- Sets Module is Done >>>> ')