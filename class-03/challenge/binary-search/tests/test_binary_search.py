from binary_search import __version__
from binary_search.binary_serach_module import binarySearch


def test_version():
    assert __version__ == '0.1.0'
    
def test_binarySearchSuccess():
    assert binarySearch([4,8,15,16,23,42], 15) == 2
    
def test_binarySearchSuccess2():
    assert binarySearch([11,22,33,44,55,66,77], 90) == -1
