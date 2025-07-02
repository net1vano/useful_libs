def bubble_sort(array: list, reverse: bool = False) -> list:
    assert isinstance(array, list)
    arr = array.copy()
    x = len(arr)
    for i in range(x-1):
        for j in range(x - 1 - i):
            if reverse:
                if arr[j+1] > arr[j]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j+1] < arr[j]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


print(bubble_sort([2,4,1,3,7,8,9,0,11]))
print(bubble_sort([2,4,1,3,7,8,9,0,11], True))