"""

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.A fancy string is a string where no three consecutive characters are equal.







"""




class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def makeFancyString(self, s: str) -> str:
        # 2 pointers

        res = []

        l = 0

        for r in range(len(s)):
            if s[l] == s[r] and r - l >= 2:
                continue

            res.append(s[r])

            if s[l] != s[r]:
                l = r

        return "".join(res)

            




# fancy string is a string where no three consecutive characters are equal


"""





 l
   r
leeetcode





"""
        



class Solution:
    def makeFancyString(self, s: str) -> str:
        res = [s[0]]
        frequency = 1
        prev = s[0]

        for i in range(1, len(s)):

            if s[i] == prev:
                frequency += 1
            else:
                prev = s[i]
                frequency = 1
            
            if frequency < 3:
                res.append(s[i])

        return "".join(res)
# No space
class Solution:

    def makeFancyString(self, s: str) -> str:
        j = 2

        s = list(s)

        for i in range(2, len(s)):
            if s[i] != s[j - 1] or s[i] != s[j - 2]:
                s[j] = s[i]
                j += 1
            
        return "".join(s[:j])

