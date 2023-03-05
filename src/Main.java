import LeetCode.BuildArrayFromPermutation;
import LeetCode.ConcatenationOfArray;
import LeetCode.LeftAndRightSumDifferences;
import LeetCode.ShuffleTheArray;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {10, 4, 8, 3};

        LeftAndRightSumDifferences leftAndRightSumDifferences = new LeftAndRightSumDifferences(nums);

        System.out.println(Arrays.toString(leftAndRightSumDifferences.naive()));
    }

}
