def sort_insert(array: list, reverse: bool = False) -> list:
    assert isinstance(array, list)
    arr = array.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if reverse:
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr
print(sort_insert([2,3,1,4,5,6,8,7,33]))