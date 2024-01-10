# First Solution - Passed (1479ms, 18.15MB)

def twoSum(nums, target: int) -> list:
    for index, number in enumerate(nums):
        for i in range(index+1, len(nums)):
            if number + nums[i] == target: 
                return [index, i]
            
# More efficient One
            
