
def findMedian(nums1, nums2):
    A = nums1
    B = nums2

    if len(nums1) > len(nums2):
        A = nums2
        B = nums1

    total = len(nums1) + len(nums2)

    half = total // 2

    l = 0
    r = len(A) - 1

    while True:
        i = l + (r - l) // 2 # A
        j = half - i - 2 # B

        ALeft = A[i] if i >= 0 else float('-infinity')
        ARight = A[i + 1] if i + 1 < len(A) else float('infinity')

        BLeft = B[j] if j >= 0 else float('-infinity')
        BRight = B[j + 1] if j + 1 < len(B) else float('infinity')

        if ALeft <= BRight and BLeft <= ARight:
            if total % 2:
                return min(ARight, BRight)
            else:
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
        elif ALeft < BRight:
            # go right
            l = i + 1
        else:
            # go left
            r = i - 1




nums1 = []
nums2 = [1]
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8]

print("res:", findMedian(nums1, nums2))
