def bin_search(ss,key):
    low = 0
    high = len(ss) - 1
    while low <= high:
        mid = (high + low) // 2
        if key == ss[mid]:
            return mid
        elif key < ss[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None