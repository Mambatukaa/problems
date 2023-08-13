package LeetCode.ArrayAndString;

import java.util.Arrays;

public class MinimumSizeSubArray {
    final private int[] nums;
    final private int target;

    public MinimumSizeSubArray(int[] nums, int target) {
        this.nums = nums;
        this.target = target;
    }


    //
    public int naive() {
        Arrays.sort(nums);

        System.out.println(Arrays.toString(nums));

        int n = nums.length;
        int sum = 0;

        for (int i = n - 1; i > -1; i--) {

            sum += nums[i];

            System.out.println("num: " + nums[i] + " sum: " + sum);


            if (sum >= target) {
                return n - i;
            }

        }


        return 0;
    }

}
