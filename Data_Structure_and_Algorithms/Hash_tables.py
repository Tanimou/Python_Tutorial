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
