package LeetCode;

import java.util.Arrays;

public class SquaresOfSortedArray {
    final private int[] nums;

    public SquaresOfSortedArray(int[] nums) {
        this.nums = nums;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public int[] naive() {
        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] * nums[i];
        }

        Arrays.sort(nums);

        return nums;
    }


}
