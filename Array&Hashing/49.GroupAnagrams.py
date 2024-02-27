# First approach

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = strs.copy()
    result=[]
    anams = anagrams.copy()
    while(len(anagrams)>0):
        aux = []
        first = anams[0]
        for word in anams:
            if set(word) == set(first):
                aux.append(word)
                anagrams.remove(word)
        result.append(aux)
        anams = anagrams.copy()
    return result