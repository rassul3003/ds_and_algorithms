"""
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. 
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.


Example 1:
---------
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 

Example 2:
---------
Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
 

Constraints:
-----------
3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums is strictly increasing.
"""


nums = [0,1,4,6,7,10]
diff = 3


# Time Complexity O(n^3)
def arithmeticTriplets_bruteforce(nums, diff):
    cnt = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                    cnt += 1

    return cnt    


def arithmeticTriplets_set(nums, diff):
    cnt = 0
    seen = set()
    for num in nums:
        if num - diff in seen and num - diff * 2 in seen:
            cnt += 1
        seen.add(num)

    return cnt
   

print('Using bruteforce -', arithmeticTriplets_bruteforce(nums, diff))
print('Using set -', arithmeticTriplets_set(nums, diff))