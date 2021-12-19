MAX_HASH_TABLE_SIZE = 4096
# List of size MAX_HASH_TABLE_SIZE with all values None
#data_list = [None]*MAX_HASH_TABLE_SIZE

"""
Hashing Function
A hashing function is used to convert strings and other non-numeric data types into numbers, 
which can then be used as list indices. 
For instance, if a hashing function converts the string "Aakash" into the number 4, 
then the key-value pair ('Aakash', '7878787878') will be stored at the position 4 within the data list.

Here's a simple algorithm for hashing, which can convert strings into numeric list indices.

1.Iterate over the string, character by character
2.Convert each character to a number using Python's built-in ord function.
3.Add the numbers for each character to obtain the hash for the entire string
4.Take the remainder of the result with the size of the data list
"""
def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = sum(ord(a_character) for a_character in a_string)

    return result % len(data_list)


def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv is None:
            return idx

        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx

        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0


class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None]*max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]

    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]
class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None]*max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        if kv is None:
            return None
        key, value = kv
        return value

    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]


basic_table = BasicHashTable(max_size=1024)
print(len(basic_table.data_list) == 1024)
# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')
# Find a value
print(basic_table.find('Hemanth') == '8888888888')


# Create an empty hash table
data_list2 = [None] * MAX_HASH_TABLE_SIZE

# New key 'listen' should return expected index
get_valid_index(data_list2, 'listen') == 655
# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, 'listen')] = ('listen', 99)

# Colliding key 'silent' should return next index
get_valid_index(data_list2, 'silent') == 656


# Create a new hash table
probing_table = ProbingHashTable()

# Insert a value
probing_table.insert('listen', 99)

# Check the value
probing_table.find('listen') == 99

# Insert a colliding key
probing_table.insert('silent', 200)

# Check the new and old keys
probing_table.find('listen') == 99 and probing_table.find('silent') == 200

# Update a key
probing_table.insert('listen', 101)

# Check the value
probing_table.find('listen') == 101
