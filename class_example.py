#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class AddrBookEntry(object):

    'address book entry class'

    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print('Created instance for:', self.name)

    def updatePhone(self, newph):
        self.phone = newph
        print('Updated phone for:', self.name)


class EmpAddrBookEntry(AddrBookEntry):

    'Employee Address Book Entry class'

    def __init__(self, nm, ph, id0, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id0
        self.email = em
       # super().updatePhone('123456')

    def getPhone(self):
        return self.phone

    def updateEmail(self, newem):
        self.email = newem
        print('Updated e-mail address for:', self.name)


class InstCt(object):

    count = 0
    x = {2003: 'poe'}

    def __init__(self):
        InstCt.count += 1

    def __del__(self):
        InstCt.count -= 1

    def howMany(self):
        return InstCt.count


'Static method and classmethod'


class TestStaticMethod:

    @staticmethod
    def func():
        print('calling static method func()')


class TestClassMethod:

    @classmethod
    def func(cls):
        print('calling class method func()')
        print('func() is part of class', cls.__name__)


class RoundFloat(float):

    def __new__(cls, val):
        return float.__new__(cls, round(val, 2))


if __name__ == '__main__':
    
    john = AddrBookEntry('John Doe', '408-555-1212')
    jane = AddrBookEntry('Jane Doe', '650-555-1212')
    john.updatePhone('415-555-1212')
    john.updatePhone('123-442-323')



    john2 = EmpAddrBookEntry('John Doe', '408-555-1212', 42, 'jonh@spam.doe')
    print(john2.getPhone())
    john2.updatePhone('111-555-1212')
    print(john2.getPhone())

    a = InstCt()
    print(a.x)
    a.x[2004] = 'valid path'
    print(a.x)
    print(InstCt.x)
    print(a.howMany())
    b = InstCt()
    c = InstCt()
    print(c.howMany())
    print(b.howMany())
    del c
    print(b.howMany())
    del b
    print(a.howMany())
    del a
    print(InstCt.count)

    tsm = TestStaticMethod()
    TestStaticMethod.func()
    tsm.func()
    tcm = TestClassMethod()
    TestClassMethod.func()
    tcm.func()
