import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {-4, -1, 0, 3, 10};

        SquaresOfSortedArray squaresOfSortedArray = new SquaresOfSortedArray(nums);

        System.out.println(Arrays.toString(squaresOfSortedArray.solution()));

    }

}
