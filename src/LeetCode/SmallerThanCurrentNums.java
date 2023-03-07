package LeetCode;

// 1365
public class SmallerThanCurrentNums {
    final private int[] nums;

    public SmallerThanCurrentNums(int[] nums) {
        this.nums = nums;
    }

    // Time complexity: O(n^2);
    // Space complexity: O(1);
    public int[] naive() {
        int counter = 0;
        int[] ans = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            for (int num : nums) {
                if (nums[i] > num) {
                    counter++;
                }
            }

            ans[i] = counter;
            counter = 0;
        }

        return ans;
    }

}
