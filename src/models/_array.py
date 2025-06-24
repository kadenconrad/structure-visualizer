import ctypes
from typing import Optional, Any
from random import randint, uniform, choice
from time import sleep

TYPE_MAPPINGS = {
    "int": { "ctype": ctypes.c_int, "mem_size": 4 },
    "uint": { "ctype": ctypes.c_uint, "mem_size": 4 },
    "double": { "ctype": ctypes.c_double, "mem_size": 8 },
    "str": { "ctype": ctypes.c_char, "mem_size": 0 } # calculated by max_string_length
        }

class Array:
    def __init__(self, array_type: str, size: int, max_str_length: Optional[int]=None):
        if array_type not in list(TYPE_MAPPINGS.keys()):
            raise ValueError(f"Please choose valid array type: {", ".join(list(TYPE_MAPPINGS.keys()))}")
        self.array_type = array_type
        if not size or isinstance(size, int) != True or size < 0:
            raise ValueError(f"Array size must be valid positive integer")
        self.size = size

        if self.array_type == "str":
            if max_str_length == None:
                raise ValueError("Must specify string length if declaring string array")
            self.str_arr_length = max_str_length + 1 # For final null terminator
            self.total_memory = size * (self.str_arr_length)
            self.ctype = ctypes.c_char * (self.str_arr_length) 
        else:
            self.total_memory = TYPE_MAPPINGS[self.array_type]["mem_size"] * size
            self.ctype = TYPE_MAPPINGS[array_type]["ctype"]
        self.memory = (self.ctype * size)() # allocates memory
        self.memory_pointer = ctypes.pointer(self.memory)
        

    def get_index_data(self, index):
        if index >= self.size or index < 0:
            raise ValueError(f"Index out of bounds. Array size: {self.size}")
        if self.array_type == "str":
            return self.memory[index].value.decode('utf-8')
        return self.memory[index]
    
    def set_index(self, index, data):
        if index >= self.size or index < 0:
            raise ValueError(f"Index out of bounds. Array size: {self.size}")
        if self.array_type == "str":
            if len(data) > self.str_arr_length - 1:
                raise ValueError(f"Value must be less than {self.str_arr_length} characters.")
            
            value_array = ctypes.create_string_buffer(data.encode("utf-8"), self.str_arr_length)
            self.memory[index] = value_array
        else:
            self.memory[index] = data

    def insert(self, index, data):
        """Overwrites last element because of fixed size"""
        if index >= self.size or index < 0:
            raise ValueError(f"Index out of bounds. Array size: {self.size}")
        if self.array_type == "str":
            if len(data) > self.str_arr_length - 1:
                raise ValueError(f"Value must be less than {self.str_arr_length} characters.")

        for i in range(self.size -1, index, -1):
            self.memory[i] = self.memory[i-1]

        if self.array_type == "str":
            value_arr = ctypes.create_string_buffer(data.encode("utf-8"), self.str_arr_length)
            self.memory[index] = value_arr
        else:
            self.memory[index] = data
    

    def display(self, sleep_time=0.5):
        print("[", end="")
        if self.array_type == "str":
            for i in range(self.size):
                print(self.memory[i].value.decode('utf-8'), end="")
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
            for i in range(self.size-1, -1, -1):
                print(self.memory[i].value.decode('utf-8'), end="")
                if i != 0:
                    print(", ", end="")
                    if sleep_time:
                        sleep(sleep_time)
        else:
            for i in range(self.size-1, -1, -1):
                print(self.memory[i], end="")
                if i != 0:
                    print(", ", end="") 
                    if sleep_time:
                        sleep(sleep_time)
        print("]")

    def linear_search(self, target_value):
        if self.array_type == "str":
            for i in range(self.size):
                if self.memory[i].value.decode('utf-8') == target_value:
                    return f"{target_value} found at index: {i}"
            return f"{target_value} not found"

        else:
            for i in range(self.size):
                if self.memory[i] == target_value:
                    return f"{target_value} found at index: {i}"
            return f"{target_value} not found"
        
    
    def populate(self, lower_bound=None, upper_bound=None):
        if self.array_type == "str":
            word_list = get_random_words(self.size, self.str_arr_length-1)
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
                    
# ---
""" UTILITY FUNCTIONS: get_random_words, set_upper, set_lower; all for populate method """
# ---
WORDS = ['notion', 'vote', 'python', 'ctypes', 'c', 'curl', 'linen', 'goal', 'fox', 'theorist', 'fuel', 'productive', 'delay', 'topple', 'settle', 'throw', 'support', 'charge', 'folk', 'apparatus', 'publisher', 'executive', 'plug', 'complain', 'quarrel', 'rocket', 'pray', 'warm', 'exempt', 'precision', 'spray', 'message', 'model', 'dealer', 'color', 'trick', 'bench', 'hospital', 'fan', 'contact', 'cousin', 'greeting', 'top', 'rise', 'waterfall', 'minute', 'courtesy', 'coalition', 'vote', 'abc', 'efg', 'u', 'hello', 'hi', 'hey', 'hola', 'guitar', 'code', 'foo', 'bar', 'susan', 'annie', 'john', 'josh', 'jake', 'kale', 'hash', 'array', 'class', 'function', 'annie', 'bart', 'glee', 'jump']
def get_random_words(n:int , max_length: int):
    """
    n: number of words to generate
    max_length: maximum length of each word
    """
    if max_length == 1:
        return [word[:max_length] for word in WORDS[:n]]
    if max_length == 0:
        raise ValueError("Max length must be greater than 0")
    
    word_list = set() # unique words
    seen = set()
    while len(word_list) < n:
        if len(seen) >= len(WORDS) // 2:
            break
        word = choice(WORDS)
        seen.add(word)
        if len(word) <= max_length:
            word_list.add(word)
    
    if len(word_list) != n:
        print(f"Warning: {len(word_list)} words generated, {n} words expected.")
    return list(word_list)


def set_upper(upper_bound: int | float | None, type: str):
    if upper_bound == None:
        if type == "int":
            return randint(47, 99)
        if type == "uint":
            return randint(80, 128)
        if type == "double":
            return uniform(47, 102)
    return upper_bound
        
def set_lower(lower_bound: int | float | None, type: str):
    if lower_bound == None:
        if type == "int":
            return randint(-99, -47)
        if type == "uint":
            return randint(0, 13)
        if type == "double":
            return uniform(-102,-47)
    return lower_bound