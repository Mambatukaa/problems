
"""
Given a strings and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "y"



Constraints:
1 = s. length = 105
s consists of lowercase English letters.
• 1 < k <= 10^5

"""

from collections import Counter


# Time Complexity: O(n)
# Space Complexity: O(1)
# Odd count
def canConstruct(s, k):
    if len(s) == k:
        return True
    if len(s) < k:
        return False

    freq = [0] * 26

    for ch in s:
        freq[ord(ch) - ord("a")] += 1


    oddCount = 0

    # count odd freq
    
    for count in freq:
        if count % 2 == 1:
            oddCount += 1


    return oddCount <= k



# Bit manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)
def canConstructII(s, k):
    # Handle edge cases
    if len(s) < k:
        return False
    if len(s) == k:
        return True
    # Initialize oddCount as an integer bitmask
    odd_count = 0

    # Update the bitmask for each character in the string
    for chr in s:
        odd_count ^= 1 << (ord(chr) - ord("a"))

    print(odd_count)
    print(bin(odd_count))
    # Return if the number of odd frequencies is less than or equal to
    return bin(odd_count).count("1") <= k

s = "aaaaaabbcde"
k = 2

print("res:", canConstructII(s, k))


"""

When k = 2

Every characters sum must be equal to k 
    OR up to K characters can be different


messi  k = 3

m 
ss
i
e

"""
