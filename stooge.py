# Kristen Harrison
# CS 325, HW2 -- Stoogesort

import math


# Implementation of stoogesort that takes as parameters an array 
# and left and right indices. Returns the sorted array
def stoogeSort(arr, left, right):
    size = right - left + 1

    # base case: array has two elements and the first one is larger, so swap them
    if ((size == 2) and (arr[left] > arr[right])):
        arr[left], arr[right] = arr[right], arr[left]

    # else recurse over the first two-thirds of the array, 
    # last two-thirds, and first two-thirds again
    elif size > 2:
        ceiling = math.ceil(2 * size / 3)
        stoogeSort(arr, left, left + ceiling - 1)
        stoogeSort(arr, left + size - ceiling, right)
        stoogeSort(arr, left, left + ceiling - 1)

    return arr;



file_in = open('data.txt', 'r')
file_out = open('stooge.out', 'w')

for line in file_in:
    # read each line in data.txt into a list
    nums = list(map(int, line.split()))
    size = nums[0]
    arr = nums[1:]
    arr = stoogeSort(arr, 0, size - 1)
    # format sorted array back into a string for file output
    sorted_str = ' '.join(str(x) for x in arr) + '\n'
    file_out.write(sorted_str)

file_in.close()
file_out.close()
