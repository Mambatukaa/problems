import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {-4, 3, 4, 5};

        SquaresOfSortedArray squaresOfSortedArray = new SquaresOfSortedArray(nums);

        System.out.println(Arrays.toString(squaresOfSortedArray.naive()));

    }

}
