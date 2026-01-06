"""
es not have a consonant.

 

Constraints:

1 <= word.length <= 20
word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and do


"""

## Time Complexity: O(n)
## Space Complexity: O(1)
class Solution:
    def isValid(self, word: str) -> bool:
        # first condition
        if len(word) < 3:
            return False
        
        has_vowel = False
        has_consonant = False

        for letter in word:
            letter = letter.lower()
            # isdigit
            # isalpha
            if letter.isalpha():
                if letter in "aeiou":
                    has_vowel = True
                elif not letter.isdigit():
                    has_consonant = True
            elif not letter.isdigit():
                return False
        return has_vowel and has_consonant


class Solution:
    def isValid(self, word: str) -> bool:
        # first condition
        if len(word) < 3:
            return False
        
        contains_vowel = False
        contains_consonant = False

        for letter in word:
            letter = letter.lower()
            # isdigit
            # isalpha
            # Second condition
            if not letter.isdigit() and not letter.isalpha():
                return False

            if letter in "aeiou":
                contains_vowel = True
            elif not letter.isdigit():
                contains_consonant = True
        return contains_vowel and contains_consonant

"""
It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
"""
