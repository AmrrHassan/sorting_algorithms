import timeit

start = timeit.default_timer()

def mergeSort(array):
    arrayLength = len(array)
    mid = arrayLength // 2

    inversions = 0
    if mid > 0:
        # divide array to multiple subarrays
        left = array[:mid]
        right = array[mid:]
        # recursive call till we reach minimal subarray
        inversions += mergeSort(left)
        inversions += mergeSort(right)
        # we merge both left and right subarrays
        inversions += merge(array, left, right)
    return inversions


def merge(arr, left, right):
    i, ileft, iright, inversions = 0, 0, 0, 0

    leftLength = len(left)
    rightLength = len(right)
    while ileft < leftLength and iright < rightLength:
        if left[ileft] <= right[iright]:
            arr[i] = left[ileft]
            ileft += 1
        else:
            # if left bigger than right 1 inversion occurs
            arr[i] = right[iright]
            iright += 1
            inversions += leftLength - ileft
        i+= 1
    while ileft < leftLength:
        arr[i] = left[ileft]
        ileft += 1
        i += 1
    while iright < rightLength:
        arr[i] = right[iright]
        iright += 1
        i += 1

    return inversions

f = open('Test.txt', 'r')
testFile = f.read().split('\n')
# testFile = [10,2,5,1,8,6]
x = mergeSort(testFile)
print("Inversions: ", x)



stop = timeit.default_timer()

print('Time: ', stop - start)
