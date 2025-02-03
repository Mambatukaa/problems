# initial



class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        idx = n + m - 1


        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            num1 = nums1[i]
            num2 = nums2[j]
            if num1 > num2:
                nums1[idx] = num1
                i -= 1
            else:
                nums1[idx] = num2
                j -= 1

            idx -= 1


        while i >= 0:
            nums1[idx] = nums1[i]
            i -= 1
            idx -= 1

        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1


    def mergeII(self, nums1, m: int, nums2, n: int) -> None:
        i = m - 1
        j = n - 1

        for idx in range(n + m - 1, -1, -1):
            if j < 0:
                break

            num1 = nums1[i] if i >= 0 else -float('inf') 
            num2 = nums2[j]

            if num1 > num2:
                nums1[idx] = num1
                i -= 1
            else:
                nums1[idx] = num2
                j -= 1

            idx -= 1















solution = Solution()

nums1 = [2, 0]
m = 1

nums2 = [1]
n = 1


solution.mergeII(nums1, m, nums2, n)

print("res:", nums1)
