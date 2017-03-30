# P398

class DevNull1(object):

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        print('Accessing [%s] ... ignoring' % self.name)

    def __set__(self, obj, val):
        print('Attempt to assign %r to [%s]... ignoring' % (val, self.name))


class C1(object):
    fo = DevNull1()


class ProtectAndHideX(object):

    def __init__(self, x):
        assert isinstance(x, int), '"x" must be an integer!'
        self.__x =~x

    def get_x(self):
        return ~self.__x

    x = property(get_x, doc='hidex')


class HideX(object):

    def __init__(self, x):
        self.x = x

    def get_x(self):
        return ~self.__x

    def set_x(self, x):
        assert isinstance(x, int), '"x" must be an integer!'
        self.__x = ~x

    x = property(get_x,set_x)


if __name__ == '__main__':
    c1 = C1()
    c1.fo = 'bar'
    print(c1.fo)

    c1.__dict__['fo'] = 'bar'
    x = c1.fo
    print(x)

    inst = ProtectAndHideX(10)
    print(inst.x)
    print(inst.x.__doc__)
    #inst.x = 20

    inst = HideX(20)
    print (inst.x)
    inst.x = 30
    print(inst.x)
    print(inst.x.__doc__)


    
