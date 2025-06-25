# Structure Visualizer
This is a data structures visualizer project. The visualizers file is more crammed than I'd like it to be, but it's so I can provide context with less files.

It started as a way for me to use the DSA notes that had been sitting on my computer from my old class. The linked list implementation is... controversial. Blame it on my textbook.

To clear up confusion:
- None checks are generally for the *head node* not for the tail pointer. 
- Most LL methods support using vals *or* premade node objects, so there's some extra clean up that usually would be done by the garbage collector.

More info on the array class [here](#structure)

### Setup
1. Create and activate venv: 
    - MacOS/Linux: `python -m venv .venv && source .venv/bin/activate`
    - Windows: `python -m venv .venv && .venv\Scripts\activate`
2. Install dependencies: `pip install -r requirements.txt`

*Make sure to run everything from the root directory!! The whole project structure falls apart if you don't :)*

### Structure
``` 
.
.
├── __init__.py
├── __pycache__
│   └── QueueVisualizer.cpython-313.pyc
├── ArrayVisualizer.py
├── notes
│   ├── data_structures
│   │   ├── adts.md
│   │   ├── arrays.md
│   │   ├── binary_tree.md
│   │   ├── data_structures.md
│   │   ├── graphs.md
│   │   ├── hash_tables.md
│   │   ├── heap.md
│   │   └── linked_lists.md
│   ├── explains_algorithms.md
│   ├── images
│   │   ├── bigO_compChart.png
│   │   └── bigO_operations.jpeg
│   ├── logarithms.md
│   ├── search_and_sort
│   │   ├── search.md
│   │   └── sort.md
│   └── time_complexity
│       └── time_complexity.md
├── QueueVisualizer.py
├── README.md
├── src
│   ├── models
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── _array.cpython-313.pyc
│   │   │   ├── doublyLL.cpython-313.pyc
│   │   │   ├── queue.cpython-313.pyc
│   │   │   ├── singly_LL.cpython-313.pyc
│   │   │   └── stack.cpython-313.pyc
│   │   ├── _array.py
│   │   ├── deque.py
│   │   ├── doublyLL.py
│   │   ├── queue.py
│   │   ├── singly_LL.py
│   │   └── stack.py
│   └── search_sort
│       ├── __init__.py
│       ├── binary_search.py
│       ├── insertion_sort.py
│       ├── merge_sort.py
│       ├── quicksort.py
│       ├── selection_sort.py
│       ├── shell_sort.py
└── tests
    ├── __init__.py
    ├── test_array.py
    ├── test_linked_lists.py
    └── test_sorted.py
```
**Notes**:
- `__init__.py`: All empty. Please make sure these remain intact inside every subdirectory and on the root level. The codebase **will not work** otherwise.
- `src/models/_array.py`: Python implementation of a *fixed-type*, *fixed-length* array, using the `ctypes` module. There are The actual, accessible array is found in the attribute `self.memory`. It is NOT dynamic and it IS NOT a Python `list` and therefore it cannot use Python list methods. It can ONLY use the methods created in the class.
- `src/search_sort.py`: Contains `binary_search`, `selection_sort`, `insertion_sort`, `shell_sort`, `quicksort`, and `merge_sort` functions (and utility functions, i.e., `partition`).
- `visualizer.py`: Contains the queue and array terminal based visualizers that rely on the `colorama` module for cross-platform colored terminal text.

### Troubleshooting
- If you see strange characters instead of colors (e.g., ][0m [), make sure your terminal supports ANSI.
    - If you're running the code in the `Output` tab, try running it in a dedicated terminal.
    -If you're on Windows and having issues, try running `python -m colorama.init()`