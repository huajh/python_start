# core python programming p395

import os
import pickle



class FileDescr(object):
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError("%r used before assigment" % self.name)

        try:
            f = open(self.name, 'rb')
            val = pickle.load(f)
            f.close()
            return val
        except(pickle.UnpicklingError, IOError, EOFError, AttributeError, ImportError,
                IndexError) as e:
            raise AttributeError("could not read %r: %s" % self.name)

    def __set__(self, obj, val):
        f = open(self.name, 'wb')
        try:
            pickle.dump(val, f)
            FileDescr.saved.append(self.name)
        except(TypeError, pickle.PicklingError) as e:
            raise AttributeError("could not pickle %r" % self.name)
        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError) as e:
            pass


class MyFileVarClass(object):
    fo = FileDescr('fo')
    bar = FileDescr('bar')


if __name__ == '__main__':
    fvc = MyFileVarClass()
   # print(fvc.fo)
    fvc.fo = 1234
    fvc.bar = 'leanna'
    print (fvc.fo, fvc.bar)
    del fvc.fo
    print (fvc.fo, fvc.bar)


    # data1 = {'a': [1, 2.0, 3, 4+6j],
    #          'b': ('string', u'Unicode string'),
    #          'c': None}

    # selfref_list = [1, 2, 3]
    # selfref_list.append(selfref_list)

    # output = open('fo', 'wb')

    # # Pickle dictionary using protocol 0.
    # pickle.dump(data1, output)

    # # Pickle the list using the highest protocol available.
    # pickle.dump(selfref_list, output, -1)

    # output.close()    
