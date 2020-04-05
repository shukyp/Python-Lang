
#import search path are set by the list of paths in sys.path
#
# to display the path settings do as follows:
# import sys# sys.path
#
# will get as follows
#------------------------
# ['C:\\Program Files\\JetBrains\\PyCharm Community Edition 2017.3.3\\helpers\\pydev', 'G:\\dvlp (study)\\python\\become_pro',
#   'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2017.3.3\\helpers\\pydev', 'C:\\ProgramData\\Anaconda3\\python37.zip',
#   'C:\\ProgramData\\Anaconda3\\DLLs', 'C:\\ProgramData\\Anaconda3\\lib', 'C:\\ProgramData\\Anaconda3', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages',
#   'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib',
#   'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin', '
#   G:\\dvlp (study)\\python\\become_pro', 'G:/dvlp (study)/python/become_pro']
#

#import could be
# from statistics inport *
# so we could call every function by its name
# however this may create  acollision with functions of same name from other imported modules
import statistics as stat

my_list = [5, 3, 2, 9, 9, 7, 4, 3, 1, 8, 9]

#================================================================================
#module entry point function
def importer_mdl():

    print ('\n\n ======== Importer (Statistics) Example Module is Running ')

    #calc mean
    x = stat.mean(my_list)
    print('\n Median: %.6f' % x)

    #calc median
    x = stat.median(my_list)
    print('\n Median: %.6f' % x)

    #calc mode
    x = stat.mode(my_list)
    print('\n Mode: %.6f' % x)

    #calc standard deviation
    x = stat.stdev(my_list)
    print('\n Std dev: %.6f' % x)

    #calc variance
    x = stat.variance(my_list)
    print('\n Variance: %.6f' % x)

    print ('\n ----------- Importer (Statistics) Example Module is Done >>>> ')

