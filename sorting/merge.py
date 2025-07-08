def sort_merge(array: list, reverse: bool = False) -> list:
    assert isinstance(array, list)
    if len(array) <= 1:
        return array
    arr = array.copy()
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    left, right = sort_merge(left,reverse), sort_merge(right, reverse)
    return merge(left, right, reverse)

def merge(left, right, reverse: bool = False):
    merged = []
    while left and right:
        if not reverse:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        else:
            if left[0] > right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))

    merged.extend(left or right)
    return merged
