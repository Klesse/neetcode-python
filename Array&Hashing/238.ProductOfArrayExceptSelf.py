# First and best solution

def productExceptSelf(nums):
    copi = nums.copy()
    if 0 not in nums:
        master = nums[0]
        for i in range(1,len(nums)):
            master *= nums[i]
        for i in range(len(nums)):
            nums[i] = master // nums[i]
    
    else:
        for i in range(len(nums)):
            aux = copi.copy()
            if nums[i] != 0:
                nums[i] = 0
            else:
                result = 1
                del(aux[i])
                for j in range(len(aux)):
                    result *= aux[j]
                nums[i] = result
    return nums