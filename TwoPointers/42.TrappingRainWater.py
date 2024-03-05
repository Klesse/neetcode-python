def trap(height):
    result = 0
    max_left_value = 0
    max_right_value = 0

    max_left = []
    max_right = []

    for index in range(len(height)):
        if index != 0:
            if height[index-1] > max_left_value:
                max_left_value = height[index-1]
            max_left.append(max_left_value)
        else:
            max_left.append(0)

    for index in range(len(height)-1,-1,-1):
        if index != len(height)-1:
            if height[index+1] > max_right_value:
                max_right_value = height[index+1]
            max_right.append(max_right_value)
        else:
            max_right.append(0)

    max_right_f = [max_right[i] for i in range(len(max_right)-1,-1,-1)]
    print(max_left)
    print(max_right_f)

    for i in range(len(height)):
        if min(max_left[i],max_right_f[i]) - height[i]> 0:
            result += min(max_left[i],max_right_f[i]) - height[i]

    return result