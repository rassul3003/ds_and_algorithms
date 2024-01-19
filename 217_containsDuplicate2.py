def containsDuplicates(arr):
    num = len(arr)
    for i in range(num-1):
        for j in range(i+1, num):
            if arr[i] == arr[j]:
                return True
    
    return False


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

arr = [1,2,3,5,3]

print(containsDuplicate_hashmap(arr))
print(containsDuplicates(arr))
