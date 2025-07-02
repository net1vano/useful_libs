def sort_select(array: list, reverse: bool = False) -> list:
    assert isinstance(array, list)
    arr = array.copy()
    x = len(arr)
    for i in range(x-1):
        min_index = i
        for j in range(i+1, x):
            if reverse:
                if arr[j] > arr[min_index]:
                    arr[j], arr[min_index] = arr[min_index], arr[j]
            else:
                if arr[j] < arr[min_index]:
                    arr[j], arr[min_index] = arr[min_index], arr[j]
    return arr

print(sort_select([3,5,1,4,8,6,9,0]))