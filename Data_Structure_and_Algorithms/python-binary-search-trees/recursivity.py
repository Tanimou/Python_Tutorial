# https://www.youtube.com/watch?v=IJDJ0kBx2LM&list=PLyZB5ywlnsu9zio01i5zViNFqQunOxrw5&index=33&ab_channel=freeCodeCamp.org
# https: // www.youtube.com/watch?v = fAAZixBzIAI & list = PLyZB5ywlnsu9zio01i5zViNFqQunOxrw5 & index = 34 & ab_channel = freeCodeCamp.org
import math
from collections import deque

from Tree import TreeNode

#!strign reversal
# *input: the simple engineer
# *output:reenigne elpmis eht


def reverseString(input):
    # what is the base case?When can I no longer continue?
    # *one letter or empty string
    # what is the smallest amount of work I can do in each iteration,between each invocation
    # what is the small "unit" I can reverse?
    return "" if (input == "") else reverseString(input[1:])+input[0]

# print(reverseString("hello"))

#!palindrome
# *unique word where we can spell the same word forward and backward
# *Exple: kayak, racecar


def isPalindrome(input):
    # *define the base case/stopping condition
    if(len(input) == 0 | len(input) == 1):
        return True

    if (input[0] == input[len(input)-1]):
        return isPalindrome(input[1:-1])

    # *additional base case to handle non palindrome
    return False

# print(isPalindrome("racecar"))

#!number to binary

def NumberToBinary(num, result):
    if(num == 0):
        return result
    result = str(num % 2)+result
    return NumberToBinary(num//2, result)  # 123/10=12.3 while 123//10=12

# print(DecimalToBinary(233,""))

#!binary search

def binarySearch(A, left, right, x):
    if(left > right):
        return -1
    mid = (left+right)//2
    if(A[mid] == x):
        return mid
    elif x < A[mid]:
        return binarySearch(A, left, mid-1, x)
    else:
        return binarySearch(A, mid+1, right, x)

# print(binarySearch([-1,0,1,2,3,4,7,9,10,20],0,9,10))


'''
#!reverse a dll recursively
class node():
    def __init__(self,data=None):
        self.head=data
        self.next=None
        self.previous=None

n1=node(1)
n2=node(2)
n3=node(3)
n4=node(4)
n5=node(5)
n6=node(6)
n7=node(7)
n8=node(8)
n9=node(9)
n10=node(10)
n1.next=n2
n2.previous=n1
n2.next=n3
n3.previous=n2
n3.next=n4
n4.previous=n3
n4.next=n5
n5.previous=n4

n5.next=n6
n6.previous=n5
n6.next = n7
n7.previous = n6
n7.next = n8
n8.previous = n7
n8.next=n9
n9.previous=n8
n9.next = n10
n10.previous = n9


def reverseList(current,nodee):
    if(current.previous!=None):
        new_node=node(current.previous.head)
        nodee.next=new_node
        new_node.previous=nodee
        reverseList(current.previous,new_node)

def reverse(list):
    current=list.next
    
    while(current.next!=None):
        current=current.next
    rlist = node(current.head)
    reverseList(current,rlist)
    return rlist

def printlist(list):
    if list.next is None:
        print(list.head)
    if list.next!=None:
        print(list.head,"-> ",end="")
        printlist(list.next)
        
printlist(n1)
printlist(reverse(n1))
'''

#!reverse a single linked list recursively
class node():
    def __init__(self, data=None):
        self.head = data
        self.next = None


n1 = node(1)
n2 = node(8)
n3 = node(22)
n4 = node(40)

n5 = node(4)
n6 = node(11)
n7 = node(16)
n8 = node(20)
n1.next = n2  # type: ignore
n2.next = n3  # type: ignore
n3.next = n4  # type: ignore
n4.next = n5  # type: ignore
n5.next = n6  # type: ignore
n6.next = n7  # type: ignore
n7.next = n8  # type: ignore


def reverseList(node):
    if node.head is None or node.next is None:
        return node
    p = reverseList(node.next)
    print(node.head)
    node.next.next = node
    node.next = None
    return p

##another way of Recursion
def reverselistere2(head,prev=None):
    if head is None:
        return prev
    next=head.next
    head.next=prev
    return reverselistere2(next,head)

def printliste(list):
    if list.next is None:
        print(list.head)
    if list.next != None:
        print(list.head, "-> ", end="")
        printliste(list.next)


#printliste(n1)
#printliste(reverseList(n1))

##the iterative way
def reverselistee(node):
    prev=None
    current=node
    while current is not None:
        next=current.next
        current.next = prev
        prev=current
        current = next
    return prev

#printliste(n1)
#printliste(reverselistee(n1))
#!Summ of a list
#*a function that return the sum of a dll/sll
def sumlist(list):
    return 0 if list is None else list.head+sumlist(list.next)

#print(sumlist(n1))


#!Merge sort on single linked lists:
#*sort a sll using merge method
class Nodee():
    def __init__(self, data):
        self.head = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
    #*add new_value at the end of our single linked list

    def append(self, new_value):
        #allocate new node
        new_node = Nodee(new_value)

        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head

        while curr_node.next is not None:
            curr_node = curr_node.next

        # Append the new node at the end
        # of the linked list
        curr_node.next = new_node  # type: ignore
        
#!merge two sorted single linked lists
# *in a ordered way
#*this function merge 2 differents sorted single linked lists
def SortedMerge(a, b):

    if a is None:
        return b
    if b is None:
        return a
   # print("a:", a.head, "", "b:", b.head)
    if a.head < b.head:

        a.next = SortedMerge(a.next, b)
        return a
    else:
        #print("a:", a.head, "", "b:", b.head)
        b.next = SortedMerge(a, b.next)
        return b

#*transform a linked list (single or double) into a simple list


def transformlist(node):
    liste = []
    while(node is not None):
        liste.append(node.head)
        node = node.next
    return liste

 # Split a DLL or a SLL into two DLLs or SLLs
    # of half sizes


def split(tempHead):
    fast = slow = tempHead
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    temp = slow.next
    slow.next = None
    return temp


def mergeSort(liste):

     if isinstance(liste, list):
          liste0 = Linkedlist()
          for i in range(len(liste)):
               liste0.append(liste[i])
          tempHead = liste0.head
     else:
          tempHead = liste

     if tempHead is None or tempHead.next is None:
          return tempHead

     #*in order to use ourge merge function we need to split our ddl into 2 differents ddl
     second = split(tempHead)

      # Recur for left and right halves
     left = mergeSort(tempHead)
     right = mergeSort(second)
        # Merge the two sorted halves
     return SortedMerge(left, right)


printliste(n1)
list1 = transformlist(n1)
list00 = mergeSort(list1)
printliste(list00)


#!Merge sort on doubly linked list
# Program for merge sort on doubly linked list

# A node of the doubly linked list
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.head = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
    #*add new_data to the beginning of our ddl

    def push(self, new_data):
	# 1. Allocates node
	# 2. Put the data in it
        new_node = Node(new_data)

	# 3. Make next of new node as head and
	# previous as None (already None)
        new_node.next = self.head  # type: ignore

	# 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node  # type: ignore

	# 5. move the head to point to the new node
        self.head = new_node

# Function to merge two linked list


def merge(first, second):
    #*this is the same as our SortedMerge() function but since we're dealing with a double linked list
    #*we have to nullify the previous pointer like in the reverselist() function
        # If first linked list is empty
    if first is None:
         return second

          # If second linked list is empty
    if second is None:
         return first

          # Pick the smaller value
    if first.head < second.head:
         first.next = merge(first.next, second)
         first.next.prev = first
         first.prev = None
         return first
    else:
         second.next = merge(first, second.next)
         second.next.prev = second
         second.prev = None
         return second

# Function to do merge sort


def MSDList(liste):

      if isinstance(liste, list):
           liste0 = DoublyLinkedList()
           for i in range(len(liste)):
                liste0.push(liste[i])
           tempHead = liste0.head
      else:
           tempHead = liste

      if tempHead is None:
           return tempHead
      if tempHead.next is None:
           return tempHead
       #*in order to use ourge merge function we need to split our ddl into 2 differents ddl
      second = split(tempHead)

       # Recur for left and right halves
      tempHead = MSDList(tempHead)
      second = MSDList(second)
         # Merge the two sorted halves
      return merge(tempHead, second)


test0 = {
    'input': {
        'liste': [2, 4, 8, 10, 15]
    },
    'output': [2, 4, 8, 10, 15]
}
test1 = {
    'input': {
        'liste': [24, 4, 8, 150, 1]
    },
    'output': [1, 4, 8, 24, 150]
}
test2 = {
    'input': {
        'liste': []
    },
    'output': []
}
test3 = {
    'input': {
        'liste': [20, 4, 2, 10, 15]
    },
    'output': [2, 4, 10, 15, 20]
}
test4 = {
    'input': {
        'liste': [20, 15, 10, 4, 3]
    },
    'output': [3, 4, 10, 15, 20]
}


list0 = DoublyLinkedList()
list0.push(15)
list0.push(10)
list0.push(8)
list0.push(4)
list0.push(2)
printliste(list0.head)
sortedlist0 = transformlist(list0.head)
list00 = MSDList(sortedlist0)
printliste(list00)
print("sum:",sumlist(list0.head))

#!trees
# *Add a node in the tree recursively


def InsertNode(head, data):
    # *base case
    if head is None:
        head = TreeNode(data)
        return head
    # *small amount of work in each iteration
    if(head.key < data):
        head.right = InsertNode(head.right, data)
    else:
        head.left = InsertNode(head.left, data)
    return head


tree_tuple = (((30, 50, 60), 80, (85, 90, 95)), 100,
              ((None, 110, 115), 120, (None, 140, 15)))
tree2 = TreeNode.parse_tuple(tree_tuple)
#tree2.display_tree("  ")
print()
# tree3=InsertNode(tree2,108)
#tree3.display_tree("  ")
print()
#tree3 = InsertNode(tree2, 20)
#tree3.display_tree("  ")
print()
#tree3 = InsertNode(tree2, 135)
#tree3.display_tree("  ")
print()

# *print all leaf nodes


def printleaves(head):
    # *base case
    if head is None:
        return
    if head.left is None and head.right is None:
        print(head.key, ", ", end="")
        return
    # *small amount of work in each iteration
    if head.left is not None:
        printleaves(head.left)
    if head.right is not None:
        printleaves(head.right)

# printleaves(tree3)

#!Depth First Values
# *iterative way


def depthFirstValues(head):
    if head is None:
        return []
    result = []
    stacks = [head]
    while stacks:
        current = stacks.pop()
        result.append(current.key)

        if current.right is not None:
            stacks.append(current.right)
        if current.left is not None:
            stacks.append(current.left)
    return result


# print(depthFirstValues(tree2))
# print(tree2.traverse_pre_order())
# *recursive way


def depthFirstValuesRec(head):
    if head is None:
        return
    print(left_subtree := depthFirstValuesRec(head.left))

    print(right_subtree := depthFirstValuesRec(head.right))
    return [head.key, left_subtree, right_subtree]

# print(depthFirstValuesRec(tree2))

#!breadthFirstValues
# *iterative way, based on the FIFO concept
# *we treat the stack as a queue


def breadthFirstValues(head):
    if head is None:
        return []
    result = []
    stacks = deque([head])
    while stacks:
        current = stacks.popleft()
        result.append(current.key)

        if current.left is not None:
            stacks.append(current.left)

        if current.right is not None:
            stacks.append(current.right)

    return result

# print(breadthFirstValues(tree2))

# *recursive way
#!we can't apply a recursion on the breadthFirstValues function because recursion is based on the LIFO stack
#!while this function is based on the FIFO stack

#!Search tree
# *return true if the target is in our tree
# *with breadthFirstValues method:


def breadthSearch(head, target):
    if head is None:
        return False
    stacks = deque([head])
    while stacks:
        current = stacks.popleft()
        if current.key == target:
            return True

        if current.left:
            stacks.append(current.left)

        if current.right:
            stacks.append(current.right)

    return False

# print(breadthSearch(tree2,9))

#!with depth recursive method
def DepthSearchRec(head, target):
    # *Base case
    if head is None:
        return False
    if head.key == target:
        return True

    return DepthSearchRec(head.left, target) or DepthSearchRec(head.right, target)

#print(DepthSearchRec(tree2, 90))


#!Tree min value

def TreeMinValue(head):

    # *base case: an empty node will be considered as infinite
    if head is None:
        return math.inf
    if not head.left and not head.right:
        return head.key

    # *small amount of work in each iteration
    leftmin = TreeMinValue(head.left)
    rightmin = TreeMinValue(head.right)

    return min(leftmin, rightmin, head.key)


print("min value:", TreeMinValue(tree2))
