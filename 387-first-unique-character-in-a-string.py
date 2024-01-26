"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
---------
Input: s = "leetcode"
Output: 0

Example 2:
---------
Input: s = "loveleetcode"
Output: 2

Example 3:
---------
Input: s = "aabb"
Output: -1
 

Constraints:
-----------
1 <= s.length <= 105
s consists of only lowercase English letters.
"""

s = "loveleetcode"

# Time Complexity O(n^2)
def firstUniqChar_bruteforce(s):
    for i in range(len(s)):
        is_unique = True
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                is_unique = False
                break

        if is_unique:
            return i

    return -1 


# Time Complexity O(n^2)
def firstUniqChar_bruteforce2(s):
    # s.count() will have time complexity of O(n) as well
    for idx, char in enumerate(s):
        if s.count(char) == 1:
            return idx

    return -1

# Time Complexity O(n^2)
def firstUniqChar_slicing(s):
    # check if the char is in a substring indexed from i+1 to end, and indexed up to i itself 
    for i in range(len(s)):
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return i
    return -1


# Time Complexity O(n)
def firstUniqChar_dict(s):
    d = {}
    for char in s:
        d[char] = d.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if d[char] == 1:
            return i

    return -1


print('Using bruteforce -', firstUniqChar_bruteforce(s))
print('Using bruteforce2 -', firstUniqChar_bruteforce2(s))
print('Using string slicing -', firstUniqChar_slicing(s))
print('Using string dict -', firstUniqChar_dict(s))