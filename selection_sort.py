# Implement Selection sort algorithm in python
def selection_sort(arr, size):
    # start a loop for grab a element for compare other element
    for i in range(0, size):
        for j in range(i + 1, size):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    numbers = [3, 2, 435, 23, 7, 5, 30, 34]
    selection_sort(numbers, len(numbers))
    print(numbers)
