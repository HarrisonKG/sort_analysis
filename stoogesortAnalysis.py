import random
import time
import math


def stoogeSort(arr, left, right):
    size = right - left + 1

    # base case: array has two elements and the first one is larger
    if ((size == 2) and (arr[left] > arr[right])):
        arr[left], arr[right] = arr[right], arr[left]

    elif size > 2:
        ceiling = math.ceil(2 * size / 3)
        stoogeSort(arr, left, left + ceiling - 1)
        stoogeSort(arr, left + size - ceiling, right)
        stoogeSort(arr, left, left + ceiling - 1)

    return arr;



def generateArr(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, 10001))

    return arr


def runSort(size):
    arr = generateArr(size)

    # time sorting in ms
    start = time.time()
    arr = stoogeSort(arr, 0, size - 1)
    finish = time.time()
    elapsed = (finish - start) * 1000
    print(elapsed)
    #return elapsed


def avgSort(size):
    avgElapsed = (runSort(size) + runSort(size) + runSort(size))/3
    print(size, avgElapsed, "\n")
    return


#avgSort(64)
#avgSort(128)
#avgSort(256)
#avgSort(512)
#avgSort(1024)
#avgSort(2048)
#avgSort(4096)

runSort(4096)
