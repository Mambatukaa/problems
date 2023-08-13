package LeetCode.ArrayAndString;

import java.util.Arrays;

public class ArrayPartitionOne {

    final private int[] nums;

    public ArrayPartitionOne(int[] nums) {
        this.nums = nums;
    }


    // Time complexity: O(n * log n)
    // Space complexity: O(n) sorting

    public int naive() {
        int counter = 0;

        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i += 2) {
            counter += nums[i];
        }


        return counter;
    }
}
