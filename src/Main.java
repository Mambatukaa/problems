import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {0, 0, 0, 0, 1, 1};

        MaxConesecutiveOnesII maxConesecutiveOnesII = new MaxConesecutiveOnesII(nums);

        System.out.println(maxConesecutiveOnesII.naive());
    }

}
