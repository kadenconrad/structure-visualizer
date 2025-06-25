import pytest
from src.models._array import Array, get_random_words, set_upper, set_lower, TYPE_MAPPINGS

# run `pytest tests/test_array` from root directory to test

class TestArrayInitialization:
    def test_valid_int_array_creation(self):
        arr = Array("int", 5)
        assert arr.array_type == "int"
        assert arr.size == 5
        assert arr.total_memory == 20  # 4 bytes * 5 elements
    
    def test_valid_uint_array_creation(self):
        arr = Array("uint", 10)
        assert arr.array_type == "uint"
        assert arr.size == 10
        assert arr.total_memory == 40  # 4 bytes * 10 elements
    
    def test_valid_double_array_creation(self):
        arr = Array("double", 3)
        assert arr.array_type == "double"
        assert arr.size == 3
        assert arr.total_memory == 24  # 8 bytes * 3 elements
    
    def test_valid_string_array_creation(self):
        arr = Array("str", 5, max_str_length=10)
        assert arr.array_type == "str"
        assert arr.size == 5
        assert arr.str_arr_length == 11  # 10 + 1 for null terminator
        assert arr.total_memory == 55  # 11 * 5 elements
    
    def test_invalid_array_type(self):
        with pytest.raises(ValueError, match="Please choose valid array type"):
            Array("invalid_type", 5)
    
    def test_invalid_size_zero(self):
        with pytest.raises(ValueError, match="Array size must be valid positive integer"):
            Array("int", 0)
    
    def test_invalid_size_negative(self):
        with pytest.raises(ValueError, match="Array size must be valid positive integer"):
            Array("int", -5)
    
    def test_invalid_size_non_integer(self):
        with pytest.raises(ValueError, match="Array size must be valid positive integer"):
            Array("int", 5.5)
    
    def test_string_array_without_max_length(self):
        with pytest.raises(ValueError, match="Must specify string length if declaring string array"):
            Array("str", 5)
    
    def test_string_array_with_zero_max_length(self):
        arr = Array("str", 3, max_str_length=0)
        assert arr.str_arr_length == 1  # 0 + 1 for null terminator


class TestArrayIndexAccess:
    def test_get_index_data_int_array(self):
        arr = Array("int", 5)
        arr.set_index(0, 42)
        arr.set_index(2, 100)
        
        assert arr.get_index_data(0) == 42
        assert arr.get_index_data(2) == 100
        assert arr.get_index_data(1) == 0  # Default value
    
    def test_get_index_data_double_array(self):
        arr = Array("double", 3)
        arr.set_index(0, 3.14)
        arr.set_index(1, -2.5)
        
        assert arr.get_index_data(0) == 3.14
        assert arr.get_index_data(1) == -2.5
    
    def test_get_index_data_string_array(self):
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "hello")
        arr.set_index(1, "world")
        
        assert arr.get_index_data(0) == "hello"
        assert arr.get_index_data(1) == "world"
        assert arr.get_index_data(2) == ""
    
    def test_set_index_int_array(self):
        arr = Array("int", 5)
        arr.set_index(0, 42)
        arr.set_index(4, -100)
        
        assert arr.get_index_data(0) == 42
        assert arr.get_index_data(4) == -100
    
    def test_set_index_string_array(self):
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "test")
        arr.set_index(1, "python")
        arr.set_index(2, "array")
        
        assert arr.get_index_data(0) == "test"
        assert arr.get_index_data(1) == "python"
        assert arr.get_index_data(2) == "array"
    
    def test_get_index_data_out_of_bounds_positive(self):
        arr = Array("int", 5)
        with pytest.raises(ValueError, match="Index out of bounds. Array size: 5"):
            arr.get_index_data(5)
    
    def test_get_index_data_out_of_bounds_negative(self):
        arr = Array("int", 5)
        with pytest.raises(ValueError, match="Index out of bounds. Array size: 5"):
            arr.get_index_data(-1)
    
    def test_set_index_out_of_bounds_positive(self):
        arr = Array("int", 5)
        with pytest.raises(ValueError, match="Index out of bounds. Array size: 5"):
            arr.set_index(5, 42)
    
    def test_set_index_out_of_bounds_negative(self):
        arr = Array("int", 5)
        with pytest.raises(ValueError, match="Index out of bounds. Array size: 5"):
            arr.set_index(-1, 42)
    
    def test_set_string_too_long(self):
        arr = Array("str", 3, max_str_length=5)
        with pytest.raises(ValueError, match="Value must be less than 6 characters"):
            arr.set_index(0, "this string is too long")
    
    def test_set_string_max_length(self):
        arr = Array("str", 2, max_str_length=5)
        arr.set_index(0, "12345")  # Exactly 5 characters
        assert arr.get_index_data(0) == "12345"


class TestArrayDisplay:
    
    def test_display_int_array(self, capsys):
        arr = Array("int", 3)
        arr.set_index(0, 1)
        arr.set_index(1, 2)
        arr.set_index(2, 3)
        
        arr.display()
        captured = capsys.readouterr()
        assert captured.out == "[1, 2, 3]\n"
    
    def test_display_double_array(self, capsys):
        arr = Array("double", 2)
        arr.set_index(0, 3.14)
        arr.set_index(1, 2.71)
        
        arr.display()
        captured = capsys.readouterr()
        assert captured.out == "[3.14, 2.71]\n"
    
    def test_display_string_array(self, capsys):
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "hello")
        arr.set_index(1, "world")
        arr.set_index(2, "test")
        
        arr.display()
        captured = capsys.readouterr()
        assert captured.out == "[hello, world, test]\n"
    
    def test_display_single_element(self, capsys):
        arr = Array("int", 1)
        arr.set_index(0, 42)
        
        arr.display()
        captured = capsys.readouterr()
        assert captured.out == "[42]\n"
    
    def test_reverse_traversal_int_array(self, capsys):
        arr = Array("int", 3)
        arr.set_index(0, 1)
        arr.set_index(1, 2)
        arr.set_index(2, 3)
        
        arr.reverse_traversal()
        captured = capsys.readouterr()
        assert captured.out == "[3, 2, 1]\n"
    
    def test_reverse_traversal_string_array(self, capsys):
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "first")
        arr.set_index(1, "second")
        arr.set_index(2, "third")
        
        arr.reverse_traversal()
        captured = capsys.readouterr()
        assert captured.out == "[third, second, first]\n"
    
    def test_reverse_traversal_single_element(self, capsys):
        arr = Array("int", 1)
        arr.set_index(0, 42)
        
        arr.reverse_traversal()
        captured = capsys.readouterr()
        assert captured.out == "[42]\n"


class TestArraySearch:
    
    def test_linear_search_int_found(self):
        arr = Array("int", 5)
        arr.set_index(0, 10)
        arr.set_index(1, 20)
        arr.set_index(2, 30)
        arr.set_index(3, 40)
        arr.set_index(4, 50)
        
        result = arr.linear_search(30)
        assert result == "30 found at index: 2"
    
    def test_linear_search_int_not_found(self):
        arr = Array("int", 3)
        arr.set_index(0, 10)
        arr.set_index(1, 20)
        arr.set_index(2, 30)
        
        result = arr.linear_search(99)
        assert result == "99 not found"
    
    def test_linear_search_double_found(self):
        arr = Array("double", 3)
        arr.set_index(0, 1.1)
        arr.set_index(1, 2.2)
        arr.set_index(2, 3.3)
        
        result = arr.linear_search(2.2)
        assert result == "2.2 found at index: 1"
    
    def test_linear_search_string_found(self):
        arr = Array("str", 4, max_str_length=10)
        arr.set_index(0, "apple")
        arr.set_index(1, "banana")
        arr.set_index(2, "cherry")
        arr.set_index(3, "date")
        
        result = arr.linear_search("cherry")
        assert result == "cherry found at index: 2"
    
    def test_linear_search_string_not_found(self):
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "apple")
        arr.set_index(1, "banana")
        arr.set_index(2, "cherry")
        
        result = arr.linear_search("orange")
        assert result == "orange not found"
    
    def test_linear_search_first_element(self):
        arr = Array("int", 3)
        arr.set_index(0, 100)
        arr.set_index(1, 200)
        arr.set_index(2, 300)
        
        result = arr.linear_search(100)
        assert result == "100 found at index: 0"
    
    def test_linear_search_last_element(self):
        arr = Array("int", 3)
        arr.set_index(0, 100)
        arr.set_index(1, 200)
        arr.set_index(2, 300)
        
        result = arr.linear_search(300)
        assert result == "300 found at index: 2"


class TestArrayPopulate:
    
    def test_populate_int_array(self):
        arr = Array("int", 10)
        arr.populate()
        
        # Check that all values are set (not default 0)
        non_zero_count = sum(1 for i in range(arr.size) if arr.get_index_data(i) != 0)
        assert non_zero_count > 0  # some should be non-zero
    
    def test_populate_int_array_with_bounds(self):
        arr = Array("int", 5)
        arr.populate(lower_bound=10, upper_bound=20)
        
        for i in range(arr.size):
            value = arr.get_index_data(i)
            assert 10 <= value <= 20
    
    def test_populate_uint_array(self):
        arr = Array("uint", 5)
        arr.populate()
        
        # Check all values are non-negative
        for i in range(arr.size):
            value = arr.get_index_data(i)
            assert value >= 0
    
    def test_populate_double_array(self):
        arr = Array("double", 5)
        arr.populate()
        
        # Check that values are set and are floats
        for i in range(arr.size):
            value = arr.get_index_data(i)
            assert isinstance(value, float)
    
    def test_populate_double_array_with_bounds(self):
        arr = Array("double", 3)
        arr.populate(lower_bound=1.0, upper_bound=5.0)
        
        for i in range(arr.size):
            value = arr.get_index_data(i)
            assert 1.0 <= value <= 5.0
    
    def test_populate_string_array(self):
        arr = Array("str", 5, max_str_length=15)
        arr.populate()
        
        # Check that strings are set and within length limits
        for i in range(arr.size):
            value = arr.get_index_data(i)
            assert isinstance(value, str)
            assert len(value) <= 15
            assert len(value) > 0  # Should not be empty


class TestUtilityFunctions:
    def test_get_random_words(self):
        words = get_random_words(5, 10)
        
        assert len(words) == 5  
        for word in words:
            assert isinstance(word, str)
            assert len(word) <= 10
    
    def test_get_random_words_short_length(self):
        words = get_random_words(3, 1)
        
        assert len(words) == 3
        for word in words:
            assert len(word) <= 1
    
    def test_set_upper_with_value(self):
        result = set_upper(100, "int")
        assert result == 100
        
        result = set_upper(50.5, "double")
        assert result == 50.5
    
    def test_set_upper_without_value_int(self):
        result = set_upper(None, "int")
        assert 47 <= result <= 99
    
    def test_set_upper_without_value_uint(self):
        result = set_upper(None, "uint")
        assert 80 <= result <= 128
    
    def test_set_upper_without_value_double(self):
        result = set_upper(None, "double")
        assert 47 <= result <= 102
    
    def test_set_lower_with_value(self):
        result = set_lower(10, "int")
        assert result == 10
        
        result = set_lower(-5.5, "double")
        assert result == -5.5
    
    def test_set_lower_without_value_int(self):
        result = set_lower(None, "int")
        assert -99 <= result <= -47
    
    def test_set_lower_without_value_uint(self):
        result = set_lower(None, "uint")
        assert 0 <= result <= 13
    
    def test_set_lower_without_value_double(self):
        result = set_lower(None, "double")
        assert -102 <= result <= -47


class TestTypeMappings:
    
    def test_type_mappings_structure(self):
        assert "int" in TYPE_MAPPINGS
        assert "uint" in TYPE_MAPPINGS
        assert "double" in TYPE_MAPPINGS
        assert "str" in TYPE_MAPPINGS
        
        for type_name, mapping in TYPE_MAPPINGS.items():
            assert "ctype" in mapping
            assert "mem_size" in mapping
    
    def test_type_mappings_memory_sizes(self):
        assert TYPE_MAPPINGS["int"]["mem_size"] == 4
        assert TYPE_MAPPINGS["uint"]["mem_size"] == 4
        assert TYPE_MAPPINGS["double"]["mem_size"] == 8
        assert TYPE_MAPPINGS["str"]["mem_size"] == 0


# Integration tests
class TestArrayIntegration:
    
    def test_array_full_workflow_int(self):
    
        arr = Array("int", 5)
        arr.set_index(0, 10)
        arr.set_index(1, 20)
        arr.set_index(2, 30)
        arr.set_index(3, 40)
        arr.set_index(4, 50)
        
        assert arr.linear_search(30) == "30 found at index: 2"
        assert arr.linear_search(99) == "99 not found"
        
        assert arr.get_index_data(0) == 10
        assert arr.get_index_data(4) == 50
    
    def test_array_full_workflow_string(self):
        arr = Array("str", 4, max_str_length=8)
        
        arr.set_index(0, "apple")
        arr.set_index(1, "banana")
        arr.set_index(2, "cherry")
        arr.set_index(3, "date")
        
        assert arr.linear_search("banana") == "banana found at index: 1"
        assert arr.linear_search("grape") == "grape not found"
    
        assert arr.get_index_data(0) == "apple"
        assert arr.get_index_data(3) == "date"
    
    def test_array_populate_and_search(self):
        arr = Array("int", 10)
        arr.populate(lower_bound=1, upper_bound=100)
        
        test_value = arr.get_index_data(5)
        result = arr.linear_search(test_value)
        assert f"{test_value} found at index: 5" == result
