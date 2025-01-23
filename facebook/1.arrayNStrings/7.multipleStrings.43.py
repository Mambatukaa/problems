"""
Given two non-negative integers numi and num represented as strings, return the product of numi and num, also represented as a string.
Note: You must not use any built-in Biginteger library or convert the inputs to integer directly.

Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

Example 2:
    Input: num1 = "123" , num2 = "456"
    Output: "56088"

"""
class Solution:
    # Time Complexity: O(n * m)
    # Space Complexity: O(n + m)
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        temp = 1
        ans = 0

        for i in range(len(num2) - 1, -1 , -1):
            res = 0

            multiplier = temp

            for j in range(len(num1) - 1, -1, -1):
                digit = int(num1[j])
                digit *= multiplier
                multiplier *= 10

                res += digit * int(num2[i])
            ans += res
            temp *= 10

        return str(ans)

    def multiplyII(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        ans= [0] * (len(num1) + len(num2)) 
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num2)):
            for i2 in range(len(num1)):
                digit = int(num1[i1]) * int(num2[i2])
                
                ans[i1 + i2] += digit
                ans[i1 + i2 + 1] += (ans[i1 + i2] // 10)
                ans[i1 + i2] = ans[i1 + i2] % 10

        ans, beg = ans[::-1], 0

        while beg < len(ans) and ans[beg] == 0:
            beg += 1

        ans = map(str, ans[beg:])

        return "".join(ans)













num1 = "123"
num2 = "456"

solution = Solution()

print("Res:", solution.multiplyII(num1, num2))



        
