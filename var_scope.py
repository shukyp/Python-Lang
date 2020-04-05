
#global variable
xx = 7

#function that refers a global variable
def func_global():
    global xx    # identify referring global x

    print ('[func_global] global x=', xx) # print global xx
    xx += 1                 # increment global xx
    print ('[func_global] global x=',xx)  # print global xx


#function that refers a local variable
#that has the same shadows/name of global variable
def func_local():

    #print (xx)             #won't work since no local x declared/defined
    xx = 9                  #local local xx declared/defined
    print ('[func_local] global x=', xx) #will work


#module entry point function
def scope_mdl():

    print ('\n\n ======== SCOPE Module is Running ')

    print('\n\n Calling functions that refer global/local variables \n')
    print('\nGlobal xx=', xx)
    func_global()
    func_local()

    print ('\n ----------- SCOPE Module is Done >>>> ')
