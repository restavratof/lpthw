from nose.tools import *
from parser import parser


def test_peek():
    assert_equal(parser.peek([('direction', 'north')]), 'direction')
    # result = parser.peek([('verb', 'run'), ('direction', 'north')])
    # assert_equal(result, ['verb', 'direction'])
