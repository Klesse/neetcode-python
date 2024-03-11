# First approach - brute force O(N²)

def maxArea(height):
    result = 0
    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            if min(height[i], height[j])*(j-i) > result:
                result = min(height[i], height[j])*(j-i)
    return result

# Second Approach (Beats only 15%)

def maxArea(height):
    result = 0
    i = 0
    j = len(height)-1
    while i < j:
        min_h = min(height[i],height[j])
        if min_h * (j-i) > result:
            result = min_h * (j-i)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return result