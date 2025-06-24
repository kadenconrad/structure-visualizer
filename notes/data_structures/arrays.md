# Arrays
## Prelude: The Basic Memory Model
The **fundamental array** behind data structures. When computers need to store data, it asks the operating system for unique bytes (4 integers; i.e., 1001, 1002, 1003, etc.) and the OS provides a range of addresses.

### Traditional Array Memory Allocation
1. **Size Calculation**: Calculates how much space is needed; for an array of five 4byte integers, you need 5*4=20 bytes total.
2. **Contiguous Allocation**: OS finds 20 *consecutive* addresses in memory. There can be **no** gaps.
3. **Base Address Storage**: The array variable stores just the first elements address as a pointer.
4. **Index Mathematics**: To find element 3, the system calculates: $baseAddress + (index \cdot elementSize) = 1000 + (3 \cdot  4) = 1012$ and can go directly to the address.