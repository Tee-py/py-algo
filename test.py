import time
from typing import List

def mtd1(num):
    num = str(num)
    res = []
    i = len(num) % 3
    if i > 0:
        res.append(num[:i]+',')
    j = 0
    while i < len(num):
        if j == 3:
            res.append(",")
            j = 0
        else:
            res.append(num[i])
            i+=1
            j+=1
    return "".join(res)

def mtd2(num):
    """
    A Faster Approach
    """
    num = str(num)
    res = []
    i = len(num) % 3
    if i > 0:
        res.append(num[:i]+',')

    while i < len(num):
        res.append(num[i:i+3]+",")
        i=i+3
        
    return "".join(res)[:-1]

def smallest_missing_num(array: List):
    array.sort()
    smallest = 1
    for num in array:
        if num <= 0:
            continue
        if num == smallest:
            smallest = smallest + 1
        if num > smallest:
            break
    return smallest

print(smallest_missing_num([1,5,3,7]))
print(smallest_missing_num([-1, 1, 2, 3, -7, 5, 4]))
print(smallest_missing_num([-1,-2]))

