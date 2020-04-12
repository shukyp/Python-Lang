#===========================================================================
#                           BaseClass Module
#===========================================================================

"""
#BaseClass - Shows How a calss looks loke
#
# Author: Shuky Persky
#
"""

class BaseClass:

    _shape_index = 1;                   #class attribute

    @classmethod                        #inhrited by derived class
    def _get_next_shape_index(cls):
        idx = cls._shape_index
        cls._shape_index += 1
        return idx

    @classmethod
    def _get_next_index(cls):           #inhrited by derived class
        idx = cls._shape_index;         #use (local/derived) class attribute
        cls._figure_index += 1
        return idx

    @staticmethod                       #inhrited by derived class
    def _something(val):
        return (val*3)

    #polymorphism - late bindinh        #inhrited
    #can be used by derived classes
    def show_info(self):
        print ('\n')
        print('Shape: {0}'.format(self._shape))
        print('Width: {0}'.format(self._width))
        print('Length: {0}'.format(self._length))
        print('Local Index: {0}'.format(self._local_index))
        print('Global Index: {0}'.format(self._glbl_index))

        print('Area: {0}'.format(self.area()))


#from base_class import BaseClass

#===========================================================================
def base_class_mdl():
    '''module entry point function
    :Args:      None
    :return     None
    '''

    print ('\n\n ======== base_class Module is Running ')


    print ('\n ----------- base_class Module is Done >>>> ')