# First code

# Using a Max Heap to pop from it k times O(k * log N)
# Better than using a Sorted list, which requires a sorting algorithm O(N log N)

# Using Bucket Sort O(2 * N) = O (N)

def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
