package LeetCode;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class FindAllNumbersDisappeared {

    final private int[] nums;

    public FindAllNumbersDisappeared(int[] nums) {
        this.nums = nums;
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public List<Integer> naive() {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();


        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i + 1);
        }

        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(i + 1)) {
                list.add(i + 1);
            }
        }

        return list;
    }


    // Time complexity: O(n)
    // Space complexity: (1)
    public List<Integer> solution() {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int value = Math.abs(nums[i]);

            if (nums[value - 1] > 0) {
                nums[value - 1] *= -1;
            }
        }

        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                list.add(i + 1);
            }
        }

        return list;
    }
}
