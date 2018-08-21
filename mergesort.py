
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



file_in = open('data.txt', 'r')
file_out = open('merge.out', 'w')

for line in file_in:
    nums = list(map(int, line.split()))
    size = nums[0]
    arr = nums[1:]
    arr = mergeSort(size, arr)
    sorted_str = ' '.join(str(x) for x in arr) + '\n'
    file_out.write(sorted_str)

file_in.close()
file_out.close()

