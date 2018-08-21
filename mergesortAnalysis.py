import random
import time


def merge(left, right):
    result = []

    # while both are not empty
    while (left and right):
        if (left[0] <= right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    # copy elements left over in one of the lists
    while(left):
        result.append(left[0])
        left = left[1:]

    while(right):
        result.append(right[0])
        right = right[1:]

    return result;



def mergeSort(size, arr):
    if(size <= 1):
        return arr;

    left = arr[0:size//2]
    right = arr[size//2:]

    left = mergeSort(len(left), left)
    right = mergeSort(len(right), right)

    return merge(left, right);



def generateArr(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, 10001))

    return arr;



def runSort(size):
    arr = generateArr(size)

    # time sorting in ms
    start = time.time()
    arr = mergeSort(size, arr)
    finish = time.time()
    elapsed = (finish - start) * 1000
    print(elapsed)
    return elapsed


def avgSort(size):
    avgElapsed = (runSort(size) + runSort(size) + runSort(size))/3
    print(size, avgElapsed, "\n")
    return


avgSort(64)
avgSort(128)
avgSort(256)
avgSort(512)
avgSort(1024)
avgSort(2048)
avgSort(4096)