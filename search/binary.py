def binary(array: list, key: int, left: int = 0, right: int | None = None) -> int:
    assert isinstance(array, list)
    assert isinstance(key, int)
    if right is None:
        right = len(array)-1
    if left > right:
        return - 1
    mid = left + (right - left) // 2
    if array[mid] == key:
        return mid
    if array[mid] < key:
        return binary(array, key, mid+1, right)
    else:
        return binary(array, key, left, mid-1)
