import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] digits = {5, 6, 2, 0, 0, 4, 6, 2, 4, 9};

        PlusOne plusOne = new PlusOne(digits);

        System.out.println(Arrays.toString(plusOne.naive()));


    }

}
