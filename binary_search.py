# Implement Binary Search in Python
def binary_search(arr, n, key):
    left = 0
    right = n - 1

    while left <= right:
        mid = left + right // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            left = mid + 1
        if arr[mid] > key:
            right = mid - 1

    return -1