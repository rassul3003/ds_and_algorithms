"""
Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

Return true if these subarrays exist, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
---------
Input: nums = [4,2,4]
Output: true
Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.

Example 2:
---------
Input: nums = [1,2,3,4,5]
Output: false
Explanation: No two subarrays of size 2 have the same sum.

Example 3:
--------
Input: nums = [0,0,0]
Output: true
Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0. 
Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.


Constraints:
-----------
2 <= nums.length <= 1000
-109 <= nums[i] <= 109
"""

nums = [4,2,4]

# Time Complexity O(n)
def findSubarrays_bruteforce(nums):
    sums = []
    for i in range(len(nums)-1):
        # if sum(nums[i:i+2]) in sums     is also possible, but might be hard to read
        if nums[i] + nums[i+1] in sums:
            return True
        else:
            sums.append(nums[i] + nums[i+1])
    
    return False


# Time Complexity O(n)
def findSubarrays_dict(nums):
    seen = {}

    for i in range(len(nums)-1):
        s = sum(nums[i:i+2])
        if s in seen:
            return True
        else:
            seen[s] = 1

    return False


# Time Complexity O(n)
def findSubarrays_set(nums):
    seen = set()
    for i in range(len(nums)-1):    
        sum = nums[i] + nums[i+1]

        if sum in seen:
            return True
        else:
            seen.add(sum)

    return False


print('Using bruteforce -', findSubarrays_bruteforce(nums))
print('Using dictionary -', findSubarrays_dict(nums))
print('Using set -', findSubarrays_set(nums))