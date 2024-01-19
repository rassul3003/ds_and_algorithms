# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

s = "anagram"
t = "nagaram"

# Time Complexity O(n)
def isAnagram_bruteforce(s, t):
    chars_1 = {}
    for char in s:
        if char in chars_1:
            chars_1[char] += 1
        else:
            chars_1[char] = 1

    chars_2 = {}
    for char in t:
        if char in chars_2:
            chars_2[char] += 1
        else:
            chars_2[char] = 1 

    if chars_1 == chars_2:
        return True
    else:
        return False


# Time Complexity O(nlogn)
def isAnagram_sorting(s,t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    return sorted_s == sorted_t


print('Using bruteforce -',isAnagram_bruteforce(s,t))
print('Using sorting -',isAnagram_sorting(s,t))