""""

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.


"""



from collections import Counter
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def partitionLabels(self, s: str):
        ctr = Counter(s)

        n = len(s)

        len1 = n

        seen = set()

        prevIdx = 0

        res = []

        for i in range(n):
            letter = s[i]

            ctr[letter] -= 1

            if ctr[letter] == 0:
                del ctr[letter]
                len1 -= 1

            seen.add(letter)

            if len(seen) + len1 == n:
                # update the answer
                res.append(i - prevIdx + 1)
                prevIdx = i + 1

        return res

class Solution:
    # Two pointers solution
    # Time Complexity: O(n)
    # Space Complexity: O(k)
    def partitionLabels(self, s: str):
        last_occurence = [0] * 26

        for i, char in enumerate(s):
            last_occurence[ord(char) - ord("a")] = i

        partition_end = 0
        partition_start = 0

        res = []

        for i, char in enumerate(s):
            partition_end = max(partition_end, last_occurence[ord(char) - ord("a")])

            if partition_end == i:
                res.append(i - partition_start + 1)
                partition_start = i + 1

        return res
        


s = "ababcbacadefegdehijhklij"
s = "eccbbbbdec"
solution = Solution()
print("res:", solution.partitionLabels(s))
