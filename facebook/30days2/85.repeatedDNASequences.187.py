
"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.



"""






"""
Time complexity : O((N−L)L), that is O(N) for the constant L=10. In the loop executed N−L+1, one builds a substring of length L. Overall that results in O((N−L)L) time complexity.

Space complexity : O((N−L)L) to keep the hashset, that results in O(N) for the constant L=10.



"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # sliding window
        # register the dna in the map

        seen = set() 

        L, n = 10, len(s)

        res = set()

        for start in range(n - L + 1):
            key = s[start:L + start]

            if key in seen:
                res.add(key)

            seen.add(key)

        return list(res)


        
