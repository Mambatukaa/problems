import LeetCode.BuildArrayFromPermutation;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {0, 2, 1, 5, 3, 4};

        BuildArrayFromPermutation buildArrayFromPermutation = new BuildArrayFromPermutation(nums);

        System.out.println(Arrays.toString(buildArrayFromPermutation.solution()));

    }

}
