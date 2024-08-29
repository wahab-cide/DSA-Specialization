def max_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[k]
        max_sum = (max_sum, window_sum)

    return max_sum


def longest_substring(str):
    
    pass