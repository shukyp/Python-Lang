
# non-default value parameter must come before ALL default value parameter(s)
def func_example(font='Arial', bg_color='yellow', font_size = 14, font_color = 'red'):
    print('font:', font)
    print ('bg_color:', bg_color)
    print ('font_size:', font_size)
    print ('font_color:', font_color)

#module entry point function
def funcs_mdl():

    print ('\n\n ======== Funcs Module is Running ')

    # init
    font = 'TMN'
    bg_color = 'white'
    font_size = 11
    font_color = 'black'

    # call func with arguments
    print ('\n\n default order, explicit values / no default values \n')
    func_example (font, bg_color, font_size, font_color);

    # call func with params:arguments pairs
    print ('\n\n free order, explicit values / no default values \n')
    func_example (bg_color='white',
                  font='TMN',
                  font_color='black',
                  font_size=11)

    # call func with partial set of arguments
    print ('\n\n default order, partiall explicit values / partial default values) \n')
    func_example ('TMN_new', 'white')

    print ('\n ----------- Funcs Module is Done >>>> ')
