
test5 = {
    'input': {
        'nums': [90, 87, 75, 60, 56]
    },
    'output': 5
}


test = {
    'input': {
        'nums': [19, 20, 30, 40, 50, 60, 70, 90, 11, 14]
    },
    'output': 3
}


""" 
If a list of sorted numbers is rotated k times, then the smallest number in the list ends up at position k (counting from 0).
Further, it is the only number in the list which is smaller than the number before it. 
Thus, we simply need to check for each number in the list whether it is smaller than the number that comes before it (if there is a number before it). 
Then, our answer i.e. the number of rotations is simply the position of this number is . If we cannot find such a number, then the list wasn't rotated at all.
"""


def count_rotations_linear(nums):
    b = 0
    for position in range(len(nums)):
        if (
            position > 0
            and nums[position] < nums[position - 1]
            and position != len(nums) - 1
        ):
            hh = position+1
            if nums[hh] > nums[position]:
                return position
            else:
                b = 1

    if b == 0:
        return 0
    elif b == 1:
        return len(nums)


""" If the middle element is smaller than its predecessor, then it is the answer
If the middle element of the list is smaller than 
the last element of the range, then the answer lies to the left of it. 
Otherwise, the answer lies to the right."""


def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1
    n = 0
    while lo <= hi:
        mid = int((lo+hi)//2)
        mid_number = nums[mid]

        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:",
              mid, ", mid_number:", mid_number)
        if hi == lo+1:
            return lo if nums[lo] < nums[hi] else hi
        if nums[hi] < nums[hi-1] and nums[lo+1] < nums[lo]:
            return len(nums) if n == 0 else hi
        if mid > 0 and mid_number < nums[mid-1]:
            # The middle position is the answer
            return mid

        elif nums[mid] < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1
            n += 1
        else:
            # Answer lies in the right half
            lo = mid + 1


print(count_rotations_binary(test['input']['nums']))
# [19, 25, 29, 35, 50, 67, 72, 9, 11, 14]
