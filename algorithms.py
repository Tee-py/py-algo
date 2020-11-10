
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

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr if i < pivot]
        right = [i for i in arr if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)



#print(recursive_max([1,12,3,4]))
#print(recursive_bin_search([1,5,6,7,8], 8))
#print(quicksort([1,67,3,56,90,3,4]))