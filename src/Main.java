import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {2, 1};

        MoveZeroes moveZeroes = new MoveZeroes(nums);

        System.out.println(Arrays.toString(moveZeroes.naive()));
    }

}
