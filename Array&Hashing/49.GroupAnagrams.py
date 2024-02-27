# First approach

def groupAnagrams(self, strs):
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
# n = number of words in each string, that will be counted (tea -> 1 a, 1 e, 1 t)
# 26 = all letters in alphabet

