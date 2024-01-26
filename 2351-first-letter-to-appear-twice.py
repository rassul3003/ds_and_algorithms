"""
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

- A letter a appears twice before another letter b if the second occurrence of a is before the second 
occurrence of b.
- s will contain at least one letter that appears twice.
 

Example 1:
---------
Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

Example 2:
---------
Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
 

Constraints:
------------
2 <= s.length <= 100
s consists of lowercase English letters.
s has at least one repeated letter.
"""


s = "abccbaacz"


# Time Complexity O(n^2)
def repeatedCharacter_bruteforce(s):
    # O(n^2) is due to iteration over two lists of the max length of n
    seen = []

    for char in s:
        if char in seen:
            return char
        else:
            seen.append(char)


# Time Complexity O(n)
def repeatedCharacter_dict(s):
    # the approach is to store every char in dict and return the first char that is already in the 'seen' dict.
    seen = {}

    for char in s:
        if char in seen:
            return char
        else:
            seen[char] = 1


# Time Complexity O(n)
def repeatedCharacter_set(s):
    # the approach is similar to dict
    seen = set()

    for char in s:
        if char in seen:
            return char
        else:
            seen.add(char)





print('Using bruteforce -', repeatedCharacter_bruteforce(s))
print('Using dictionary -', repeatedCharacter_dict(s))
print('Using set -', repeatedCharacter_set(s))
