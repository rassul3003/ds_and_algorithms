"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 

Example 1:
-----------
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [*1,*2,2,1]
- [*1,2,*2,1]
- [1,*2,2,*1]
- [1,2,*2,*1]

Example 2:
----------
Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.

Example 3:
----------
Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [*3,2,*1,5,4]
- [*3,2,1,*5,4]
- [3,*2,1,5,*4]
 

Constraints:
------------
1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99
"""


nums = [1,2,2,1]
k = 1

# Time complexity O(n^2)
def countKDifference_bruteforce(nums, k):
    count = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                count += 1

    return count



# Time Complexity O(n)
def countKDifference_dictionary(nums, k):
    numsDict = {}
    count = 0

    # store every number with its frequency in a dictionary
    for num in nums:
        if num not in numsDict:
            numsDict[num] = 1
        else:
            numsDict[num] += 1

    for num in nums:
        complement = num + k
        if complement in numsDict:
            count += numsDict[complement]

    return count 



print('Using bruteforce -', countKDifference_bruteforce(nums, k))
print('Using dictionary -', countKDifference_dictionary(nums, k))