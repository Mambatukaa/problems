class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)

        max_vowel = 0
        max_consonant = 0

        for k, v in count.items():
            if k in "aeiou":
                if v > max_vowel:
                    max_vowel = v
            else:
                if v > max_consonant:
                    max_consonant = v

        return max_vowel + max_consonant
        
