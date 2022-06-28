def get_change(m, p):
    denominations = [0.01, 0.05, 0.10, 0.25, 0.50, 1]
    change = m - p
    res = [0, 0, 0, 0, 0, 0]
    if change >= 1:
        res[5] = (change//1)
        change = change % 1
    i = 4
    while i > 0:
        if change % denominations[i] == 0:
            res[i] = change/denominations[i]
        else:
            res[i] = change//denominations[i]
            if res[i] > 0:
                change = change%denominations[i]
        i -= 1
    return res

def test(string, arr):
    hashmap = {}
    for char in string:
        if hashmap.get(char):
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    lowest = len(string)
    for word in arr:
        count = 0
        hashmap2 = {}
        for char in word:
            if hashmap.get(char):
                if hashmap2.get(char):
                    hashmap2[char] += 1
                    if hashmap2[char] > hashmap[char]:
                        continue
                else:
                    hashmap2[char] = 1
                count += 1
            else:
                continue
        if (len(string)-count) < lowest:
            lowest = (len(string) - count)
    return lowest

print(test("apbpleeeeef", ["a", "ab", "abc", "abcg", "b", "c", "dog", "e", "efd", "zzzz"]))
# print(get_change(5, 0.99))
# print(get_change(3.14, 1.99))
# print(get_change(3, 0.01))
# print(get_change(4, 3.14))
# print(get_change(0.45, 0.34))
