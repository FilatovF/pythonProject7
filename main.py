"""Task 1"""


def binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2

    if (val == arr[mid]):
        return mid
    if (val > arr[mid]):
        return binary_search(arr[mid + 1:], val) + (mid + 1)
    return binary_search(arr[:mid], val)


"""Task 2"""


def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)

"""Task 3"""




if __name__ == "__main__":

    arr1 = []
    for i in range(10):
        arr1.append(i)
    for i in range(10):
        print(binary_search(arr1, i))

print(fibo(21))