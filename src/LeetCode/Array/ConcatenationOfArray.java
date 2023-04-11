package LeetCode.Array;

public class ConcatenationOfArray {
    final private int[] nums;

    public ConcatenationOfArray(int[] nums) {
        this.nums = nums;
    }


    public int helper(int index, int[] nums, int[] ans) {
        for (int num : nums) {
            ans[index] = num;
            index++;
        }

        return index;
    }


    // Time complexity: O(2n) ~ O(n)
    // Space complexity: O(n)
    public int[] naiveSolution() {
        int[] ans = new int[nums.length * 2];
        int index = this.helper(0, nums, ans);

        this.helper(index, nums, ans);

        return ans;
    }


    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] solution() {
        int length = nums.length;
        int[] ans = new int[length * 2];
        int index = 0;

        for (int i = 0; i < ans.length; i++) {

            ans[i] = nums[index];

            index = index >= length - 1 ? 0 : index + 1;
        }

        return ans;
    }

}

