def quicksort(array):
    _quicksort(array, 0, len(array)-1)
    return array

def _quicksort(array, low, high):
    pointer = partition(array, low, high)
    # print(pointer)
    # print("left: {}, right: {}".format(array[low:pointer], array[pointer+1:high]))

    if (low < high):
        pointer = partition(array, low, high)
        _quicksort(array, low, pointer-1)
        _quicksort(array, pointer, high)

def partition(array, low, high):


    while low < high:
        if high - low == 1:
            if array[low] > array[high]:
                array[high], array[low] = array[low], array[high]
            exit
        # print(array)
        # print("{}:{}, {}:{}".format(low, array[low], high, array[high]))
        if array[low] > array[high]:
            temp = array[high-1]
            array[high-1] = array[high]
            array[high] = array[low]
            array[low] = temp
            high -= 1
        else:
            low += 1


    return high


myArray = [20,5,7,34,54,13,90,10]
print(quicksort(myArray))
