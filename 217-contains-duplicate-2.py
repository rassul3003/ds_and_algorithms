# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

arr = [1,2,3,5,3]
            

# Time Complexity O(n^2)
def containsDuplicates(arr):
    num = len(arr)
    for i in range(num-1):
        for j in range(i+1, num):
            if arr[i] == arr[j]:
                return True
    
    return False

# Time Complexity O(n)
def containsDuplicate_hashmap(nums):
    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += 1
            if seen[num] >= 2:
                return True
        else:
            seen[num] = 1
    return False


print('Using bruteforce -', containsDuplicate_hashmap(arr))
print('Using hashmap -', containsDuplicates(arr))
