# TIME LIMIT EXCEEDED
class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)

    def getProduct(self, k: int) -> int:
        n = len(self.nums)

        product = 1
        
        for i in range(n - 1, n - k - 1, -1):
            product *= self.nums[i]
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# Time Complexity: O(1)
# Space Complexity: O(n)
# PrefixProduct
class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.zeroIndex = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.zeroIndex = len(self.nums)
            self.nums.append(1)
            return
        

        if not len(self.nums):
            self.nums.append(num)
        else:
            self.nums.append(num * self.nums[-1])
        

    def getProduct(self, k: int) -> int:
        idx = len(self.nums) - k

        if self.zeroIndex >= idx:
            return 0

        if idx == 0:
            return self.nums[-1]

        return int(self.nums[-1] / self.nums[idx-1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# pa
