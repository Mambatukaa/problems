package LeetCode;

import java.util.Arrays;

public class PivotIndex {
    final private int[] nums;

    public PivotIndex(int[] nums) {
        this.nums = nums;
    }

    // Space complexity: O(n)
    // Time complexity: O(n)
    public int naive() {
        int[] leftSum = nums.clone();
        int[] rightSum = nums.clone();

        for (int i = 1; i < nums.length; i++) {
            leftSum[i] = leftSum[i - 1] + leftSum[i];
        }

        for (int i = nums.length - 2; i >= 0; i--) {
            rightSum[i] = rightSum[i] + rightSum[i + 1];
        }

        for (int i = 0; i < nums.length; i++) {
            if (rightSum[i] == leftSum[i]) {
                return i;
            }
        }


        return -1;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public int solution() {
        if (nums.length == 0) return -1;

        int leftSum = 0, rightSum = 0;

        for (int num : nums)
            rightSum += num;

        for (int i = 0; i < nums.length; i++) {
            rightSum -= nums[i];
            if (rightSum == leftSum) return i;
            leftSum += nums[i];
        }

        return -1;

    }


}
