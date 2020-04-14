
#===========================================================================
#                           BaseClass Module
#===========================================================================

"""
#BaseClass - Shows How a calss looks loke
#
# Author: Shuky Persky
#
"""

from oo_base_class import *

#===========================================================================
class DerivedClass_Triangle(BaseClass):

    _figure_index = 1                                                    #class attribute

    @classmethod
    def _get_next_index(cls):
        idx = cls._figure_index;                                        #use (local/derived) class attribute
        cls._figure_index += 1
        return idx

    @staticmethod                                                       # inhrited by derived class and overrides the base class same method
    def _something (val):                                               # and overrides the base class same mehod
        return (val * 44)

    #initializer (not a constructor)
    def __init__(self, base, height):
        self._cache = {}
        self._shape = "Triangle"
        self._width = base      #length of triangle base
        self._length = height   #triangle height

        self._local_index = DerivedClass_Triangle._get_next_index()    # use (local/derived) class method
        self._glbl_index = self._get_next_shape_index()                 # The classmethod of the Base class is inherited
                                                                        # so it uses the BaseClass attribute

    def __call__ (self):
        '''Callable instance '''
        if (self._local_index not in self._cache):
            id = self._local_index
            shape = self._shape
            self._cache[id] = shape
            return (id, shape)
        return None

    def __repr__ (self):
        return ('{obj.__class__.__name__}({obj._width}, {obj._length})'.format(obj=self))

    def __str__(self):
        return ('{obj.__class__.__name__}: type:{obj._shape}, width={obj._width}, height={obj._length}'.format(obj=self))

    def area(self):
        return (self._width * self._length / 2)


#===========================================================================
class DerivedClass_Rectangular(BaseClass):

    _figure_index = 1

    @classmethod                                                        #inhrited by derived class and overrides the base class same method
    def _get_next_index(cls):                                           #may also be used as constrtors
        idx = cls._figure_index                                         #use (local/derived) class attribute
        cls._figure_index += 1
        return idx

    @staticmethod                                                       # inhrited by derived class
    def _something (val):                                               # and overrides the base class same mehod
        return (val * 33)

    #initializer (not a constructor)
    def __init__(self, shape, width, length):
        self._cache = {}
        self._shape = shape
        self._width = width
        self._length = length

        self._local_index = DerivedClass_Rectangular._get_next_index()  #use (local/derived) class method
        self._glbl_index = self._get_next_shape_index()                 # The classmethod of the Base class is inherited
                                                                        # so it uses the BaseClass attribute

    def __call__(self):
        '''Callable instance '''
        if (self._local_index not in self._cache):
            id = self._local_index
            shape = self._shape
            self._cache[id] = shape
            return (id, shape)
        return None

    def clear(self):
        self._cache.clear()

    def __repr__(self):
        return '{obj.__class__.__name__}({obj._shape}, {obj._width}, {obj._length})'.format(obj=self)

    def __str__(self):
        return '{obj.__class__.__name__}: type:{obj._shape}, width={obj._width}, length={obj._length}'.format(obj=self)

    def area(self):
        return (self._width * self._length)


#===========================================================================
def derived_class_mdl():
    '''module entry point function
    :Args:      None
    :return     description
    '''

    print ('\n\n ======== derived_class Module is Running ')


    #create triangle object & show info
    tri = DerivedClass_Triangle(10, 10)
    x = tri()               # invokes __call__
    if (x != None):
        print('\nid={obj[0]}, shape={obj[1]}'.format(obj=x))

    tri.show_info()
    print(tri)              # invokes __str__
    #tri                    # from REPL invokes __repr__

    print(f'{tri!s}')       #invokes __str__
    print(f'{tri!r}')       #invokes __repr__



    #create triangle object & show info
    rec_rec = DerivedClass_Rectangular('Rectangle', 12, 12)
    x = rec_rec()           # invokes __call__
    if (x != None):
        print('\nid={obj[0]}, shape={obj[1]}'.format(obj=x))

    rec_rec.show_info()
    print(rec_rec)          # invokes __str__
    #rec_rec                # from REPL invokes __repr__

    print (f'{rec_rec!s}')  # invokes __str__
    print (f'{rec_rec!r}')  # invokes __repr__



    #create triangle object & show info
    rec_sq = DerivedClass_Rectangular('Square', 9, 9)
    x = rec_sq()            # invokes __call__
    if (x != None):
        print('\nid={obj[0]}, shape={obj[1]}'.format(obj=x))

    rec_sq.show_info()
    print(rec_sq)           # invokes __str__
    #rec_sq                 # from REPL invokes __repr__

    print (f'{rec_sq!s}')   # invokes __str__
    print (f'{rec_sq!r}')   # invokes __repr__


    print ('\n ----------- derived_class Module is Done >>>> ')