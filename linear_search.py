def linear_search(numbers, n, x):
    for i in range(0, n):
        if numbers[i] == x:
            return i
    return -1

items = [1, 2, 3, 5, 6, 7, 100]
result = linear_search(items, len(items), 34)
print(result)