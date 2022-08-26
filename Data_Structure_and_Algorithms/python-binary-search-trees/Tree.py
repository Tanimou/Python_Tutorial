"""
The word "binary" indicates that each "node" in the tree can have at most 2 children (left or right).
Nodes can have 0, 1 or 2 children. Nodes that do not have any children are sometimes also called "leaves".
The single node at the top is called the "root" node, and it typically where operations like search, insertion etc. begin.
"""
class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def __str__(self):
        return f"BinaryTree <{self.to_tuple()}>"

    def __repr__(self):
        return f"BinaryTree <{self.to_tuple()}>"
    #!Height of a binary tree
    # *The height/depth of a binary tree is defined as the length of the longest path from its root node to a leaf.
    # *It can be computed recursively, as follows:

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))  # type: ignore

    #!size of a binary tree
    # *it's the number of node in a tree
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)  # type: ignore

    #!traversing a binary tree
    # *Inorder traversal:
    # *1.Traverse the left subtree recursively inorder.
    # *2.Traverse the current node.
    # *3.Traverse the right subtree recursively inorder.
    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +  # type: ignore
                [self.key] +
                TreeNode.traverse_in_order(self.right))  # type: ignore

    #!traversing a binary tree
    # *Preorder traversal:
    # *1.Traverse the current node.
    # *2.Traverse the left subtree recursively preorder.
    # *3.Traverse the right subtree recursively preorder.
    def traverse_pre_order(self):
        if self is None:
            return []
        return ([self.key] +
                TreeNode.traverse_pre_order(self.left) +  # type: ignore
                TreeNode.traverse_pre_order(self.right))  # type: ignore

    #!traversing a binary tree
    # *Postorder traversal:
    # *1.Traverse the right subtree recursively postorder.
    # *2.Traverse the current node.
    # *3.Traverse the left subtree recursively postorder.
    def traverse_post_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_post_order(self.right) +  # type: ignore
                [self.key] +
                TreeNode.traverse_post_order(self.left))  # type: ignore

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
        TreeNode.display_tree(self.right, space, level+1)  # type: ignore
        print(space*level + str(self.key))
        TreeNode.display_tree(self.left, space, level+1)  # type: ignore

    #!convert a binary tree into tuple
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)  # type: ignore

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
            self.right = TreeNode.InsertNode(self.right, data)  # type: ignore
        else:
            self.left = TreeNode.InsertNode(self.left, data)  # type: ignore
        return self

    def find(self, key):
        if self is None:
            return None
        if key == self.key:
            return self
        if key < self.key:
            return TreeNode.find(self.left, key)  # type: ignore
        if key > self.key:
            return TreeNode.find(self.right, key)  # type: ignore


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
