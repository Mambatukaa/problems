class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_arr = text.split(" ")
        broken_letters = set(brokenLetters)

        res = 0

        for word in text_arr:
            can_type = True
            for letter in word:
                if letter in broken_letters:
                    can_type = False
            if can_type:
                res += 1

        return res


        
