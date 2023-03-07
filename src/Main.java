import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {8, 1, 2, 2, 3};

        SmallerThanCurrentNums smallerThanCurrentNums = new SmallerThanCurrentNums(nums);

        System.out.println(Arrays.toString(smallerThanCurrentNums.mapSolution()));
    }

}
