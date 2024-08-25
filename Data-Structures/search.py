def linearSearch(arr, find):
    for idx, arr_each in enumerate(arr):
        if arr_each == find:
            return idx
print(linearSearch([3, 65, 8, 59, 6, 12], 6))




def BinarySearch(sorted_arr, find):
    low, high = 0, len(sorted_arr)

    while high - low > 0:
        mid = (low + high) // 2
        if find == sorted_arr[mid]:
            return mid
        
        if find > sorted_arr[mid]:
            low = mid +  1

        if find < sorted[mid]:
            high = mid - 1 

    mid = (low + high) // 2

    if find == sorted_arr[mid]:
        return mid
    return -1

#requires sorted array


#fibonacci search
def fibonacci_search(arr, find):
    f0, f1, f2 = 0, 1, 1
    start = -1
    size = len(arr)
    while f2 < size:
        f0 = f1
        f1 = f2
        f2 = f0 + f1

    while f2 > 1:
        pos = min(start + f0, size)

        if find > arr[pos]:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = pos
        elif find < arr[pos]:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return pos

    return -1
