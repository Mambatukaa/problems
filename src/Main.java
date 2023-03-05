import LeetCode.BuildArrayFromPermutation;
import LeetCode.ConcatenationOfArray;
import LeetCode.ShuffleTheArray;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {1, 3, 2, 4};
        int n = 2;

        ShuffleTheArray shuffleTheArray = new ShuffleTheArray(nums, n);

        System.out.println(Arrays.toString(shuffleTheArray.naiveArraylistSolution()));
    }

}
