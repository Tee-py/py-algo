def is_next(char, string):
    if len(string) == 0:
        return False
    if char == string[0]:
        return True
    else:
        return False



def comp(msg):
    comp=""
    i = 0
    if len(msg)<2:
        return msg
    while i < len(msg):
        cnt = 1
        while is_next(msg[i],msg[i+1:]):
            cnt +=1
            i+=1
        comp+=f"{msg[i-1]}{cnt}" if cnt > 1 else f"{msg[i]}"
        #print(i)
        i+=1
        #print(i)
    return comp

#print(comp("wwww"))

# A Python program to print all combinations  
# of given length with duplicates in input 
from itertools import combinations, combinations_with_replacement 
  
# Get all combinations of [1, 1, 3] 
# and length 2 
import threading




def getUmbrellas(num, arr):
    if num in arr:
        return 1
    lst = []
    def get_counts_thread(combs, num):
        for tup in combs:
            if sum(tup) == num:
                #print("hello")
                lst.append(len(tup))
    for i in range(1,len(arr)+1):
        combs = list(combinations_with_replacement(arr, i))
        thread = threading.Thread(target=get_counts_thread, args=(combs, num))
        thread.start()
        #print("Hello")
    
        #for tup in combs:
        #    if sum(tup) == num:
        #        return len(list(tup))
        #combs.append(list(combinations_with_replacement(arr, i)))
    #for comb in combs:
        #print(comb)
        #for tup in comb:
            #print(sum(tup))
            #if sum(tup) == num:
                #return len(list(tup))
    return min(lst) if lst else -1


#lst = [1,2,3]
#combs = []
#for i in range(1,len(lst)):
#    combs.append(list(combinations(lst, i)))
#print(combs)
#for comb in combs:
#    for tup in comb:
#        print(sum(tup)==2)

print(getUmbrellas(6, [1,7]))
