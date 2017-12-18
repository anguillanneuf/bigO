def merge_sort(array, i=None, j=None):
  
    if i is None and j is None:
        i = 0
        j = len(array)-1
        
    if i < j:
        mid = (i+j) // 2
        merge_sort(array, i, mid)
        merge_sort(array, mid+1, j)
        merge(array, i, mid, j)
    return array

def merge(array, i, mid, j):

    i_end = mid + 1
    j_start = mid + 1

    pointer = i

    helper = array[:]    # Not doing in place merge sort

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


