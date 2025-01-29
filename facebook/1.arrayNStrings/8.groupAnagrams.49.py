""""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
    Input: strs = ["eat", "tea", "tan", "ate" , "nat", "bat"]|
    Output: [["bat"], ["nat" , "tan"], ["ate", "eat" ,"tea"]]|

    Explanation:
    • There is no string in strs that can be rearranged to form "bat".
    • The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    • The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
    Input: strs = [""]
    Output: [["''']]|

Example 3:
    Input: strs = ["a"]|
    Output: [["a"] ]|










Constraints:
    • 1 <= strs.length <= 10^4)
    • 0 <= strs[i].length <= 100
    • strs [i] consists of lowercase English letters.
"""


from collections import defaultdict

class Solution:
    # Solution with sorting
    # Time Complexity: O(n * m log m)
    # Space Complexity: O(n)
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for word in strs:
            sortedStr = ''.join(sorted(word))
            res[sortedStr].append(word)

        return list(res.values())

    # count in the array and conver to tuple
    # Time Complexity: O(n * k) k is the maximum length of a string in strs. n is the length of strs
    # Space Complexity: O(n * k)
    def groupAnagramsII(self, strs):
        res = defaultdict(list)


        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord("a") - ord(c)] += 1

            res[tuple(count)].append(s)

        return list(res.values())







solution = Solution()

strs = ["eat", "tea", "tan", "ate" , "nat", "bat"]

print("res:", solution.groupAnagramsII(strs))
