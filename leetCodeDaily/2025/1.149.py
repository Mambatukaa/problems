from collections import Counter

class Solution:
    def findValidPair(self, s: str):
        n = len(s)
        
        if n == 2:
            return ""

        validPairs = []

        seenCount = Counter(s)

        for i in range(n - 1):
            n1 = s[i]
            n2 = s[i + 1]

            if n1 != n2:
                if int(n1) == seenCount[n1] and int(n2) == seenCount[n2]:
                    return "".join([n1, n2])



        return ""






solution = Solution()

print("res:", solution.findValidPair("291212"))
