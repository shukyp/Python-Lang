

__all__ = ['OldSubCalc__', 'VERY_OLD_SOME_VAL']

OKD_SOME_VAL = 50
VERY_OLD_SOME_VAL = 40


class OldSubCalc:

    def __init__(self):
        pass

    def __repr__ (self):
        return ('{obj.__class__.__name__} __repr__'.format(obj=self))

    def __str__(self):
        return ('{obj.__class__.__name__} __str__'.format(obj=self))

    def oldAdder(self, a, b):
        print('\n[OldSubCalc]/Add')

    def oldSuber(self, a, b):
        print('\n[OldSubCal]c/Sub')

    def oldMuler(self, a, b):
        print('\n[OldSubCalc]/Mul')

    def oldDiver(self, a, b):
        print('\n[OldSubCalc]/Div')



class OldSubCalc__:

    def __init__(self):
        pass

    def __repr__ (self):
        return ('{obj.__class__.__name__} __repr__'.format(obj=self))

    def __str__(self):
        return ('{obj.__class__.__name__} __str__'.format(obj=self))

    def oldAdder__(self, a, b):
        print('\n[OldSubCalc__]/Add')

    def oldSuber__(self, a, b):
        print('\n[OldSubCalc__]/Sub')

    def oldMuler__(self, a, b):
        print('\n[OldSubCalc__]/Mul')

    def oldDiver__(self, a, b):
        print('\n[OldSubCalc__]/Div')

