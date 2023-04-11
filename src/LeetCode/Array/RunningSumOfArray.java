package LeetCode.Array;

// 1480

public class RunningSumOfArray {
    final private int[] nums;

    public RunningSumOfArray(int[] nums) {
        this.nums = nums;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public int[] naive() {
        int counter = 0;

        for (int i = 0; i < nums.length; i++) {
            counter += nums[i];
            nums[i] = counter;
        }

        return nums;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public int[] solution() {
        for (int i = 0; i < nums.length - 1; i++) {
            nums[i + 1] = nums[i] + nums[i + 1];
        }

        return nums;
    }
}
