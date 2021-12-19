# https://www.youtube.com/watch?v=IJDJ0kBx2LM&list=PLyZB5ywlnsu9zio01i5zViNFqQunOxrw5&index=33&ab_channel=freeCodeCamp.org
#!merge sort
# *recursive way

def Merge(data, start, mid, end):
    # *build a temporary array to avoid modifying the original one
    temp = []
    i, j = start, mid+1
    # *while both sub-array have values, then try and merge them in sorted order with linear comparison
    while (i <= mid and j <= end):
        if data[i] <= data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1

    # *Add the rest of the values from the left sub-array into the result
    # *when no right sub-array
    while (i <= mid):
        temp.append(data[i])
        i += 1

    # *Add the rest of the values from the right sub-array into the result
    # *when no left sub-array
    while (j <= end):
        temp.append(data[j])
        j += 1

    # *copy the temporary array to original one(data)
    i = start
    while i <= end:
        data[i] = temp[i-start]
        i += 1
    return data


def MergeSort(data, start, end):
    # *base case
    if len(data) <= 1:
        return data

    if start < end:
        mid = (start+end)//2
        MergeSort(data, start, mid)  # divide the left part of data
        MergeSort(data, mid+1, end)  # divide the right part of data
        return Merge(data, start, mid, end)

#data=[20,-5,10,3,2,0,44,58,22,-20]
#print(MergeSort(data,0,len(data)-1))


##another way to merge recursively

def merge(nums1, nums2):
    # List to store the results
    merged = []

    # Indices for iteration
    i, j = 0, 0

    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):

        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged array
    return merged + nums1_tail + nums2_tail


def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # Get the midpoint
    mid = len(nums) // 2

    # Split the list into two halves
    print("left: ", left := nums[:mid])
    print("right: ", right := nums[mid:])

    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    return merge(left_sorted, right_sorted)

#data=[20,-5,10,3,2,0,44,58,22,-20]
#print(merge_sort(data))


##Quicksort
"""
To overcome the space inefficiencies of merge sort, 
we'll study another divide-and-conquer based sorting algorithm called quicksort, which works as follows:

1.If the list is empty or has just one element, return it. It's already sorted.

2.Pick a random element from the list. This element is called a pivot.

3.Reorder the list so that all elements with values less than or equal to the pivot come before the pivot,
while all elements with values greater than the pivot come after it. This operation is called partitioning.

4.The pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort.

Here's an implementation of quicksort, assuming we already have a helper function called partitions which picks a pivot, 
partitions the array in-place, and returns the position of the pivot element.
"""


def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end-1

    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums


# *iterative way
"""
1.Iterate over the list of numbers, starting from the left
2.Compare each number with the number that follows it
3.If the number is greater than the one that follows it, swap the two elements
4.Repeat steps 1 to 3 till the list is sorted.

We need to repeat steps 1 to 3 at most n-1 times to ensure that the array is sorted. 

This method is called bubble sort, as it causes smaller elements to bubble to the top and larger to sink to the bottom. 
"""


def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)

    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):

        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):

            # 2. Compare the number with
            if nums[i] > nums[i+1]:

                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]

    # Return the sorted list
    return nums

#data = [20, -5, 10, 3, 2, 0, 44, 58, 22, -20]
# print(bubble_sort(data))


## another way of sorting iteratively
"""
#* Insertion Sort

Before we look at explore more efficient sorting techniques, here's another simple sorting technique called insertion sort,
where we keep the initial portion of the array sorted and insert the remaining elements one by one at the right position.

1.Iterate over the list of numbers, starting from the left
2.Pick each number and compare to all numbers before him till the start of the list
3.If a number before the picked number is less than the picked number, place the picked number after the number less than him
"""


def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums


data = [20, -5, 10, 3, 2, 0, 44, 58, 22, -20]
print(insertion_sort(data))
