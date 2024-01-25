"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:
----------
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
----------
Input: s = "rat", t = "car"
Output: false


Constraints:
------------
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

s = "anagram"
t = "nagaram"

# Time Complexity O(n)
def isAnagram_dictionary(s, t):
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

    return chars_1 == chars_2


# Time Complexity O(nlogn)
def isAnagram_sorting(s,t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    return sorted_s == sorted_t



# needs to import 'defaultdict' from 'collections' library.
from collections import defaultdict

# CoderPad allows to import the following libraries for python: 'requests', 'beautifulsoup', 'numpy', 'scipy', 'pandas', 'scikit-learn', and  'statsmodels'.

# Time Complexity O(n)
def isAnagram_defaultdict(s,t):
    # the difference between defaultdict and regular dict is that if key doesn't exist in reg dict, 'KeyError' will be raised. In defaultdict it will output the default value
    count = defaultdict(int)

    for x in s:
        count[x] += 1

    for x in t:
        count[x] -= 1

    for val in count.values():
        if val != 0:
            return False
        
    return True


# Time Complexity O(n)
def isAnagram_array(s,t):
    # initialize the list with 26 elements (for English alphabet) all set to 0, to keep track of frequencies.
    count = [0]*26
    
    for char in s:
        # find the Unicode for every character using 'ord' f-n, subtract from letter 'a' to store in array at proper index
        count[ord(char)-ord('a')] += 1

    for char in t:
        count[ord(char)-ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    
    return True

print('Using bruteforce -', isAnagram_dictionary(s,t))
print('Using sorting -', isAnagram_sorting(s,t))
print('Using default dictionary -', isAnagram_defaultdict(s,t))
print('Using array -', isAnagram_array(s,t))