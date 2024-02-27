# First approach

def groupAnagrams(strs):
    anagrams = strs.copy()
    result=[]
    anams = anagrams.copy()
    while(len(anagrams)>0):
        aux = []
        first = anams[0]
        for word in anams:
            if sorted(word) == sorted(first):
                aux.append(word)
                anagrams.remove(word)
        result.append(aux)
        anams = anagrams.copy()
    return result


# Hashmap O (m * n * 26)
# m = number os strings
# n = average length of each string, that will be counted (tea -> 1 a, 1 e, 1 t)
# 26 = all letters in alphabet

from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] +=1

        res[tuple(count)].append(s)
    return res.values()
