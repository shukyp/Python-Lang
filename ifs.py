


#module entry point function
def ifs_mdl():

    print ('\n\n ======== IFs Module is Running ')

    print ('\n\n If statement \n');
    x = 3
    y = 55
    z = 92

    # simple if
    if (x > y):
        print ("x:%d > y:%d" % (x, y))

    if (y > x):
        print ("y:%d > x:%d" % (y, x))

    # multiple if
    if (x < y < z):
        print ("x:%d < y:%d < z:%d" % (x, y, z))

    # if else (simple else)
    if (x > y):
        print ("[main] x:%d > y:%d" % (x, y))
    else:  # if the main if not fulfilled
        print ("[else] y:%d > x:%d" % (y, x))

    # if else (elif)
    if (x > y):
        print ("[main] x:%d > y:%d" % (x, y))
    elif (y > 50):  # elif if the main if not fulfilled
        print ("[elif] y:%d > 50" % (y))
    else:  # else if elif not fulfilled
        print ("[else follows elif]")

    print ('\n ----------- IFs Module is Done >>>> ')
