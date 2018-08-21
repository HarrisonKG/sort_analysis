

def insertSort(size, arr):
    # first element is trivially sorted
    i = 1
    while(i < size):
        j = i
        while(j > 0 and arr[j-1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -=1

        i += 1

    return arr;



file_in = open('data.txt', 'r')
file_out = open('insert.out', 'w')

for line in file_in:
    nums = list(map(int, line.split()))
    size = nums[0]
    arr = nums[1:]
    arr = insertSort(size, arr)
    sorted_str = ' '.join(str(x) for x in arr) + '\n'
    file_out.write(sorted_str)

file_in.close()
file_out.close()

