"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1





"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        str_num = list(str(n))

        idx = -1

        # compare the elements to find the swap element
        for i in range(len(str_num) - 2, -1, -1):
            if int(str_num[i]) < int(str_num[i + 1]):
                idx = i
                break

        if idx == -1:
            return -1


        # swap i with next greater element
        for i in range(len(str_num) - 1, -1, -1):
            if int(str_num[i]) > int(str_num[idx]):
                # swap
                str_num[idx], str_num[i] = str_num[i], str_num[idx]
                break

        # reverse after the elements after i:
        str_num[idx+1:] = str_num[idx + 1:][::-1]

        res = int("".join(str_num))

        if res >= 2 ** 31:
            return -1


        return res







        
