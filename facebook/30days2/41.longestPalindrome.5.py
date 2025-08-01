class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = s[0]
        res_len = 1

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -=1 
                right += 1

            return s[left + 1: right]


        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > res_len:
                res = odd
                res_len = len(odd)
            if len(even) > res_len:
                res = even
                res_len = len(even)

        return res
                    

                



        



"""

O(n^2)

l   r
babad

comparing left and right


b a b a d
l m r


l i   r
0 1 2 3
c b b c
"""




