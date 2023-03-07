import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {12, 3331, 551};

        FindEvenNumbersDigit findEvenNumbersDigit = new FindEvenNumbersDigit(nums);

        System.out.println(findEvenNumbersDigit.naive());

    }

}
