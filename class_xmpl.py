

#example class

class calc:

    def add(x, y):
        return(x+y)

    def sub (x, y):
        return (x - y)

    def mul (x, y):
        return (x * y)

    def div (x, y):
        return (x / y)





#module entry point function
def class_xmpl_mdl():

    x = 5
    y = 8
    rslt = 0.0

    print ('\n\n ======== Class Example Module is Running ')

    #add
    rslt = calc.add(x, y)
    print("\n Add result: %d + %d = %d" %(x, y, rslt))

    #sub
    rslt = calc.sub(x, y)
    print("\n Sub result: %d - %d = %d" %(x, y, rslt))

    #mul
    rslt = calc.mul(x, y)
    print("\n Multiply result: %d * %d = %d" %(x, y, rslt))

    #mul
    rslt = calc.div(x, y)
    print("\n Divide result: %d / %d = %.3f" %(x, y, rslt))

    print ('\n ----------- Class Example Module is Done >>>> ')

