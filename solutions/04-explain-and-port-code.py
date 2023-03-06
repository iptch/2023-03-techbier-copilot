#! /usr/bin/env python

import pytest 
# float unknown_function(int n) {
#     float unknown = 0.0;
#     int unknown = 1;
#     for (int i = 1; i < n; i += 2) {
#         unknown += sign * 4.0 / i;
#         sign *= -1;
#     }
#     return unknown;
# }

# port to python
def unknown_function(n):
    '''
    Calculate pi
    '''
    unknown = 0.0
    sign = 1
    for i in range(1, n, 2):
        unknown += sign * 4.0 / i
        sign *= -1
    return unknown

# test
def test_unknown_function():
    assert unknown_function(1000000) == pytest.approx(3.14159, 0.00001)

