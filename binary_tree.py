
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

user = database.find('siddhant')
print(user)
print()
print(database.list_all())
print()
# *Let's verify that a new user is inserted into the correct position.
database.insert(biraj)
print(database.list_all())

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
and update by organizing our data in the following structure, called a BINARY TREE
"""


class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    #!Height of a binary tree
    # *The height/depth of a binary tree is defined as the length of the longest path from its root node to a leaf.
    # *It can be computed recursively, as follows:

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    #!size of a binary tree
    # *it's the number of node in a tree
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    #!traversing a binary tree
    # *Inorder traversal:
    # *1.Traverse the left subtree recursively inorder.
    # *2.Traverse the current node.
    # *3.Traverse the right subtree recursively inorder.
    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +
                [self.key] +
                TreeNode.traverse_in_order(self.right))

    #!traversing a binary tree
    # *Preorder traversal:
    # *1.Traverse the current node.
    # *2.Traverse the left subtree recursively preorder.
    # *3.Traverse the right subtree recursively preorder.
    def traverse_pre_order(self):
        if self is None:
            return []
        return ([self.key] +
                TreeNode.traverse_pre_order(self.left) +
                TreeNode.traverse_pre_order(self.right))

    #!traversing a binary tree
    # *Postorder traversal:
    # *1.Traverse the right subtree recursively postorder.
    # *2.Traverse the current node.
    # *3.Traverse the left subtree recursively postorder.
    def traverse_post_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_post_order(self.right) +
                [self.key] +
                TreeNode.traverse_post_order(self.left))

    #!display the tree
    def display_tree(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return
        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
        # If the node has children
        TreeNode.display_tree(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_tree(self.left, space, level+1)

    #!convert a binary tree into tuple
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)

    #!convert a tuple into binary tree
    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

    def InsertNode(self, data):
        # *base case
        if self is None:
            return TreeNode(data)
        # *small amount of work in each iteration
        if(self.key < data):
            self.right = TreeNode.InsertNode(self.right, data)
        else:
            self.left = TreeNode.InsertNode(self.left, data)
        return self

    def find(self, key):
        if self is None:
            return None
        if key == self.key:
            return self
        if key < self.key:
            return TreeNode.find(self.left, key)
        if key > self.key:
            return TreeNode.find(self.right, key)
        
# *we can represent a binary tree to a tuple
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


'''
def tuple_to_tree(data):
   # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = tuple_to_tree(data[0])
        node.right = tuple_to_tree(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = tuple_to_tree(tree_tuple)
'''
print()
tree2 = TreeNode.parse_tuple(tree_tuple)


'''
def tree_to_tuple(node):
    tree_left = None if node.left is None else tree_to_tuple(node.left)
    tree_right = None if node.right is None else tree_to_tuple(node.right)

    if tree_left is None and tree_right is None:
        return node.key
    else:
       return (tree_left, node.key,tree_right)
print(tree_to_tuple(tree2))
'''
print()
print(tree2.to_tuple())


'''
def display_tree(node, space='\t', level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    # If the node has children
    display_tree(node.right, space, level+1)
    print(space*level + str(node.key))
    display_tree(node.left, space, level+1)
display_tree(tree2," ")
'''
print()
#TreeNode.display_tree(tree2, " ")
tree2.display_tree(" ")
'''
def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] +
           traverse_in_order(node.right))
print(traverse_in_order(tree2))
'''
print()
print(tree2.traverse_in_order())

'''
def traverse_pre_order(node):
    if node is None:
        return []
    return( [node.key] +
            traverse_pre_order(node.left) +
           traverse_pre_order(node.right))
print(traverse_pre_order(tree2))
'''


'''
def traverse_post_order(node):
    if node is None:
        return []
    return(traverse_post_order(node.right) +
           [node.key]  +
           traverse_post_order(node.left))
print(traverse_post_order(tree2))
'''


'''
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
'''
print()
print(tree2.height())

'''
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
'''
print()
print(tree2.size())
tree3 = tree2.InsertNode(40)
tree3.display_tree(" ")


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
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

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
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
    """
    ### Insertion into BST

    Write a function to insert a new node into a BST.

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
            return TreeNode.find(self.left, key)
        if key > self.key:
            return TreeNode.find(self.right, key)

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
BSTNode.insert(tree, biraj.username, biraj)
BSTNode.insert(tree, sonaksh.username, sonaksh)
BSTNode.insert(tree, aakash.username, aakash)
BSTNode.insert(tree, hemanth.username, hemanth)
BSTNode.insert(tree, siddhant.username, siddhant)
BSTNode.insert(tree, vishal.username, siddhant)
TreeNode.display_tree(tree, "   ")
found=tree.find("hemanth")
#found=find(tree, "hemanth")
print(found.key,found.value)
tree.update('hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
found = tree.find("hemanth")
print(found.key, found.value)
print(tree.list_all())