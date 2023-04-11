package LeetCode.Array;

import java.util.Arrays;

public class SquaresOfSortedArray {
    final private int[] nums;

    public SquaresOfSortedArray(int[] nums) {
        this.nums = nums;
    }


    // Time complexity: O(n * logn)
    // Space complexity: O(1)
    public int[] naive() {
        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] * nums[i];
        }

        Arrays.sort(nums);

        return nums;
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] solution() {
        int leftIndex = 0;
        int rightIndex = nums.length - 1;
        int index = nums.length - 1;
        int[] ans = new int[nums.length];

        while (leftIndex <= rightIndex) {
            int leftNumSqr = (int) Math.pow(nums[leftIndex], 2);
            int rightNumSqr = (int) Math.pow(nums[rightIndex], 2);

            if (leftNumSqr > rightNumSqr) {
                ans[index] = leftNumSqr;
                leftIndex++;
            } else {
                ans[index] = rightNumSqr;
                rightIndex--;
            }

            index--;
        }

        return ans;
    }


}
