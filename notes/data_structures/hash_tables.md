## Hash Table
Data structure used to quickly insert, look up, and remove key-value pairs quickly, using *hashing*, where each key is translated by a hash function into a distinct index in an array. **Unique keys are required.**

One common hash function: $key \% n = b$. For example, given an array with indices 0 - 9, if storing the integer 25, it would use the function $25 \% 10 = 5$. If storing the integer 149, it would use the hash function $149 \% 10 = 9$. Since arithmetic functions are in constant time *O(n)*, so is searching a hash table. 

A 100 element hash table has 100 buckets. Hash tables are **not** designed to be filled to maximum capacity, as this increases the risk of *Hash Collisions*. This is easy to imagine – if we're given a 10 element array, any element with the same value in the ones place has the same hash value: $19 \% 10 = 9$, $29 \% 10 = 9$, $39 \% 10 = 9$, etc.

*n = number of elements and b = bucket the element is hashed into*

### Hash Collisions
When an item being inserted into the table has the same value as an element that is already in the table.

- **Chaining**: Each bucket has a list (or linked list) of items; not ideal because it defeats the purpose of a hash table, but an easy way. Usually means there's a bad hash function. *Hash tables using chaining can have a load factor above one.*

    - **Insert**: Checks if the hash table already has the same key in the table, creates new node, and appends node to initialized bucket list with the appropriate hash value.
    - **Search**: Searches list (with linked list search) for item node data or returns null
    - **Remove**: Uses list search to find item data and list remove.

- **Open Addressing**: Looks for an empty bucket in the hash table
    - **Linear probing**: Looks for an empty bucket linearly through the hash table. Differentiates empty-after-removal buckets from empty-since-start buckets. 
        - *Implementation*: While bucket is not empty-since-start and bucketsProbed is < N, *if the hash table[bucket] is not Empty and the key isn't == the key we are trying to place* ***this would mean we have placed the key and should return the hash table bucket***, increment the bucket by (bucket + 1 % n) and number of buckets probed by + 1. Return null if a bucket is not found.
    - **Quadratic probing**: Starts at the key's mapped bucket and quadratically searches subsequent buckets until an empty bucket is found. If $H$ = the mapped bucket, the formula $(H + c1 * i + c2 * i^2) \% (tablesize)$ to determine the item's index. `c1` and `c2` are programmer-defined constants.
    - **Double Hashing**: Uses two different hash functions to compute bucket indices. $(h1(key) + i * h2(key) \% (tablesize))$. Each time an empty bucket is not found, i is incremented by 1. 

**Load Factor**: As a hash table reaches maximum capacity, it's load factor increases. The load factor can be calculated . The higher the load factor, the higher the risk of collision, i.e., when multiple keys have the same hash value. Once load factor reaches over 0.75%, the table is generally dynamically resized.


### Hash table resizing
Increases the number of buckets while preserving all existing items. Hash table with N buckets is generally resized to the next prime number >= N * 2. 

### Direct Hashing
Uses the element's key as the bucket index, which prevents collisions, but the item must be a non-negative integer *(may be negative in some implementations)* and the hash table's size must equal the largest key's size + 1.

### Cryptography
- **Encryption**: Alteration of data to hide the original meaning
- **Decryption**: Reconstruction of data from encrypted data

- **Caesar Cipher**: Shifts characters in the alphabet to encrypt a message, i.e., with a right shift of 4, the character 'N' is shifted to 'R'. Uses ASCII codes to shift spaces and end alphabet characters, i.e., 'w' becomes '{'. The caeser cipher is extremely easy to decrypt, so it's not secure.

### Modern Hashing functions
- **MD5**: Produces a 128-bit hash value for any input data. It cannot be used to reconstruct the original data, but it can help verify that the data isn't corrupt and hasn't been altered. 

- **Cryptographic hashing function**: Specifically for cryptography, such as for encrypting and decrypting data

- **Password hashing function**: Produces a hash value for a password; databases often store passwords as a hash value instead of the actual password. When the user attempts to login, the password they type is hashed, and the hash is compared with the one in the database. This is in case a database is breached, so that hackers may still have a difficult time determining the user's password. 