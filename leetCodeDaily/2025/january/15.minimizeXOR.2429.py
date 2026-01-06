""""

Given two positive integers numi and num2, find the positive integer x such that:
    • x has the same number of set bits as num, and
    • The value x XOR num1 is minimal.

Note that XOR is the bitwise XOR operation.

    Return the integer x. The test cases are generated such that x is uniquely determined.
    The number of set bits of an integer is the number of 1's in its binary representation.


Constraints:
• 1 < num1, num2 <= 10^9



Example 1:
    Input: num1 = 3, num2 = 5
    Output: 3

Explanation:
    The binary representations of numi and num2 are 0011 and 0101, respectively.
    The integer 3 has the same number of set bits as numb, and the value 3 XOR 3 = 0 is
    minimal.


"""


# Time Complexity: O(log n)
# Space Complexity: O(1)
def minimizeXOR(num1, num2):
    def countBits(num):
        res = 0

        while num > 0:
            # 0001
            # 0001
            # If they are both 1 will return 1
            # set the bit
            res += 1 & num

            num = num >> 1
        return res

    cnt1, cnt2 = countBits(num1), countBits(num2)

    x = num1
    i = 0

    # remove least significant
    while cnt1 > cnt2: 
        # 1 shifted by to the left ended with number x
        # check the 1 from the right side in x
        if x & ( 1 << i):
            cnt1 -= 1
            # unset the bit
            x = x ^ (1 << i)
        i += 1

    # adding least significant
    while cnt1 < cnt2:
        if x & ( 1 << i) == 0:
            cnt1 += 1
            x = x | (1 << i)
        i += 1


    return x

num1 = 3
num2 = 5

print("res:", minimizeXOR(num1, num2))

num1 = 1
num2 = 12

print("res 1:", minimizeXOR(num1, num2))
