""""

You are given a 0-indexed string blocks of length n, where blocks [i] is either "W' or 'B', representing the color of the ith block. The
characters "W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

Example 1:
    Input: blocks = "WBBWWBBWBW", k = 7
    Output: 3

    Explanation:
    One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
    so that blocks = "BBBBBBBWBW" .
    It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
    Therefore, we return 3.

Example 2:
    Input: blocks = "WBWBBBW", k = 2
    Output: 0
    Explanation:
    No changes need to be made, since 2 consecutive black blocks already exist.
    Therefore, we return 0.

Constraints:
• n == blocks. length
• 1 <= n <= 100
• blocks [i] is either "W' or • 'B'
• 1 <= k <= n



"""


# Sliding window
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = r = 0
        res = float('inf')
        ctr = 0


        while r < len(blocks):
            while r - l < k:
                if blocks[r] == "B":
                    ctr += 1
                r += 1

            res = min(res, k - ctr)
            if blocks[l] == "B":
                ctr -= 1
            l += 1

        return res

# Sliding window
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        num_whites = 0
        num_recolors = float("inf")

        # Move right pointer
        for right in range(len(blocks)):

            # Increment num_whites if block at right pointer is white
            if blocks[right] == "W":
                num_whites += 1

            # k consecutive elements are found
            if right - left + 1 == k:

                # Update minimum
                num_recolors = min(num_recolors, num_whites)

                # Decrement num_whites if block at left pointer is white
                if blocks[left] == "W":
                    num_whites -= 1

                # Move left pointer
                left += 1

        return num_recolors

# QUEUE
# Time Complexity: O(n)
# Space Complexity: O(m) k elements
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        block_queue = deque()
        num_whites = 0

        # Initiate queue with first k values
        for i in range(k):
            current_char = blocks[i]
            if current_char == "W":
                num_whites += 1
            block_queue.append(current_char)

        # Set initial minimum
        num_recolors = num_whites

        for i in range(k, len(blocks)):

            # Remove front element from queue and update current number of white blocks
            if block_queue.popleft() == "W":
                num_whites -= 1

            # Add current element to queue and update current number of white blocks
            current_char = blocks[i]
            if current_char == "W":
                num_whites += 1
            block_queue.append(current_char)

            # Update minimum
            num_recolors = min(num_recolors, num_whites)

        return num_recolors
        
solution = Solution()

blocks = "WBBWWBBWBW"
k = 7

blocks = "WBWBBBW"
k = 2
print("res:", solution.minimumRecolors(blocks, k))


""""
L           R
0 1 2 3 4 5 6 7 8 9
W B B W W B B W B W

Count B until R reaches k

update the answer and 





"""

