# core python programming 2nd p277
from time import ctime, sleep


def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s () called' % (ctime(), func.__name__))
        return func()
    return wrappedFunc


@tsfunc
def foo1():
    pass

if __name__ == '__main__':
    foo1()    
    sleep(4)
    for i in range(2):
        sleep(1)
        foo1()
