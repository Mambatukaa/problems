import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};

        FindAllNumbersDisappeared findAllNumbersDisappeared = new FindAllNumbersDisappeared(nums);

        System.out.println(findAllNumbersDisappeared.solution());
    }

}
