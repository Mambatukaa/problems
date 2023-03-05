import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {1, 1, 2, 2};

        NumberOfGoodPairs numberOfGoodPairs = new NumberOfGoodPairs(nums);

        System.out.println(numberOfGoodPairs.naive());
    }

}
