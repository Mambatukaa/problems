import LeetCode.ArrayAndString.*;

import java.util.Arrays;
import java.util.List;

class Main {
    public static void main(String[] args) {
        int target = 100;
        int[] nums = new int[]{5, 25, 75};

        TwoSumSorted twoSumSorted = new TwoSumSorted(nums, target);

        System.out.println(Arrays.toString(twoSumSorted.naive()));


    }

}
