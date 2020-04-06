#===========================================================================
#                           Files Module
#===========================================================================
"""
#Demonstrates accessing text file
#
# Author: Shuky Persky
#
"""

from os import SEEK_SET, SEEK_CUR, SEEK_END
from os import getcwd

#--------------------------------------------------------------
# see file open modes
# https://www.tutorialspoint.com/python/python_files_io.htm
#--------------------------------------------------------------

#==================================================================================
#writes some text to file in data folder below working directory
#wd: working directory
def write_to_file(wd):

    #init
    file_name = "pt_out_write.txt"
    pathname = "{}/{}/{}".format(wd, "data", file_name)
    some_text = "Example Text"
    my_name = "David Koper"

    #open file for writing
    try:
        f = open(pathname, 'w+')

    except Exception as e:
        f.close()
        print("file %s open failed (%s)" % (pathname, str(e)))
        return

    #write to file
    f.write ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    #write to file
    f.write(some_text)
    f.write("\nMy name is %s" % (my_name))

    f.write("JJJJJ TTTT WWWW")
    f.flush()

    #seek, overwrite
    f.seek(2, SEEK_SET)
    f.write ("-X-1-X-")
    f.flush()

    f.write ("-JJJJJJJJJJJJJJJJJJJJ TTTTTTTTTTTTTTTTTTTTTTTTT MMMMMMMMMMMMMMMMMMMM-")
    print('\npos1=%d'%f.tell()) # SP--
    f.seek(f.tell()-27, SEEK_SET)
    print('\npos1=%d'%f.tell()) # SP--
    f.write ("-X-4-X-")
    f.flush()

    #save position
    pos = f.tell()

    #jump to end of file
    f.seek(0, SEEK_END)
    f.seek(f.tell()-47, SEEK_SET)
    f.write ("-X-2-X-")
    f.flush()

    #return to prev. position
    f.seek(pos, SEEK_SET)
    f.write ("-X-3-X-")
    f.flush()


    #close file
    f.close()


#==================================================================================
#Append some text (writes) at the end of file in data folder below working directory
#wd: working directory
def append_to_file(wd):

    #init
    file_name = "pt_out_append.txt"
    pathname = "{}/{}/{}".format(wd, "data", file_name)
    some_text = "Some more Text"
    my_name = "David Koper"

    #open file for writing
    try:
        f = open (pathname, 'a')

    except Exception as e:
        f.close()
        print("file %s open failed (%s)" % (pathname, str(e)))
        return

    #write to file
    f.write('\n'+ some_text)
    f.write(" Add by %s" % (my_name))

    #close file
    f.close()


#==================================================================================
#Read some text from file in data folder below working directory
#wd: working directory
def read_from_file(wd):

    #init
    file_name = "pt_out_append.txt"
    pathname = "{}/{}/{}".format(wd, "data", file_name)

    #open file for writing
    f = open(pathname, 'r')
    try:
        f = open (pathname, 'r')

    except Exception as e:
        f.close()
        print("file %s open failed (%s)" % (pathname, str(e)))
        return

    #read from file
    some_text = f.read()
    print("This text was read from file \n %s \n\n" % (some_text))

    #split the text that was read from file
    splitted = some_text.split('\n')
    print("This is splitted text (read from file) \n %s \n\n" % (splitted))
    print('\n\nSingle lien number 3: %s' %(splitted[3]))

    #close file
    f.close()



#==================================================================================
#module entry point function
def files_mdl():

    #find working directory
    wd = getcwd()

    print ('\n\n ======== Files Module is Running ')

    #write some data to file
    print("\nWriting to file")
    write_to_file(wd) ##create the file (if not exist)
    write_to_file(wd) #overwrite it

    #append some data to file
    print("\nAppending to file")
    append_to_file(wd) #create the file (if not exist)
    append_to_file(wd) #append to existing content

    #read from data to file
    print("\nReading from file")
    read_from_file(wd) #read from file


    print ('\n ----------- Files Module is Done >>>> ')
