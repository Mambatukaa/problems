package LeetCode.ArrayAndString;

public class TwoSumSorted {
    final private int[] nums;
    final private int target;

    public TwoSumSorted(int[] nums, int target) {
        this.nums = nums;
        this.target = target;
    }

    // Space complexity: O(1)
    // Time complexity: O(n)
    public int[] naive() {
        int leftIndex = 0;
        int rightIndex = nums.length - 1;

        while (leftIndex < rightIndex) {
            int sum = nums[leftIndex] + nums[rightIndex];

            if (sum == target) {
                return new int[]{leftIndex + 1, rightIndex + 1};
            } else if (sum > target) {
                rightIndex--;
            } else {
                leftIndex++;
            }
        }

        return new int[]{};
    }
}
