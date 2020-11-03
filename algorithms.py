def bin_search(lst, num):
    start = 0
    end = len(lst)-1
    while start<=end:
        mid = int((start+end)/2)
        if lst[mid] == num:
            return mid
        if lst[mid] < num:
            start = mid+1
        elif lst[mid] > num:
            end = mid - 1
    return None
