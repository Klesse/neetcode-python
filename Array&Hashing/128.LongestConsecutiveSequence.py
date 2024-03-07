# Better solution

def longestConsecutive(nums):
    nums_sort = sorted(set(nums))
    sequences = []
    seq = 0
    previous = 0
    for n in nums_sort:
        if seq == 0:
            seq += 1
        else:
            if n == (previous + 1):
                seq += 1
            else:
                sequences.append(seq)
                seq = 1
        previous = n
    sequences.append(seq)
    return max(sequences)