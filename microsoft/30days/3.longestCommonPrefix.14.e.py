""""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.




"""


""""

Time complexity : O(S) , where S is the sum of all characters in all strings.

In the worst case all n strings are the same. The algorithm compares the string S1 with the other strings [S 
2
 …S 
n
 ] There are S character comparisons, where S is the sum of all characters in the input array.

Space complexity : O(1). We only used constant extra space.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix 


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
