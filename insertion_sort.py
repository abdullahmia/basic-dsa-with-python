# Implement insertion sort algorithm in python
def insertion_sort(arr, size):
    for i in range(1, size):
        t = arr[i]
        j = i -1
        while j >= 0 and t < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = t


if __name__ == '__main__':
    nums = [34, 32, 2, 8, 90, 22, 56, 6]
    insertion_sort(nums, len(nums))
    print(nums)
