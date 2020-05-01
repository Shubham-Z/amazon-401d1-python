from array_shift import __version__
from array_shift.array_shift_module import insertShiftArray


def test_version():
    assert __version__ == '0.1.0'
    
def test_insertShiftArraySuccess():
    assert insertShiftArray([2,4,6,8], 5) == [2, 4, 5, 6, 8]

def test_insertShiftArraySuccess2():
    assert insertShiftArray([4,8,15,23,42], 16) == [4,8,15,16,23,42]
