#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-22 18:44:49
# @Author  : huajh7 (huajh7@gmail.com)
# @Link    : http://www.huajh7.com/
# @Version : $Id$

import os
import types
import operator
from decimal import Decimal


def displayNumType(num):
    print(num, 'is')
    if isinstance(num, (int, float, complex)):
        print('a number of type:', type(num).__name__)
    else:
        print('not a number at all.')


if __name__ == '__main__':
    displayNumType(-69)
    displayNumType(999999999999999999999999999)
    displayNumType(98.6)
    displayNumType(-5.3+1.9j)
    displayNumType('xxxxx')
    a = 100
    b = 223
    if operator.lt(a, b):
        print('a < b')
    if operator.le(a, b):
        print('a <= b')
    if operator.eq(a, b):
        print('a == b')
    if operator.ne(a, b):
        print('a != b')
    if operator.gt(a, b):
        print('a > b')
    if operator.ge(a, b):
        print('a >= b')

    dec = Decimal('.1')

    s = 'fasdfefjlj'
