# First Solution - Time Limit Exceeded

def containsDuplicate(nums: list) -> bool:
	nums_sorted = nums.sort()
	for index, number in enumerate(nums):
		for i in range(index+1, len(nums)):
			if number == nums[i]:
				return True
	return False
	

	

# Optimized One - Passed (439 ms, 32.78 MB)

def containsDuplicate(nums) -> bool:
	return not (sorted(list(set(nums))) == sorted(nums))
	
# More efficient One - Passed (420ms, 32.72)

def containsDuplicate(nums: list) -> bool:
	hashset = set()
	for number in nums:
		if number in hashset:
			return True
		else:
			hashset.add(number)
	return False
