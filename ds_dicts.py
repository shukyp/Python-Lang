#===========================================================================
#                           Dictionary Module
#===========================================================================
"""
# Demonstrates accessing the builtin Dictionary type (container)
#
#   Dictionary is mutable
#   Key - Immutable
#   Value = Mutable
#
#   support the following protocols: Container, Size, Iterable, Mutable Mapping.
#
# Author: Shuky Persky
#
"""

#---------------------------------------------------------------------------------
# list obj APIs:
# https://www.w3schools.com/python/python_dictionaries.asp
# https://www.tutorialspoint.com/python/python_dictionary.htm
#---------------------------------------------------------------------------------


#================================================================================
def dicts_comrehension (dct):
    '''Shows how to implement list comprehension

     :arg        dict(dictionary)
                     just data

     :return:    none

     :raises     none
     '''

    # do it
    words = "Why there are sunny days while sometimes there are cloudy days as well".split ()
    words_len_dict = {word:len (word) for word in words}
    print ('\n the words_len dictionary generated by comprehension {}'.format (words_len_dict))

    # the expression can be generated by a functiion call, based on existing list
    x0_dct = {word:len(word) for chr,word in dct.items()}
    print ('\n the disctionary generated by comprehension based on factorial {}'.format (x0_dct))


    from math import factorial

    # the expression can be generated by a functiion call, based on a range, NO filtering
    x1_dct = {str (factorial (x)):x for x in range (3, 11) if (x>=0)}
    print ('\n the list generated by comprehension based on factorial {}'.format (x1_dct))

    # the expression can be generated by a functiion call, based on a range, WITH filtering
    x2_dct = {str (factorial (x)):x for x in range (3, 11) if ((x%2==0) and (x>=0))}
    print ('\n the list generated by comprehension based on factorial {}'.format (x2_dct))


#================================================================================
def dicts_iterator (dict):
    '''Shows how to implement list iterator

     :arg        dict(dictionary)
                     just data

     :return:    none

     :raises     none
     '''

    # create iiterator
    try:
        iterator = iter (dict.items())
    except Exception as e:
        print(f'{e!r}')

    while (True):
        try:
            elem = next (iterator)
            print (f'key={elem[0]}, value={elem[1]}')
        except StopIteration as SI_e:
            print (f'=> {SI_e!r})')
            break

    print ('\n We are done with iterator traverse')

#================================================================================
#module entry point function
def ds_dicts_mdl():
    '''
    The Dictionary is a collection of mutable objects.
    The objects are Key:Value. The Key MUST NOT be duplicated (MUST b eunique)
    The order is according the order of insertion

    ?? List allows duplicate elements. Elements can be of different types ??
    '''

    print ('\n\n ======== Dicts Module is Running ')

    #init
    dct_01 = {'Alice':32, 'Bob':24, 'Charles':56, 'Dave':32}
    dct_02 = dict(Alice=32, Bob=24, Charles=56, Dave=32)

    pntc_01 = dict(a='alfa', b='bravo', c='Charlie', d='delta', e='echo', f='fox')
    pntc_02 = dict(f='Foxtrot', g='Golf', h='Hotel', i='India', j='Juliett', k='Kilo', l='Lima')
    pntc_03 = dict(m='Mike', n='November', o='Oscar', p='Papa', q='Quebec', r='Romeo', s='Sierra')
    pntc_04 = dict(t='Tango', u='Uniform', v='Victor', w='Whiskey', x='Xray', y='Yankee', z='Zulu')

    empty_dct_01 = {}
    empty_dct_02 = dict()

    dct_lists = {'a':[1, 2, 55, -12], 'b':[-1, -2, -55, 12], 'c':[11, 12, 155, -112], 'd':[21, 22, 255, -212]}
    dct_lists['b'] += [33, -34, 35, -37]

    #copy
    pntc = pntc_01.copy()
    pntc.update(pntc_02)
    pntc.update (pntc_03)
    pntc.update (pntc_04)

    # join
    #if the dictionary for the update holds keys whaih are already in the updated dictionary
    #then the value of that key takes th enew value (the old one is overwritten)
    pntc_10 = dict (a='alfa___', b='bravo___', c='Charlie___', d='delta___', e='echo___', f='fox___')
    pntc.update (pntc_10)

    for key in pntc:
        print (f'{key}: {pntc[key]}')

    for key in pntc.keys():
        print(f'{key}: {pntc[key]}')

    for val in pntc.values():
        print (f'{val}')


    # iterante over keys and values in tandem
    # on evry cycle a pair is retrieved as a tuple (key, value)
    # this way we do unpacking and get the (key value) paur
    for key, value in pntc.items():
        print (f'{key}: {value}')

    #we can check if a key is in the dictionary
    if ('a' in pntc):
        print('\n \'a\' in the pntc dictionary')
    else:
        print('\n \'a\' NOT in the pntc dictionary')

    if ('aa' not in pntc):
        print('\n \'aa\' NOT in the pntc dictionary')
    else:
        print('\n \'aa\' in the pntc dictionary')

    #delete a key

    del (pntc_10['f'])



    print('\n-------------------------')

    dicts_comrehension(pntc)

    print('\n-------------------------')

    dicts_iterator (pntc)

    print ('\n ----------- Dicts Module is Done >>>> ')