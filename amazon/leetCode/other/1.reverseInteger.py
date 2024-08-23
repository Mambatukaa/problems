# Time Complexity: O(n)
# Space Complexity: O(1)
# 32 bit constraints
def reverseInteger(x):
  min = -2147483648
  max = 2147483648

  isPositive = x > 0
  x = abs(x)

  res = 0

  while x > 0:
    lastDigit = x % 10
    x = x // 10

    res *= 10
    res += lastDigit

  if res > max or res < min:
    return 0

  return res if isPositive else -res

print("RES:", reverseInteger(1534236469))

"""

x = 123
o: 321

x = -123
o = -321

Constraints:
-2^31 <= x <= 2^31 - 1

"""
