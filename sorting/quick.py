
def sort_quick(array: list, reverse: bool = False) -> list:
    assert isinstance(array, list)
    if len(array) <= 1 :
        return array
    arr = array.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    result = sort_quick(left) + middle + sort_quick(right)
    return result if not reverse else result[::-1]

print(sort_quick([4,1,3,2,5,8,7,9,11,12]))

