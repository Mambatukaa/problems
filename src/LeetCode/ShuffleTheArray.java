package LeetCode;

import java.util.ArrayList;
import java.util.Arrays;

public class ShuffleTheArray {
    final private int[] nums;
    final private int n;

    public ShuffleTheArray(int[] nums, int n) {
        this.nums = nums;
        this.n = n;
    }


    public Object[] naiveArraylistSolution() {
        System.out.println("Nums: " + Arrays.toString(nums));
        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = 0; i < nums.length / 2; i++) {
            System.out.println(i + n);
            ans.add(nums[i]);
            ans.add(nums[i + n]);
        }

        return ans.toArray();
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public int[] solution() {
        int[] ans = new int[n * 2];

        for (int i = 0; i < n; i++) {
            ans[i * 2] = nums[i];
            ans[i * 2 + 1] = nums[i + n];
        }

        return ans;
    }


}
