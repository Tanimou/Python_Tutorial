#https://www.youtube.com/watch?v=IJDJ0kBx2LM&list=PLyZB5ywlnsu9zio01i5zViNFqQunOxrw5&index=33&ab_channel=freeCodeCamp.org
from binary_tree import TreeNode
from collections import deque
import math
#!strign reversal
#*input: the simple engineer
#*output:reenigne elpmis eht


def reverseString(input):
    ##what is the base case?When can I no longer continue?
    #*one letter or empty string
    if(input == ""):
        return ""

    ##what is the smallest amount of work I can do in each iteration,between each invocation
    ##what is the small "unit" I can reverse?

    return reverseString(input[1:])+input[0]

#print(reverseString("hello"))

#!palindrome
#*unique word where we can spell the same word forward and backward
#*Exple: kayak, racecar


def isPalindrome(input):
    #*define the base case/stopping condition
    if(len(input) == 0 | len(input) == 1):
        return True

    if(input[0] == input[len(input)-1]):
        return isPalindrome(input[1:len(input)-1])

    #*additional base case to handle non palindrome
    return False

#print(isPalindrome("racecar"))

#!number to binary


def NumberToBinary(num, result):
    if(num == 0):
        return result
    result = str(num % 2)+result
    return NumberToBinary(num//2, result)  # 123/10=12.3 while 123//10=12

#print(DecimalToBinary(233,""))

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

#print(binarySearch([-1,0,1,2,3,4,7,9,10,20],0,9,10))

#!merge sort


def Merge(data, start, mid, end):
    #*build a temporary array to avoid modifying the original one
    temp = []
    i, j = start, mid+1
    #*while both sub-array have values, then try and merge them in sorted order with linear comparison
    while (i <= mid and j <= end):
        if data[i] <= data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1

    #*Add the rest of the values from the left sub-array into the result
    #*when no right sub-array
    while (i <= mid):
        temp.append(data[i])
        i += 1

    #*Add the rest of the values from the right sub-array into the result
    #*when no left sub-array
    while (j <= end):
        temp.append(data[j])
        j += 1

    #*copy the temporary array to original one(data)
    i = start
    while i <= end:
        data[i] = temp[i-start]
        i += 1


def MergeSort(data, start, end):
    #*base case
    if start < end:
        mid = (start+end)//2
        MergeSort(data, start, mid)  # divide the left part of data
        MergeSort(data, mid+1, end)  # divide the right part of data
        Merge(data, start, mid, end)

#data=[20,-5,10,3,2,0,44,58,22,-20]
#MergeSort(data,0,len(data)-1)
#print((data))


#!reverse a linked list recursively
'''
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
n1.next = n2
n2.next = n3
n3.next = n4

n5.next = n6
n6.next = n7
n7.next = n8


def reverseList(node):
    if node.head is None or node.next is None:
        return node
    p = reverseList(node.next)
    print(node.head)
    node.next.next = node
    node.next = None
    return p


def printlist(list):
    if list.next is None:
        print(list.head)
    if list.next != None:
        print(list.head, "-> ", end="")
        printlist(list.next)


printlist(n1)
printlist(reverseList(n1))

#!merge two sorted linked lists
#*in a ordered way


def SortedMerge(a, b):

    if a is None:
        return b
    if b is None:
        return a
    print("a:", a.head, "", "b:", b.head)
    if a.head < b.head:

        a.next = SortedMerge(a.next, b)
        return a
    else:
        #print("a:", a.head, "", "b:", b.head)
        b.next = SortedMerge(a, b.next)
        return b
#printlist(n1)
#printlist(n5)
#printlist(SortedMerge(n1,n5))

#!trees
#*Add a node in the tree recursively


def InsertNode(head, data):
    #*base case
    if head is None:
        head = TreeNode(data)
        return head
    #*small amount of work in each iteration
    if(head.key < data):
        head.right = InsertNode(head.right, data)
    else:
        head.left = InsertNode(head.left, data)
    return head


tree_tuple = (((30, 50, 60), 80, (85, 90, 95)), 100,
              ((None, 110, 115), 120, (None, 140,15)))
tree2 = TreeNode.parse_tuple(tree_tuple)
#tree2.display_tree("  ")
print()
#tree3=InsertNode(tree2,108)
#tree3.display_tree("  ")
print()
#tree3 = InsertNode(tree2, 20)
#tree3.display_tree("  ")
print()
#tree3 = InsertNode(tree2, 135)
#tree3.display_tree("  ")
print()

#*print all leaf nodes


def printleaves(head):
    #*base case
    if head is None:
        return
    if head.left is None and head.right is None:
        print(head.key, ", ", end="")
        return
    #*small amount of work in each iteration
    if head.left is not None:
        printleaves(head.left)
    if head.right is not None:
        printleaves(head.right)

#printleaves(tree3)

#!Depth First Values
#*iterative way


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


#print(depthFirstValues(tree2))
#print(tree2.traverse_pre_order())
#*recursive way


def depthFirstValuesRec(head):
    if head is None:
        return
    print(left_subtree := depthFirstValuesRec(head.left))

    print(right_subtree := depthFirstValuesRec(head.right))
    return [head.key, left_subtree, right_subtree]

#print(depthFirstValuesRec(tree2))

#!breadthFirstValues
#*iterative way, based on the FIFO concept
#*we treat the stack as a queue


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

#print(breadthFirstValues(tree2))

#*recursive way
#!we can't apply a recursion on the breadthFirstValues function because recursion is based on the LIFO stack
#!while this function is based on the FIFO stack

#!Search tree
#*return true if the target is in our tree
#*with breadthFirstValues method:

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

#print(breadthSearch(tree2,9))

#!with depth recursive method

def DepthSearchRec(head, target):
    #*Base case
    if head is None:
        return False
    if head.key == target:
        return True

    return DepthSearchRec(head.left, target) or DepthSearchRec(head.right, target)

#print(DepthSearchRec(tree2, 90))


#!Tree min value



def TreeMinValue(head):
    
    #*base case: an empty node will be considered as infinite
    if head is None:
        return math.inf
    if not head.left and not head.right:
       return head.key

    #*small amount of work in each iteration
    leftmin = TreeMinValue(head.left)
    rightmin = TreeMinValue(head.right)
     
    return min(leftmin, rightmin, head.key)

print("min value:", TreeMinValue(tree2))
