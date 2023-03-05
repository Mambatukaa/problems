package LeetCode;

public class NumberOfGoodPairs {
    final private int[] nums;


    public NumberOfGoodPairs(int[] nums) {
        this.nums = nums;
    }

    // Space complexity: O(1)
    // Time complexity: O(n^2)
    public int naive() {
        int count = 0;
        int length = nums.length;

        for (int i = 0; i < length; i++) {
            int current = nums[i];

            for (int j = i + 1; j < length; j++) {
                if (current == nums[j]) {
                    count++;
                }

            }
        }

        return count;
    }

}
