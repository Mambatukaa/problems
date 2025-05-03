"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9

In this problem, we need to count all equivalent dominoes, where dominoes are represented by pairs. The definition of "equivalent" is that, under the condition of allowing the flip of two pairs, their elements correspond and are equal one by one.

So we might as well directly convert each binary pair into the specified format, that is, the first dimension must not be greater than the second dimension. Two pairs are equivalent if they contain the same two numbers, regardless of order.

Noticing that the elements in the pairs are all not greater than 9, we can concatenate each binary pair into a two-digit positive integer, i.e., (x,y)→10x+y. In this way, there is no need to use a hash table to count the number of elements, but we can directly use an array of length 100.
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numEquivDominoPairs(self, dominoes) -> int:
        # dominoes[i] = [a, b]
        # dominoes[j] = [c, d]
        # a == c and b == d
        # or (a == d and b == c)
        # (x,y) → 10x+y
        
        count = [0] * 100
        res = 0

        for x, y in dominoes:
            val = x * 10 + y if x <= y else y * 10 + x
            res += count[val]
            count[val] += 1

        return res


