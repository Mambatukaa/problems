package LeetCode;

public class BuildArrayFromPermutation {
    final private int[] nums;


    public BuildArrayFromPermutation(int[] nums) {
        this.nums = nums;
    }


    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] solution() {
        int[] ans = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            int current = nums[nums[i]];
            ans[i] = current;

        }

        return ans;
    }
}
