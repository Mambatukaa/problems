import LeetCode.BuildArrayFromPermutation;
import LeetCode.ConcatenationOfArray;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {1, 3};

        ConcatenationOfArray concatenationOfArray = new ConcatenationOfArray(nums);

        System.out.println(Arrays.toString(concatenationOfArray.solution()));

    }

}
