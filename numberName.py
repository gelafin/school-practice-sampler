# Author: Mark Mendez
# Date: 9/23/2020
# Description: trivial test script that shows basic exception handling

class OutOfRangeError(Exception):
    pass

def numberName(number):
    """prints the spelled input number if input is in range 1-3, else raises OutOfRangeError"""
    if number == 1:
        print('one')
    elif number == 2:
        print('two')
    elif number == 3:
        print('three')
    else:
        raise OutOfRangeError

try:
    name = numberName(int(input('please give a number 1-3: ')))
except OutOfRangeError:
    print('That number is out of range')
