# First approach - brute force solution - O(N²) (Time limit exceed), no stack

def dailyTemperatures(temperatures):
    days = []

    for index, temp in enumerate(temperatures):
        if (index == len(temperatures)-1):
            days.append(0)
        else:
            aux_ind = index+1
            aux_temp = temperatures[aux_ind]
            while temp >= aux_temp:
                if aux_ind >= len(temperatures)-1:
                    aux_temp = 9999999
                else:
                    aux_ind += 1
                    aux_temp = temperatures[aux_ind]
            if aux_temp == 9999999:
                days.append(0)
            else:
                days.append(aux_ind - index)
    return days

# Stack approach

def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for index, temp in enumerate(temperatures):
        if not stack:
            stack.append([temp, index])
        else:
            while stack and temp > stack[-1][0]:
                aux_index = stack.pop()[1]
                result[aux_index] = index - aux_index
            stack.append([temp,index])
    return result
            