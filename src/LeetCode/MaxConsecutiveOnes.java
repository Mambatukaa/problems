package LeetCode;

public class MaxConsecutiveOnes {
    final private int[] nums;

    public MaxConsecutiveOnes(int[] nums) {
        this.nums = nums;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public int naive() {
        int counter = 0, max = 0;

        for (int num : nums) {
            if (num == 1) {
                counter++;
            } else {
                max = Math.max(counter, max);
                counter = 0;
            }
        }

        return Math.max(counter, max);
    }
}
