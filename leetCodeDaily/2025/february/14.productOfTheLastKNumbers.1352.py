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
        self.nums = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
            self.size = 0
        else:
            self.nums.append(num * self.nums[self.size])
            self.size += 1
        

    def getProduct(self, k: int) -> int:
        # 0 found
        if k > self.size:
            return 0

        return self.nums[self.size] // self.nums[self.size - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# pa
