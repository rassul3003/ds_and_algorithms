nums = [1,2,3,1]


# Time Complexity O(n^2)
# TLE - time limit exceeded for large arrays
def containsDuplicate_bruteforce(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False
            

# Time complexity O(nlogn)
def containsDuplicate_sorting(nums):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i-1]:
            return True
    return False

# Time complexity is O(n)
def containsDuplicate_hashset(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Time complexity is O(n)
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

def containsDuplicate(nums):
    if len(nums) == len(set(nums)):
        return False
    return True

print(containsDuplicate_bruteforce(nums))
print(containsDuplicate_sorting(nums))
print(containsDuplicate_hashset(nums))
print(containsDuplicate_hashmap(nums))
print(containsDuplicate(nums))