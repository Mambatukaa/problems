""""

You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel ('a' , 'e' , 'i' ,and 'u') at least
once and exactly k consonants.

Example 1:
    Input: word = "aeioqa", k = 1
    Output: 0
    Explanation:
    There is no substring with every vowel.

Example 2:

    Input: word = "aeiou" , k=0
    Output: 1
    Explanation:
    The only substring with every vowel and zero consonants is word [0..4], which is "aeiou".

Example 3:

    Input: word = "ieaouqqieaouqa" , k = 1
    Output: 3

Explanation:

    The substrings with every vowel and one consonant are:


    • word [0..5], which is "ieaouq"
    • word [6..11], which is "qieaou"
    • word [7..12], which is "ieaouq"

Constraints:
• 5 < word. length <= 2 * 105
• word consists only of lowercase English letters.
• 0 <= k <= word. length - 5

"""





# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isVowel(self, letter):
        return letter in "aeiou"

    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        consonants_index = [0] * n
        consonant_index = n

        for i in range(n - 1, -1, -1):
            consonants_index[i] = consonant_index

            if not self.isVowel(word[i]):
                consonant_index = i

        left = right = 0

        vowel_count = {}
        consonant_count = 0
        res = 0

        while right < n:
            new_letter = word[right]

            # increase vowel or consonant count
            if self.isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            # if consonant reaches the limit shrink the window
            while consonant_count > k:
                start_letter = word[left]

                if self.isVowel(start_letter):
                    vowel_count[start_letter] -= 1

                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                left += 1


            # update the answer
            while left < n and len(vowel_count) == 5 and consonant_count == k:
                res += consonants_index[right] - right

                start_letter = word[left]

                if self.isVowel(start_letter):
                    vowel_count[start_letter] -= 1

                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1

                left += 1

            right += 1


        return res


        

solution = Solution()

word = "aeioutaeit"
k = 1
print("Res:", solution.countOfSubstrings(word, k))
