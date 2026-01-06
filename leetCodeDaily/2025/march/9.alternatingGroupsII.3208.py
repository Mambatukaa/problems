class Solution:
    # Time Complexity: O(n + k)
    # Space Complexity: O(k)
    def numberOfAlternatingGroups(self, colors, k: int) -> int:
        # append k - 1. Left pointers == n
        for i in range(k - 1):
            colors.append(colors[i])

        n = len(colors)

        l = res = 0
        r = 1

        while r < n:
            if colors[r-1] == colors[r]:
                l = r
            
            if r - l + 1 == k:
                res += 1
                l += 1
            
            r += 1
            
        return res
    
    def numberOfAlternatingGroupsII(self, colors, k: int) -> int:
        n = len(colors)

        l = res = 0
        r = 0

        while r < n + k - 1:
            if colors[r % n] == colors[(r - 1) % n]:
                l = r
            
            if r - l + 1 == k:
                res += 1
                l += 1
            
            r += 1
            
        return res

class Solution1:
    def numberOfAlternatingGroups(self, colors, k):
        length = len(colors)
        result = 0
        # Tracks the length of the current alternating sequence
        alternating_elements_count = 1
        last_color = colors[0]

        # First pass through the array
        for index in range(1, length):
            # Check if the current color is the same as the last one
            if colors[index] == last_color:
                # Pattern breaks, reset sequence length
                alternating_elements_count = 1
                last_color = colors[index]
                continue

            # Sequence can be extended
            alternating_elements_count += 1

            # If sequence length reaches at least k, count it
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        # Wrap around to the first k - 1 elements
        for index in range(k - 1):

            # Pattern breaks. Since there are less than k elements remaining,
            # no more sequences can be formed
            if colors[index] == last_color:
                break

            # Extend the pattern
            alternating_elements_count += 1

            # Record a new alternating sequence
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        return result

class Solution2:
    def numberOfAlternatingGroups(self, colors, k: int) -> int:
        length = len(colors)
        result = 0
        alternating_elements_count = 1  # Length of current alternating sequence
        last_color = colors[0]  # Previous color

        # Loop through array with circular traversal
        for i in range(1, length + k - 1):
            index = i % length  # Wrap around using modulo

            # Check if current color is the same as the last color
            if colors[index] == last_color:
                # Pattern breaks, reset sequence length
                alternating_elements_count = 1
                last_color = colors[index]
                continue

            # Extend sequence
            alternating_elements_count += 1

            # If sequence length reaches at least k, count it
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        return result
solution = Solution()
colors = [0,1,0,1,0]
k = 3

print("res:", solution.numberOfAlternatingGroupsII(colors, k))
