# Easiest answer - does not work with portuguese sentences

def encode(strs):
    if len(strs) == 0:
        return strs
    result = ""
    for word in strs:
        result += word + 'ç'
    return result [:len(result)-1]


def decode(s):
    if s == []:
        return []
    return s.split('ç')