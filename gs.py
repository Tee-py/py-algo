from itertools import combinations, combinations_with_replacement 
import threading
import re
from algorithms import bin_search
from time import time


def is_next(char, string):
    if len(string) < 2:
        return False
    return True if char == string[0] else False

def comp(msg):
    if len(msg) < 2:
        return msg
    comp = ""
    i = 0
    while i < len(msg):
        cnt = 1
        while is_next(msg[i],msg[i+1:]):
            cnt +=1
            i+=1
        comp+=f"{msg[i-1]}{cnt}" if cnt > 1 else f"{msg[i]}"
        i+=1
    return comp

def comp_regex(msg):
    pass



def getUmbrellas(num, arr):
    if bin_search(arr, num):
        return 1
    lst = []
    def get_counts_thread(combs, num):
        for tup in combs:
            if sum(tup) == num:
                lst.append(len(tup))
    for i in range(1,len(arr)+1):
        combs = list(combinations_with_replacement(arr, i))
        thread = threading.Thread(target=get_counts_thread, args=(combs, num))
        thread.start()
    return min(lst) if lst else -1


#print(getUmbrellas(5,[i for i in range(40000)]))

def recusive_max(arr):
    arr.sort()
    return None if len(arr) == 0 else arr[0] if len(arr) == 1 else recusive_max(arr[int(len(arr)/2):]) if arr[int(len(arr)/2)] > recusive_max(arr[0:int(len(arr)/2)]) else recusive_max(arr[:int(len(arr)/2)])
  

def normal_max(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        mid = int(len(arr)/2)
        maxim = arr[mid]
        index = mid 
        for i in range(len(arr)):
            if arr[i] > maxim:
                maxim = arr[i]
                index = i
        return maxim


def bin_search(arr, val):
    return True if arr[int(len(arr)/2)] == val else bin_search(arr[int(len(arr)/2)+1:], val) if val > arr[int(len(arr)/2)] else bin_search(arr[:int(len(arr)/2)], val) if val < arr[int(len(arr)/2)] else None


#start = time()
#arr = [ i for i in range(10000000)]
#end = time()
#print(f"completed in {end-start}s")
#start = time()
#print(recusive_max([5]))
#print(bin_search([1,2,3,4,5,6,7], 67))
#end = time()
#print(f"completed in {end-start}s")
#start = time()
#print(max(arr))
#end = time()
#print(f"completed in {end-start}s")
#start = time()
#print(normal_max(arr))
#end = time()
#print(f"completed in {end-start}s")

