def merge_sort(array):
    _merge_sort(array, 0, len(array)-1)
    return array

def _merge_sort(array, i, j):
    if i < j:
        mid = (i+j) // 2
        _merge_sort(array, i, mid)
        _merge_sort(array, mid+1, j)
        merge(array, i, mid, j)

def merge(array, i, mid, j):

    i_end = mid + 1
    j_start = mid + 1

    pointer = i

    helper = array[:]

    while i < i_end and j_start < j+1:
        if helper[i] < helper[j_start]:
            array[pointer] = helper[i]
            i += 1
        else:
            array[pointer] = helper[j_start]
            j_start += 1
        pointer += 1
        
    rem = i_end - i
    for k in range(rem):
        array[pointer+k] = helper[i+k]

test = [10,5,1,8,59,-9]
print(merge_sort(test))


