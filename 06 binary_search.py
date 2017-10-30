"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search_iterative(input_array, value):
    """Your code goes here."""
    left, right = 0, len(input_array)-1

    while left <= right:
        mid = (left+right)//2

        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_recursive(input_array, value, left=0, right=None):
    if right is None:
        right = len(input_array)-1
    if right < left:
        return -1

    mid = (left+right)//2
    # print("{}, {}:{}, {}".format(left, mid, input_array[mid], right))

    if input_array[mid] == value:
        return mid
    elif input_array[mid] < value:
        return binary_search_recursive(input_array, value, mid+1, right)
    else:
        return binary_search_recursive(input_array, value, left, mid-1)

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 100
test_val2 = 15

print(binary_search_iterative(test_list, test_val1))
print(binary_search_iterative(test_list, test_val2))
print(binary_search_recursive(test_list, test_val1))
print(binary_search_recursive(test_list, test_val2))


# Here is my ugly implementation
global pointer

def binary_search(input_array, value):
    global pointer
    pointer = len(input_array)//2
    binary_search_(input_array, value)
    return pointer

def binary_search_(input_array, value):
    global pointer
    local_pointer = len(input_array)//2

    if len(input_array) == 0:
        pointer = -1
        return pointer
    elif len(input_array) == 1:
        if input_array[0] == value:
            return pointer
        else:
            pointer = -1
            return pointer
    else:
        if input_array[local_pointer] < value:
            pointer = pointer + len(input_array[local_pointer+1:])//2+1
            return binary_search_(input_array[local_pointer+1:], value)
        elif input_array[local_pointer] > value:
            pointer = pointer - len(input_array[:local_pointer])//2-1
            return binary_search_(input_array[:local_pointer], value)
        else:
            return pointer

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 100
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))