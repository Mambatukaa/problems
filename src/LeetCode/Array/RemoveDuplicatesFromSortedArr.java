package LeetCode.Array;

import java.util.Arrays;

public class RemoveDuplicatesFromSortedArr {

    public int[] nums;


    public RemoveDuplicatesFromSortedArr(int[] nums) {
        this.nums = nums;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public int naive() {
        // declare pointers
        int leftIndex = 0;
        int rightIndex = 1;
        int n = nums.length;

        while (rightIndex < n) {
            // get current values
            int leftNum = nums[leftIndex];
            int rightNum = nums[rightIndex];

            if (leftNum == rightNum) {
                rightIndex++;
                continue;
            }

            // update duplicated value
            nums[++leftIndex] = rightNum;
            rightIndex++;
        }

        return leftIndex + 1;
    }

    public int solution() {
        // declare pointers
        int leftIndex = 0;
        int rightIndex = 1;
        int n = nums.length;

        while (rightIndex < n) {
            // get current values
            int leftNum = nums[leftIndex];
            int rightNum = nums[rightIndex];

            if (leftNum != rightNum) {
                nums[++leftIndex] = rightNum;
            }

            rightIndex++;
        }

        return leftIndex + 1;
    }
}
