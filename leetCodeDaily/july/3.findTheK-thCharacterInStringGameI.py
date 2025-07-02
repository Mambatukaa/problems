""""
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

 

Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
Example 2:

Input: k = 10

Output: "c"

 

Constraints:

1 <= k <= 500
"""
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while len(word) < k:
            # generate new_word
            new_word = ""

            for l in word:
                letter = chr(ord(l) + 1) if ord(l) < 122 else 'a'

                new_word += letter

            word += new_word

        return word[k-1]





class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            ans += 1
        return chr(ord("a") + ans)


        


# by changing each character in word to it's next character in the word and append it
