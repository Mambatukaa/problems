package LeetCode;

import java.util.Arrays;

public class RemoveDuplicatesFromSortedArray {
    final private int[] nums;

    public RemoveDuplicatesFromSortedArray(int[] nums) {
        this.nums = nums;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public int naive() {
        int left = 0;
        int right = 1;

        while (right < nums.length) {
            int leftValue = nums[left];
            int rightValue = nums[right];

            if (leftValue != rightValue) {
                nums[left + 1] = nums[right];
                left++;
            }

            right++;
        }

        System.out.println(Arrays.toString(nums));

        return left + 1;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public int solution() {
        int insertIndex = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] != nums[i]) {
                nums[insertIndex] = nums[i];
                insertIndex++;
            }
        }

        return insertIndex;
    }
}
