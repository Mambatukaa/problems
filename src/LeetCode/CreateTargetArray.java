package LeetCode;

import java.util.Arrays;

// 1389
public class CreateTargetArray {
    final private int[] nums;
    final private int[] index;

    public CreateTargetArray(int[] nums, int[] index) {
        this.nums = nums;
        this.index = index;
    }

    private void shift(int[] nums, int index) {
        int i = nums.length - 1;

        while (i > index) {
            nums[i] = nums[i - 1];
            i--;
        }
    }

    // Time complexity: O(n^2)
    // Space complexity: O(n)
    public int[] naive() {
        int[] ans = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int position = index[i];

            shift(ans, position);

            ans[position] = num;
        }

        return ans;
    }
}
