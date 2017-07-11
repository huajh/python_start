import os

import pprint
from sklearn import svm


def main():
    filepath = os.path.dirname(__file__)
    print(
        'I don\'t use any of imports on this file line is longer than pep8 limits')
    i_am_an_unused_variable = None
    'this format doesn\'s follow indentation rule {}, {}'.format(
        'no',
        'rules')

if __name__ == '__main__':
    main()
    

