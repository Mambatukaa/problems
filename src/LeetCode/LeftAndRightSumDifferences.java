package LeetCode;

import java.util.Arrays;

public class LeftAndRightSumDifferences {
    private final int[] nums;


    public LeftAndRightSumDifferences(int[] nums) {
        this.nums = nums;
    }

    private int[] leftSum(int[] nums) {
        int[] leftSum = new int[nums.length];
        int sumTracker = 0;
        int currentIndex = 1;

        for (int i = 0; i < nums.length - 1; i++) {
            sumTracker += nums[i];
            leftSum[currentIndex] = sumTracker;
            currentIndex++;
        }

        return leftSum;
    }

    private int[] rightSum(int[] nums) {
        int[] rightSum = new int[nums.length];
        int sumTracker = 0;
        int currentIndex = nums.length - 2;

        for (int i = nums.length - 1; i > 0; i--) {
            sumTracker += nums[i];
            rightSum[currentIndex] = sumTracker;
            currentIndex--;
        }

        return rightSum;
    }

    public int[] naive() {
        System.out.println("Starting...");

        int[] leftSum = this.leftSum(nums);
        int[] rightSum = this.rightSum(nums);


        int[] ans = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            int left = leftSum[i];
            int right = rightSum[i];

            ans[i] = Math.abs(left - right);
        }

        return ans;
    }

}
