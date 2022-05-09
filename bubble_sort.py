# Implement bubble sort in python
def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


if __name__ == '__main__':
    numbers = [-2, 45, 0, 11, -9]
    bubble_sort(numbers, len(numbers))
    print(f"The sorted list is: {numbers}")