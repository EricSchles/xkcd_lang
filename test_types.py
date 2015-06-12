from xkcd_types import Types

def test_int_add():
    first = Types(1)
    second = Types(2)
    assert first + second == 'DONE'

def test_int_str_add():
    first = Types(1)
    second = Types("3")
    assert first + second == "4"

def test_str_int_add():
    first = Types("1")
    second = Types(3)
    assert first + second == "4"

def test_const_increasing_seq_add():
    first = Types([1,2,3])
    second = Types(4)
    assert first + second == True

def test_power_increasing_seq_add():
    first = Types([1,4,9])
    second = Types(16)
    assert first + second == True
