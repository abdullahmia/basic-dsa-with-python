# implement stack in python
def push(arr, value):
    arr.append(value)
    print('Data pushed successfully')

def pop(arr):
    poped_item = arr.pop()
    print(f"Poped item is: {poped_item}")

def peek(arr):
    index = len(arr) - 1
    print(f"Item is: {arr[index]}")

def display(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

def is_empty(arr):
    if len(arr) == 0:
        print('List is empty. Push some data!')
        return True
    else:
        return False

if __name__ == '__main__':
    arr = []
    while True:
        choise = input("Enter Choises:\n\t1. Push\n\t2. Pop\n\t3. Peek\n\t4. Display\n\t5. Exit\nEnter value: ")
        if choise == '1':
            thing = input("Enter value to push: ")
            push(arr, thing)
        elif choise == '2':
            if is_empty(arr):
                continue
            else:
                pop(arr)
                continue
        elif choise == '3':
            if is_empty(arr):
                continue
            else:
                peek(arr)
                continue
        elif choise == '4':
            if is_empty(arr):
                continue
            else:
                display(arr)
                continue
        elif choise == '5':
            print('Thanks for use!')
            break
        else:
            print('Enter between number 1-5')
            continue