# generate arrays of size n containing random integer values from 0 to 10,000
import random
import time


def insertSort(size, arr):
    i = 1
    while(i < size):
        j = i
        while(j > 0 and arr[j-1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -=1

        i += 1

    return arr;


def generateArr(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, 10001))

    return arr;


def runSort(size):
    arr = generateArr(size)

    # time sorting in ms
    start = time.time()
    arr = insertSort(size, arr)
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