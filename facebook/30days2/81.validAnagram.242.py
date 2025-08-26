""""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?





"""



# Time Complexity: O(n) len(s) == n
# Space Complexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0] * 26


        for i in range(len(s)):
            counter[ord(s[i]) - ord("a")] += 1
            counter[ord(t[i]) - ord("a")] -= 1


        return all(value == 0 for value in counter) 
        
