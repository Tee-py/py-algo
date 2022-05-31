#binary search algorithm for list
def bin_search(lst, item):
    lst.sort()
    start = 0
    end = len(lst)-1
    while start <= end:
        mid = int((start + end)*0.5)
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            end = mid -1
        else:
            start = mid + 1
    return None

def find_smallest(arr):
    value = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < value:
            value = arr[i]
            index = i
    return index

def selection_sort(arr):
    sorted_lst = []
    for i in range(len(arr)):
        sorted_lst.append(arr.pop(find_smallest(arr)))
        #arr.pop(arr[find_smallest(arr)])
    return sorted_lst

def flatten(lst):
    out = []
    for item in lst:
        if type(item) != list:
            out.append(item)
        else:
            for sub_item in item:
                lst.append(sub_item)
    return out
    
def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])

def recursive_count(arr):
    if arr == []:
        return 0
    elif len(arr) == 1:
        return 1
    else:
        return 1 + recursive_count(arr[1:])

def recursive_max(arr):
    if arr == []:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > recursive_max(arr[1:]):
            return arr[0]
        else:
            return recursive_max(arr[1:])

def recursive_bin_search(arr, item):
    if arr == []:
        return None
    else:
        start = 0
        end = len(arr) - 1
        mid = int((start+end)/2)
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return recursive_bin_search(arr[:mid-1], item)
        else:
            return recursive_bin_search(arr[mid+1:], item)

def quicksort(arr, reverse=False):
    if len(arr) < 2:
        return arr
    mid = int(len(arr)/2)
    left = [i for i in arr if i < arr[mid]]
    right = [i for i in arr if i > arr[mid]]
    if reverse:
        return quicksort(right, reverse=True) + [arr[mid]] + quicksort(left, reverse=True)
    return quicksort(left) + [arr[mid]] + quicksort(right)

def insert_sort(lst):
    for i in range(1, len(lst)):
        curr = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > curr:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = curr

def select_sort(lst):
    for i in range(len(lst)):
        m = lst[i]
        m_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < m:
                m = lst[j]
                m_index = j
        lst[m_index] = lst[i]
        lst[i] = m
    return lst

print(select_sort([1,3,2,5,4,6]))


