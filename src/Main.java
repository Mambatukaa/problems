import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {1, 0, 1, 1, 0, 1, 1, 1, 1};

        MaxConsecutiveOnes maxConsecutiveOnes = new MaxConsecutiveOnes(nums);

        System.out.println(maxConsecutiveOnes.naive());

    }

}
