package LeetCode;

import java.util.Arrays;
import java.util.HashMap;

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


    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] mapSolution() {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        int[] duplicated = nums.clone();

        Arrays.sort(duplicated);

        for (int i = 0; i < duplicated.length; i++) {
            hashMap.putIfAbsent(duplicated[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            nums[i] = hashMap.get(nums[i]);
        }

        return nums;
    }

    public int[] solutionFromLeetCode() {
        int[] count = new int[101];
        int[] res = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            count[nums[i]]++;
        }

        System.out.println(Arrays.toString(count));

        for (int i = 1; i <= 100; i++) {
            count[i] += count[i - 1];
        }

        System.out.println(Arrays.toString(count));

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0)
                res[i] = 0;
            else
                res[i] = count[nums[i] - 1];
        }

        return res;
    }

}
