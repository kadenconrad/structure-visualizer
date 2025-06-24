import pytest
import sys
import os
from io import StringIO

from src.models._array import Array, get_random_words, set_upper, set_lower, TYPE_MAPPINGS


class TestArrayInitialization:
    """Test cases for Array class initialization"""
    
    def test_valid_int_array_creation(self):
        """Test creating a valid integer array"""
        arr = Array("int", 5)
        assert arr.array_type == "int"
        assert arr.size == 5
        assert arr.total_memory == 20  # 4 bytes * 5 elements
    
    def test_valid_uint_array_creation(self):
        """Test creating a valid unsigned integer array"""
        arr = Array("uint", 10)
        assert arr.array_type == "uint"
        assert arr.size == 10
        assert arr.total_memory == 40  # 4 bytes * 10 elements
    
    def test_valid_double_array_creation(self):
        """Test creating a valid double array"""
        arr = Array("double", 3)
        assert arr.array_type == "double"
        assert arr.size == 3
        assert arr.total_memory == 24  # 8 bytes * 3 elements
    
    def test_valid_string_array_creation(self):
        """Test creating a valid string array"""
        arr = Array("str", 5, max_str_length=10)
        assert arr.array_type == "str"
        assert arr.size == 5
        assert arr.str_arr_length == 11  # 10 + 1 for null terminator
        assert arr.total_memory == 55  # 11 * 5 elements
    
    def test_invalid_array_type(self):
        """Test creating array with invalid type"""
        with pytest.raises(ValueError, match="Please choose valid array type"):
            Array("invalid_type", 5)
    
    def test_invalid_size_zero(self):
        """Test creating array with size zero"""
        with pytest.raises(ValueError, match="Array size must be valid positive integer"):
            Array("int", 0)
    
    def test_invalid_size_negative(self):
        """Test creating array with negative size"""
        with pytest.raises(ValueError, match="Array size must be valid positive integer"):
            Array("int", -5)
    
    def test_invalid_size_non_integer(self):
        """Test creating array with non-integer size"""
        with pytest.raises(ValueError, match="Array size must be valid positive integer"):
            Array("int", 5.5)
    
    def test_string_array_without_max_length(self):
        """Test creating string array without specifying max string length"""
        with pytest.raises(ValueError, match="Must specify string length if declaring string array"):
            Array("str", 5)
    
    def test_string_array_with_zero_max_length(self):
        """Test creating string array with zero max length"""
        arr = Array("str", 3, max_str_length=0)
        assert arr.str_arr_length == 1  # 0 + 1 for null terminator


class TestArrayIndexAccess:
    """Test cases for getting and setting array values"""
    
    def test_get_index_int_array(self):
        """Test getting values from integer array"""
        arr = Array("int", 5)
        arr.set_index(0, 42)
        arr.set_index(2, 100)
        
        assert arr.get_index(0) == 42
        assert arr.get_index(2) == 100
        assert arr.get_index(1) == 0  # Default value
    
    def test_get_index_double_array(self):
        """Test getting values from double array"""
        arr = Array("double", 3)
        arr.set_index(0, 3.14)
        arr.set_index(1, -2.5)
        
        assert arr.get_index(0) == 3.14
        assert arr.get_index(1) == -2.5
    
    def test_get_index_string_array(self):
        """Test getting values from string array"""
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "hello")
        arr.set_index(1, "world")
        
        assert arr.get_index(0) == "hello"
        assert arr.get_index(1) == "world"
        assert arr.get_index(2) == ""  # Default empty string
    
    def test_set_index_int_array(self):
        """Test setting values in integer array"""
        arr = Array("int", 5)
        arr.set_index(0, 42)
        arr.set_index(4, -100)
        
        assert arr.get_index(0) == 42
        assert arr.get_index(4) == -100
    
    def test_set_index_string_array(self):
        """Test setting values in string array"""
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "test")
        arr.set_index(1, "python")
        arr.set_index(2, "array")
        
        assert arr.get_index(0) == "test"
        assert arr.get_index(1) == "python"
        assert arr.get_index(2) == "array"
    
    def test_get_index_out_of_bounds_positive(self):
        """Test getting index beyond array size"""
        arr = Array("int", 5)
        with pytest.raises(ValueError, match="Index out of bounds. Array size: 5"):
            arr.get_index(5)
    
    def test_get_index_out_of_bounds_negative(self):
        """Test getting negative index"""
        arr = Array("int", 5)
        with pytest.raises(ValueError, match="Index out of bounds. Array size: 5"):
            arr.get_index(-1)
    
    def test_set_index_out_of_bounds_positive(self):
        """Test setting index beyond array size"""
        arr = Array("int", 5)
        with pytest.raises(ValueError, match="Index out of bounds. Array size: 5"):
            arr.set_index(5, 42)
    
    def test_set_index_out_of_bounds_negative(self):
        """Test setting negative index"""
        arr = Array("int", 5)
        with pytest.raises(ValueError, match="Index out of bounds. Array size: 5"):
            arr.set_index(-1, 42)
    
    def test_set_string_too_long(self):
        """Test setting string that exceeds max length"""
        arr = Array("str", 3, max_str_length=5)
        with pytest.raises(ValueError, match="Value must be less than 6 characters"):
            arr.set_index(0, "this string is too long")
    
    def test_set_string_max_length(self):
        """Test setting string at exactly max length"""
        arr = Array("str", 2, max_str_length=5)
        arr.set_index(0, "12345")  # Exactly 5 characters
        assert arr.get_index(0) == "12345"


class TestArrayDisplay:
    """Test cases for display methods"""
    
    def test_display_int_array(self, capsys):
        """Test displaying integer array"""
        arr = Array("int", 3)
        arr.set_index(0, 1)
        arr.set_index(1, 2)
        arr.set_index(2, 3)
        
        arr.display()
        captured = capsys.readouterr()
        assert captured.out == "[1, 2, 3]\n"
    
    def test_display_double_array(self, capsys):
        """Test displaying double array"""
        arr = Array("double", 2)
        arr.set_index(0, 3.14)
        arr.set_index(1, 2.71)
        
        arr.display()
        captured = capsys.readouterr()
        assert captured.out == "[3.14, 2.71]\n"
    
    def test_display_string_array(self, capsys):
        """Test displaying string array"""
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "hello")
        arr.set_index(1, "world")
        arr.set_index(2, "test")
        
        arr.display()
        captured = capsys.readouterr()
        assert captured.out == "[hello, world, test]\n"
    
    def test_display_single_element(self, capsys):
        """Test displaying array with single element"""
        arr = Array("int", 1)
        arr.set_index(0, 42)
        
        arr.display()
        captured = capsys.readouterr()
        assert captured.out == "[42]\n"
    
    def test_reverse_traversal_int_array(self, capsys):
        """Test reverse traversal of integer array"""
        arr = Array("int", 3)
        arr.set_index(0, 1)
        arr.set_index(1, 2)
        arr.set_index(2, 3)
        
        arr.reverse_traversal()
        captured = capsys.readouterr()
        assert captured.out == "[3, 2, 1]\n"
    
    def test_reverse_traversal_string_array(self, capsys):
        """Test reverse traversal of string array"""
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "first")
        arr.set_index(1, "second")
        arr.set_index(2, "third")
        
        arr.reverse_traversal()
        captured = capsys.readouterr()
        assert captured.out == "[third, second, first]\n"
    
    def test_reverse_traversal_single_element(self, capsys):
        """Test reverse traversal with single element"""
        arr = Array("int", 1)
        arr.set_index(0, 42)
        
        arr.reverse_traversal()
        captured = capsys.readouterr()
        assert captured.out == "[42]\n"


class TestArraySearch:
    """Test cases for linear search functionality"""
    
    def test_linear_search_int_found(self):
        """Test linear search finding integer value"""
        arr = Array("int", 5)
        arr.set_index(0, 10)
        arr.set_index(1, 20)
        arr.set_index(2, 30)
        arr.set_index(3, 40)
        arr.set_index(4, 50)
        
        result = arr.linear_search(30)
        assert result == "30 found at index: 2"
    
    def test_linear_search_int_not_found(self):
        """Test linear search not finding integer value"""
        arr = Array("int", 3)
        arr.set_index(0, 10)
        arr.set_index(1, 20)
        arr.set_index(2, 30)
        
        result = arr.linear_search(99)
        assert result == "99 not found"
    
    def test_linear_search_double_found(self):
        """Test linear search finding double value"""
        arr = Array("double", 3)
        arr.set_index(0, 1.1)
        arr.set_index(1, 2.2)
        arr.set_index(2, 3.3)
        
        result = arr.linear_search(2.2)
        assert result == "2.2 found at index: 1"
    
    def test_linear_search_string_found(self):
        """Test linear search finding string value"""
        arr = Array("str", 4, max_str_length=10)
        arr.set_index(0, "apple")
        arr.set_index(1, "banana")
        arr.set_index(2, "cherry")
        arr.set_index(3, "date")
        
        result = arr.linear_search("cherry")
        assert result == "cherry found at index: 2"
    
    def test_linear_search_string_not_found(self):
        """Test linear search not finding string value"""
        arr = Array("str", 3, max_str_length=10)
        arr.set_index(0, "apple")
        arr.set_index(1, "banana")
        arr.set_index(2, "cherry")
        
        result = arr.linear_search("orange")
        assert result == "orange not found"
    
    def test_linear_search_first_element(self):
        """Test linear search finding first element"""
        arr = Array("int", 3)
        arr.set_index(0, 100)
        arr.set_index(1, 200)
        arr.set_index(2, 300)
        
        result = arr.linear_search(100)
        assert result == "100 found at index: 0"
    
    def test_linear_search_last_element(self):
        """Test linear search finding last element"""
        arr = Array("int", 3)
        arr.set_index(0, 100)
        arr.set_index(1, 200)
        arr.set_index(2, 300)
        
        result = arr.linear_search(300)
        assert result == "300 found at index: 2"


class TestArrayPopulate:
    """Test cases for array population functionality"""
    
    def test_populate_int_array(self):
        """Test populating integer array with random values"""
        arr = Array("int", 10)
        arr.populate()
        
        # Check that all values are set (not default 0)
        non_zero_count = sum(1 for i in range(arr.size) if arr.get_index(i) != 0)
        assert non_zero_count > 0  # At least some should be non-zero
    
    def test_populate_int_array_with_bounds(self):
        """Test populating integer array with specified bounds"""
        arr = Array("int", 5)
        arr.populate(lower_bound=10, upper_bound=20)
        
        # Check all values are within bounds
        for i in range(arr.size):
            value = arr.get_index(i)
            assert 10 <= value <= 20
    
    def test_populate_uint_array(self):
        """Test populating unsigned integer array"""
        arr = Array("uint", 5)
        arr.populate()
        
        # Check all values are non-negative
        for i in range(arr.size):
            value = arr.get_index(i)
            assert value >= 0
    
    def test_populate_double_array(self):
        """Test populating double array with random values"""
        arr = Array("double", 5)
        arr.populate()
        
        # Check that values are set and are floats
        for i in range(arr.size):
            value = arr.get_index(i)
            assert isinstance(value, float)
    
    def test_populate_double_array_with_bounds(self):
        """Test populating double array with specified bounds"""
        arr = Array("double", 3)
        arr.populate(lower_bound=1.0, upper_bound=5.0)
        
        # Check all values are within bounds
        for i in range(arr.size):
            value = arr.get_index(i)
            assert 1.0 <= value <= 5.0
    
    def test_populate_string_array(self):
        """Test populating string array with random words"""
        arr = Array("str", 5, max_str_length=15)
        arr.populate()
        
        # Check that strings are set and within length limits
        for i in range(arr.size):
            value = arr.get_index(i)
            assert isinstance(value, str)
            assert len(value) <= 15
            assert len(value) > 0  # Should not be empty


class TestUtilityFunctions:
    """Test cases for utility functions"""
    
    def test_get_random_words(self):
        """Test getting random words"""
        words = get_random_words(5, 10)
        
        assert len(words) == 5  
        for word in words:
            assert isinstance(word, str)
            assert len(word) <= 10
    
    def test_get_random_words_short_length(self):
        """Test getting random words with very short max length"""
        words = get_random_words(3, 1)
        
        assert len(words) == 3
        for word in words:
            assert len(word) <= 1
    
    def test_set_upper_with_value(self):
        """Test set_upper when upper bound is provided"""
        result = set_upper(100, "int")
        assert result == 100
        
        result = set_upper(50.5, "double")
        assert result == 50.5
    
    def test_set_upper_without_value_int(self):
        """Test set_upper when no upper bound provided for int"""
        result = set_upper(None, "int")
        assert 47 <= result <= 99
    
    def test_set_upper_without_value_uint(self):
        """Test set_upper when no upper bound provided for uint"""
        result = set_upper(None, "uint")
        assert 80 <= result <= 128
    
    def test_set_upper_without_value_double(self):
        """Test set_upper when no upper bound provided for double"""
        result = set_upper(None, "double")
        assert 47 <= result <= 102
    
    def test_set_lower_with_value(self):
        """Test set_lower when lower bound is provided"""
        result = set_lower(10, "int")
        assert result == 10
        
        result = set_lower(-5.5, "double")
        assert result == -5.5
    
    def test_set_lower_without_value_int(self):
        """Test set_lower when no lower bound provided for int"""
        result = set_lower(None, "int")
        assert -99 <= result <= -47
    
    def test_set_lower_without_value_uint(self):
        """Test set_lower when no lower bound provided for uint"""
        result = set_lower(None, "uint")
        assert 0 <= result <= 13
    
    def test_set_lower_without_value_double(self):
        """Test set_lower when no lower bound provided for double"""
        result = set_lower(None, "double")
        assert -102 <= result <= -47


class TestTypeMappings:
    """Test cases for type mappings constant"""
    
    def test_type_mappings_structure(self):
        """Test that TYPE_MAPPINGS has expected structure"""
        assert "int" in TYPE_MAPPINGS
        assert "uint" in TYPE_MAPPINGS
        assert "double" in TYPE_MAPPINGS
        assert "str" in TYPE_MAPPINGS
        
        for type_name, mapping in TYPE_MAPPINGS.items():
            assert "ctype" in mapping
            assert "mem_size" in mapping
    
    def test_type_mappings_memory_sizes(self):
        """Test that memory sizes are correct"""
        assert TYPE_MAPPINGS["int"]["mem_size"] == 4
        assert TYPE_MAPPINGS["uint"]["mem_size"] == 4
        assert TYPE_MAPPINGS["double"]["mem_size"] == 8
        assert TYPE_MAPPINGS["str"]["mem_size"] == 0


# Integration tests
class TestArrayIntegration:
    """Integration tests combining multiple operations"""
    
    def test_array_full_workflow_int(self):
        """Test complete workflow with integer array"""
        # Create array
        arr = Array("int", 5)
        
        # Set some values
        arr.set_index(0, 10)
        arr.set_index(1, 20)
        arr.set_index(2, 30)
        arr.set_index(3, 40)
        arr.set_index(4, 50)
        
        # Test search
        assert arr.linear_search(30) == "30 found at index: 2"
        assert arr.linear_search(99) == "99 not found"
        
        # Test get values
        assert arr.get_index(0) == 10
        assert arr.get_index(4) == 50
    
    def test_array_full_workflow_string(self):
        """Test complete workflow with string array"""
        # Create array
        arr = Array("str", 4, max_str_length=8)
        
        # Set values
        arr.set_index(0, "apple")
        arr.set_index(1, "banana")
        arr.set_index(2, "cherry")
        arr.set_index(3, "date")
        
        # Test search
        assert arr.linear_search("banana") == "banana found at index: 1"
        assert arr.linear_search("grape") == "grape not found"
        
        # Test get values
        assert arr.get_index(0) == "apple"
        assert arr.get_index(3) == "date"
    
    def test_array_populate_and_search(self):
        """Test populating array and then searching"""
        arr = Array("int", 10)
        arr.populate(lower_bound=1, upper_bound=100)
        
        # Pick a value and search for it
        test_value = arr.get_index(5)
        result = arr.linear_search(test_value)
        assert f"{test_value} found at index: 5" == result
