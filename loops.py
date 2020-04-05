
def while_loop():
    i = 0

    print ('\n\n While Loop \n')
    while (i <= 10):
        print ('i=%d' % (i))
        i += 1


#for loop of conainer elements
def for_loop_container():
    '''
    for loop of conainer elements
    :return:none
    '''

    #container init
    someList = [2, 4, 6, 3, -1, 66]

    print ('\n\n For Loop - running on list elements \n');
    for elem in someList:
        print ('elem: %d' % (elem))


#for loop of a range
def for_loop_range():
    '''
    for loop of a range
    :return:none
    '''
    print ('\n\n For Loop - running on range of values \n');
    low = 1
    high = 12
    for elem in range (low, high):
        print ('elem: %d' % (elem))


#module entry point function
def loops_mdl():

    print ('\n\n ======== Loops Module is Running ')

    while_loop()
    for_loop_container()
    for_loop_range()

    print ('\n ----------- Loops Module is Done >>>> ')
