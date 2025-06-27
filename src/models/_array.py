import ctypes
from typing import Optional, Any
from random import randint, uniform, choice
from time import sleep
from .utils import get_random_words, set_lower, set_upper

TYPE_MAPPINGS = {
    "int": {"ctype": ctypes.c_int, "mem_size": 4},
    "uint": {"ctype": ctypes.c_uint, "mem_size": 4},
    "double": {"ctype": ctypes.c_double, "mem_size": 8},
    "str": {"ctype": ctypes.c_char, "mem_size": 0},  # calculated by max_string_length
}


class Array:
    def __init__(
        self, array_type: str, size: int, max_str_length: Optional[int] = None
    ):
        if array_type not in list(TYPE_MAPPINGS.keys()):
            raise ValueError(
                f"Please choose valid array type: {", ".join(list(TYPE_MAPPINGS.keys()))}"
            )
        self.array_type = array_type
        if not size or isinstance(size, int) != True or size < 0:
            raise ValueError(f"Array size must be valid positive integer")
        self.size = size

        if self.array_type == "str":
            if max_str_length == None:
                raise ValueError("Must specify string length if declaring string array")
            self.str_arr_length = max_str_length + 1  # For final null terminator
            self.total_memory = size * (self.str_arr_length)
            self.ctype = ctypes.c_char * (self.str_arr_length)
        else:
            self.total_memory = TYPE_MAPPINGS[self.array_type]["mem_size"] * size
            self.ctype = TYPE_MAPPINGS[array_type]["ctype"]
        self.memory = (self.ctype * size)()  # allocates memory
        self.memory_pointer = ctypes.pointer(self.memory)

    def get_index_data(self, index):
        if index >= self.size or index < 0:
            raise ValueError(f"Index out of bounds. Array size: {self.size}")
        if self.array_type == "str":
            return self.memory[index].value.decode("utf-8")
        return self.memory[index]

    def set_index(self, index, data):
        if index >= self.size or index < 0:
            raise ValueError(f"Index out of bounds. Array size: {self.size}")
        if self.array_type == "str":
            if len(data) > self.str_arr_length - 1:
                raise ValueError(
                    f"Value must be less than {self.str_arr_length} characters."
                )

            value_array = ctypes.create_string_buffer(
                data.encode("utf-8"), self.str_arr_length
            )
            self.memory[index] = value_array
        else:
            self.memory[index] = data

    def insert(self, index, data):
        """Overwrites last element because of fixed size"""
        if index >= self.size or index < 0:
            raise ValueError(f"Index out of bounds. Array size: {self.size}")
        if self.array_type == "str":
            if len(data) > self.str_arr_length - 1:
                raise ValueError(
                    f"Value must be less than {self.str_arr_length} characters."
                )

        for i in range(self.size - 1, index, -1):
            self.memory[i] = self.memory[i - 1]

        if self.array_type == "str":
            value_arr = ctypes.create_string_buffer(
                data.encode("utf-8"), self.str_arr_length
            )
            self.memory[index] = value_arr
        else:
            self.memory[index] = data

    def display(self, sleep_time=0.5):
        print("[", end="")
        if self.array_type == "str":
            for i in range(self.size):
                print(self.memory[i].value.decode("utf-8"), end="")
                if i != self.size - 1:
                    print(", ", end="")
                    if sleep_time:
                        sleep(sleep_time)
        else:
            for i in range(self.size):
                print(self.memory[i], end="")
                if i != self.size - 1:
                    print(", ", end="")
                    if sleep_time:
                        sleep(sleep_time)
        print("]")

    def reverse_traversal(self, sleep_time=0.5):
        print("[", end="")
        if self.array_type == "str":
            for i in range(self.size - 1, -1, -1):
                print(self.memory[i].value.decode("utf-8"), end="")
                if i != 0:
                    print(", ", end="")
                    if sleep_time:
                        sleep(sleep_time)
        else:
            for i in range(self.size - 1, -1, -1):
                print(self.memory[i], end="")
                if i != 0:
                    print(", ", end="")
                    if sleep_time:
                        sleep(sleep_time)
        print("]")

    def linear_search(self, target_value):
        if self.array_type == "str":
            for i in range(self.size):
                if self.memory[i].value.decode("utf-8") == target_value:
                    return f"{target_value} found at index: {i}"
            return f"{target_value} not found"

        else:
            for i in range(self.size):
                if self.memory[i] == target_value:
                    return f"{target_value} found at index: {i}"
            return f"{target_value} not found"

    def populate(self, lower_bound=None, upper_bound=None):
        if self.array_type == "str":
            word_list = get_random_words(self.size, self.str_arr_length - 1)
            for i in range(self.size):
                self.set_index(i, word_list[i])
        else:
            lower_bound = set_lower(lower_bound, self.array_type)
            upper_bound = set_upper(upper_bound, self.array_type)
            if self.array_type == "int" or self.array_type == "uint":
                for i in range(self.size):
                    self.set_index(i, randint(lower_bound, upper_bound))
            if self.array_type == "double":
                for i in range(self.size):

                    self.set_index(i, round(uniform(lower_bound, upper_bound), 3))