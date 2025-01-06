
"""

You have n boxes. You are given a binary string boxes of length n,
where boxes [il is '0' if the ith box is empty, and '1' if it contains
one ball.

In one operation, you can move one ball from a box to an adjacent box.
Box i is adjacent to box j if abs(i - j) == 1. Note that after doing
so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer [i] is the minimum
number of operations needed to move all the balls to the ith box.
Each answer [i] is calculated considering the initial state of the boxes.




Example 1:
Input: boxes = "110"
Output: [1,1,3]

Explanation: The answer for each box is as follows:
    1) First box: you will have to move one ball from
        the second box to the first box in one operation.

    2) Second box: you will have to move one ball from
        the first box to the second box in one operation.

    3) Third box: you will have to move one ball from
        the first box to the third box in two operations,
        and move one ball from the second box to the third
        box in one operation.

    {0, 1}

1. Collect the index which has ball in set
2. Iterate through boxes and do the inner loop with set
    and collect the totalSteps to collect balls from other indexes

idx 0 1 2
    1 1 0

set 0 1

"""


# Naive approach
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
def minOperations(boxes):
    res = [0] * len(boxes)

    ballIdx = set()

    for i in range(len(boxes)):
        box = boxes[i]
        if box == "1":
            ballIdx.add(i)

    for i in range(len(res)):
        counter = 0
        for ball in ballIdx:
            if i == ball:
                continue

            counter += abs(ball - i)

        res[i] = counter


    return res

print("res:", minOperations("110"))
