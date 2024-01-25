""""
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
----------
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
----------
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
---------
Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:
-----------
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


nums = [1,2,3,1]
k = 3            

# Time Complexity O(n^2)
def containsNearbyDuplicate_bruteforce(nums, k):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i]==nums[j] and abs(i-j) <= k:
                return True
    return False


# Time Complexity O(n)
def containsNearbyDuplicate_dict(nums, k):
    d = {}
    # iterate over indices and corresponding values of list 'nums' and store in dict 'd', where key is number, and value is its index
    for idx, val in enumerate(nums):
        if val in d and abs(idx - d[val]) <= k:
            return True
        else:
            d[val] = idx

    return False


print('Using bruteforce -', containsNearbyDuplicate_bruteforce(nums, k))
print('Using dictionary -', containsNearbyDuplicate_dict(nums, k))
