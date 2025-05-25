import pytest
from models import *

"""-- class ARRAY tests --
    Array initalization
    * Checks that proper errors are raised upon invalid initialization
"""
def test_Array_with_no_type():
    with pytest.raises(ValueError):
        no_type_array = Array(length=3, array=[1, 2, 3])

def test_Array_invalid_type_param():
    with pytest.raises(TypeError):
        invalid_type_param_array = Array(length=3, type=0, array=[1, 2, 3])

def test_Array_with_no_length():
    with pytest.raises(ValueError):
        no_length_array = Array(type="int", array=[1, 2, 3])

def test_Array_negative_length():
    with pytest.raises(ValueError):
        negative_length_array = Array(length=-1, type="int")

def test_Array_non_int_length_param():
    with pytest.raises(TypeError):
        non_int_length_array = Array(length="3", type="int", array=[1, 2, 3])


    

    

