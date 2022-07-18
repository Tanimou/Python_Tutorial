from Tree import TreeNode
"""
QUESTION 1: As a senior backend engineer, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

1.Insert the profile information for a new user.
2.Find the profile information of a user, given their username
3.Update the profile information of a user, given their usrname
4.List all the users of the platform, sorted by username

You can assume that usernames are unique.
"""
# *A Python class would be a great way to represent the information for a user


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(
            guest_name, self.name, self.email))


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

# *We can also express our desired data structure as a Python class UserDatabase
# *with four methods: insert, find, update and list_all.
"""
The various functions can be implemented as follows:

1.Insert: Loop through the list and add the new user at a position that keeps the list sorted.
2.Find: Loop through the list and find the user object with the username matching the query.
3.Update: Loop through the list, find the user object matching the query and update the details
4.List: Return the list of user objects.
"""


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
            # Find the first username greater than the new user's username
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


database = UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

#user = database.find('siddhant')
#print(user)
#print()
#print(database.list_all())
#print()
# *Let's verify that a new user is inserted into the correct position.
#database.insert(biraj)
#print(database.list_all())

"""
It takes almost 10 seconds to execute all the iterations in the above cell.

A 10-second delay for fetching user profiles will lead to a suboptimal users experience 
and may cause many users to stop using the platform altogether.

The 10-second processing time for each profile request will also significantly 
limit the number of users that can access the platform at a time or increase the cloud 
infrastructure costs for the company by millions of dollars.

As a senior backend engineer, you must come up with a more efficient data structure! 
Choosing the right data structure for the requirements at hand is an important skill. 
It's apparent that a sorted list of users might not be the best data structure to organize profile information for millions of users.

We can limit the number of iterations required for common operations like find, insert 
and update by organizing our data in the following structure, called a BINARY TREE (see Tree.py)

For our use case, we require the binary tree to have some additional properties:

1.Keys and Values: Each node of the tree stores a key (a username) and a value (a User object). Only keys are shown for brevity.
A binary tree where nodes have both a key and a value is often referred to as a map or treemap (because it maps keys to values).

2.Binary Search Tree: The left subtree of any node only contains nodes with keys that are lexicographically smaller than the node's key,
and the right subtree of any node only contains nodes with keys that lexicographically larger than the node's key. A tree that satisfies this property is called a binary search trees, 
and it's easy to locate a specific key by traversing a single path down from the root note.

3.Balanced Tree: The tree is balanced i.e. it does not skew too heavily to one side or the other. The left and right subtrees of any node shouldn't differ in height/depth by more than 1 level
"""

#!Binary search Tree or BST
# Binary Search Tree (BST)
'''
A binary search tree or BST is a binary tree that satisfies the following conditions:

1. The left subtree of any node only contains nodes with keys less than the node's key
2. The right subtree of any node only contains nodes with keys greater than the node's key

It follows from the above conditions that every subtree of a binary search tree must also be a binary search tree.
'''
#!check if a tree is a binary search tree and give us the min and max values of the tree


def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    #*base case
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    #*if is_bst_l exists and is_bst_r exists and
    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key


tree2 = TreeNode.parse_tuple(
    (('aakash', 'biraj', 'hemanth'), 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))

print(is_bst(tree2))

#! Storing Key-Value Pairs using BSTs
#*Recall that we need to store user objects with each key in our BST. Let's define new class `BSTNode` to represent the nodes of of our tree.
#*Apart from having properties `key`, `left` and `right`, we'll also store a `value` and pointer to the parent node(for easier upward traversal).
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
    """
    ### Insertion into BST

    We use the BST-property to perform insertion efficiently: 

    1. Starting from the root node, we compare the key to be inserted with the current node's key
    2. If the key is smaller, we recursively insert it in the left subtree (if it exists) or attach it as as the left child if no left subtree exists.
    3. If the key is larger, we recursively insert it in the right subtree (if it exists) or attach it as as the right child if no right subtree exists.

    Here's a recursive implementation of `insert`.
    """
    def insert(self, key, value):
        if self is None:
            self = BSTNode(key, value)
        elif key < self.key:
            self.left = BSTNode.insert(self.left, key, value)
            self.left.parent = self
        elif key > self.key:
            self.right = BSTNode.insert(self.right, key, value)
            self.right.parent = self
        return self
    
    def find(self, key):
        if self is None:
            return None
        if key == self.key:
            return self
        if key < self.key:
            return BSTNode.find(self.left, key)
        if key > self.key:
            return BSTNode.find(self.right, key)

    def update(self, key, value):
        target = BSTNode.find(self, key)
        if target is not None:
            target.value = value
            
    """
    ### List the nodes

    Write a function to retrieve all the key-values pairs stored in a BST in the sorted order of keys.

    The nodes can be listed in sorted order by performing an inorder traversal of the BST.
    """
    def list_all(self):
        if self is None:
            return []
        return BSTNode.list_all(self.left) + [(self.key, self.value)] + BSTNode.list_all(self.right)
    
    
'''
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node
''' 

'''
def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
''' 
    
# *let's use this to recreate our tree
# *to recreate the first node, we can use the insert function with None as the target tree
tree = BSTNode.insert(None, jadhesh.username, jadhesh)
tree.insert( biraj.username, biraj)
tree.insert( sonaksh.username, sonaksh)
tree.insert( aakash.username, aakash)
tree.insert(hemanth.username, hemanth)
tree.insert( siddhant.username, siddhant)
tree.insert( vishal.username, vishal)
#TreeNode.display_tree(tree, "   ")
#found=tree.find("hemanth")
#found=find(tree, "hemanth")
#print(found.key,found.value)
#tree.update('hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
#found = tree.find("hemanth")
#print(found.key, found.value)
#print(tree.list_all())

#!Balanced Binary Tree
#*return true/false if the binary tree is balanced or not and return the heigh of the tree
def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
   # height =TreeNode.height(node)
    return balanced, height

#print(is_balanced(tree))
#tree.insert("tanya",User("tanya","Tanya JJ","tanyajj@example.com"))
#print(is_balanced(tree))
#print(tree.list_all())
#TreeNode.display_tree(tree, "   ")

#*make a balanced bst
"""
We can use a recursive strategy here, turning the middle element of the list into the root,
and recursively creating left and right subtrees.
"""

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)

    return root


data = [(user.username, user) for user in users]
tree = make_balanced_bst(data)
TreeNode.display_tree(tree, "   ")
