# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

 
# Example 1:
# ----------
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# ----------
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# ----------
# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:
# ------------
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


nums = [2,7,11,15]
target = 9

# TIme Complexity O(n^2)
def twoSum_bruteforce(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
            

# Time Complexity O(n)
def twoSum_dictionary(nums, target):
    # store all the numbers with their indices in dictionary
    numsDict = {}

    for i in range(len(nums)):
        numsDict[nums[i]] = i

    for i in range(len(nums)):
        secondNum = target - nums[i]
        if secondNum in numsDict and numsDict[secondNum] != i:
            return [i, numsDict[secondNum]]
        
    return []    



def twoSum(nums, target):

    numsDict = {}

    for i in range(len(nums)):
        secondNum = target - nums[i]
        if secondNum in numsDict:
            return [i, numsDict[secondNum]]
        
        numsDict[nums[i]] = i

    return []
        




print('Using bruteforce -', twoSum_bruteforce(nums, target))
print('Using dictionary -', twoSum_dictionary(nums, target))
print('Using dictionary with one loop -', twoSum(nums, target))