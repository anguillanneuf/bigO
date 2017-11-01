def quicksort(array):
    _quicksort(array, 0, len(array)-1)
    return array

def _quicksort(array, low, high):
    pointer = partition(array, low, high)
    print(pointer)
    print(array[low:pointer])
    print(array[pointer:high])
    # if (low < high):
    #     pointer = partition(array, low, high)
    #     print(array)
    #     _quicksort(array, low, pointer-1)
    #     _quicksort(array, pointer, high)

def partition(array, low, high):

    while low < high:
        print("{}:{}".format(array[low], array[high]))
        if array[low] > array[high]:
            temp = array[high-1]
            array[high-1] = array[high]
            array[high] = array[low]
            array[low] = temp
            high -= 1
        else:
            low += 1


    return high


myArray = [2,5,7,34,54,13,90,10]
mySortedArray = quicksort(myArray)
print(mySortedArray)

# print(partition(myArray, 0, 7))