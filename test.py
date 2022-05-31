import time

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


"""
start = time.perf_counter()
mtd1(test_num)
print(f"First Method Ran In --> {time.perf_counter()-start} Secs")

start = time.perf_counter()
mtd2(test_num)
print(f"Second Method Ran In --> {time.perf_counter()-start} Secs")
"""
