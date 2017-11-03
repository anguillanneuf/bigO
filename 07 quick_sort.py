def quicksort(array):
    _quicksort(array, 0, len(array)-1)
    return array

def _quicksort(array, i, j):
    if (i < j):
        pivot = partition(array, i, j)
        _quicksort(array, i, pivot-1)
        _quicksort(array, pivot, j)
        

def partition(array, i, j):

    while i < j:
        if j - i == 1:
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
            exit
 
        if array[i] > array[j]:
            array[i], array[j-1], array[j] = array[j-1], array[j], array[i]

            j -= 1
        else:
            i += 1

    return j


myArray = [20,5,7,34,54,13,90,10]
print(quicksort(myArray))
