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