#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-22 14:39:00
# @Author  : huajh7 (huajh7@gmail.com)
# @Link    : http://www.huajh7.com/
# @Version : $Id$

"this is a test module"

import os
import sys
import numpy

debug = True

class foolclass (object):

    "Foo class"
    pass


def test():
    "test function"
    foo = foolclass()

    if debug:
        print('run test')


if __name__ == '__main__':
    test()
    print(sys.version)

    ls = os.linesep  # '\r\n'
    fname = 'input.txt'
    # while True:
    #     if os.path.exists(fname):
    #         print("Error: '%s' already exists" % fname)
    #     else:
    #         break

    fname = input('Enter filename:')
    try:
        fobj = open(fname,'r')
    except IOError as e:
        print ("*** file open error:", e)
    else:
        # display contents to the screen 
        for eachline in fobj:
            print(eachline)
        fobj.close()

    contents = []

    print("\nEnter lines ('.' by itself to quit).\n")

    while True:
        entry = input('>')
        if entry == '.':
            break
        else:
            contents.append(entry)

    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in contents])
    fobj.close()
    print('DONE!')
