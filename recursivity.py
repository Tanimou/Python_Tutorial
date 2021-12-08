#https://www.youtube.com/watch?v=IJDJ0kBx2LM&list=PLyZB5ywlnsu9zio01i5zViNFqQunOxrw5&index=33&ab_channel=freeCodeCamp.org
#!strign reversal
#*input: the simple engineer
#*output:reenigne elpmis eht
def reverseString(input):
    ##what is the base case?When can I no longer continue?
    #*one letter or empty string
    if(input== ""):
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
    if(len(input)==0|len(input)==1):
        return True
    
    if(input[0]==input[len(input)-1]):
        return isPalindrome(input[1:len(input)-1])
    
    #*additional base case to handle non palindrome
    return False

#print(isPalindrome("racecar"))

#!number to binary
def NumberToBinary(num,result):
    if(num==0):
        return result
    result=str(num%2)+result
    return NumberToBinary(num//2,result)##123/10=12.3 while 123//10=12

#print(DecimalToBinary(233,""))

#!binary search 
def binarySearch(A,left,right,x):
    if(left>right):
        return -1
    mid=(left+right)//2
    if(A[mid]==x):
        return mid
    elif x<A[mid]:
        return binarySearch(A,left,mid-1,x)
    else:
        return binarySearch(A,mid+1,right,x)

#print(binarySearch([-1,0,1,2,3,4,7,9,10,20],0,9,10))

#!merge sort
def Merge(data,start,mid,end):
    #*build a temporary array to avoid modifying the original one
    temp=[]
    i,j=start,mid+1
    #*while both sub-array have values, then try and merge them in sorted order with linear comparison
    while (i<=mid and j<=end):
        if data[i]<=data[j]:
            temp.append(data[i])
            i+=1
        else:
            temp.append(data[j])
            j+=1

    #*Add the rest of the values from the left sub-array into the result
    #*when no right sub-array
    while (i<=mid):
        temp.append(data[i])
        i += 1
               
    #*Add the rest of the values from the right sub-array into the result
    #*when no left sub-array
    while (j <= end):
        temp.append(data[j])
        j += 1
        
    #*copy the temporary array to original one(data)
    i=start
    while i<=end:
        data[i]=temp[i-start]
        i+=1
        
def MergeSort(data,start,end):
    #*base case
    if start<end:
        mid=(start+end)//2
        MergeSort(data,start,mid)#divide the left part of data
        MergeSort(data,mid+1,end)#divide the right part of data
        Merge(data,start,mid,end)      

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
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)
n6 = node(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

def reverseList(node):
    if node.head is None or node.next is None:
        return node
    p=reverseList(node.next)
    print(node.head)
    node.next.next=node
    node.next=None
    return p

def printlist(list):
    if list.next is None:
        print(list.head)
    if list.next != None:
        print(list.head,"-> ", end="")
        printlist(list.next)

printlist(n1)
printlist(reverseList(n1))
