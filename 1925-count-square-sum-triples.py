"""
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:
---------
Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:
---------
Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 

Constraints:
-----------
1 <= n <= 250
"""

# !!! you don't really need to import sqrt form math, because ** 0.5 can be used instead

n = 10

import math

def countTriples_bruteforce(n):
    cnt = 0
    nums = []

    for i in range(1,n+1):
        nums.append(i)

    for a in nums:
        for b in nums:
            if a**2 + b**2 <= n**2 and math.sqrt(a**2 + b**2) in nums:
                cnt += 1
            
    return cnt
    

def countTriples_bruteforce2(n):
    cnt = 0

    for a in range(1, n):
        for b in range(a+1, n):
            c = (a**2 + b**2) ** 0.5
            if int(c) == c and c <= n:
                cnt += 2

    return cnt



print('Using bruteforce -', countTriples_bruteforce(n))
print('Using bruteforce -', countTriples_bruteforce2(n))