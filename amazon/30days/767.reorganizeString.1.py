
"""
 # 09 April 2025


Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

"""

from heapq import heappush, heapify, heappop
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)

        heap = [(-freq, element) for element, freq in freq_map.items()]
        
        heapify(heap)

        res = ""

        while heap:
            first_freq, first_element = heappop(heap)

            if not heap:
                if res and first_element == res[-1] or first_freq != -1:
                    return ""

                res += first_element
                break

            second_freq, second_element = heappop(heap)

            if first_freq != -1:
                heappush(heap, (first_freq + 1, first_element))
            if second_freq != -1:
                heappush(heap, (second_freq + 1, second_element))

            res += first_element + second_element

        return res

    # Time Complexity: O(n * log k)
    # Space Complexity: O(k)
    def reorganizeStringII(self, s: str) -> str:
        freq_map = Counter(s)

        heap = [(-freq, element) for element, freq in freq_map.items()]
        
        heapify(heap)

        res = ""

        while heap:
            first_freq, first_element = heappop(heap)

            if not res or res[-1] != first_element:
                res += first_element


                if first_freq + 1 != 0:
                    heappush(heap, (first_freq + 1, first_element))
            else:
                if not heap:
                    return ""

                second_freq, second_element = heappop(heap)
                res += second_element

                if second_freq + 1 != 0:
                    heappush(heap, (second_freq + 1, second_element))

                heappush(heap, (first_freq, first_element))

        return res

    # Counting odd even
    # Time Complexity: O(n)
    # Space Complexity: O(k)
    def reorganizeStringIII(self, s):
        n = len(s)
        char_counts = Counter(s)

        max_count, letter = 0, ""

        for char, count in char_counts.items():
            if count > max_count:
                max_count = count
                letter = char

        # case 1
        if max_count >  (n + 1) // 2:
            return ""

        res = [""] * n

        index = 0

        while char_counts[letter] != 0:
            res[index] = letter
            char_counts[letter] -= 1
            index += 2


        for char, count in char_counts.items():
            while count > 0:
                count -= 1

                if index >= n:
                    index = 1

                res[index] = char
                index += 2

        return "".join(res)


solution = Solution()            

s = "aabcdcd"


print("res:", solution.reorganizeStringIII(s))

