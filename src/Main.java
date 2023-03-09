import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] arr = {-2, 0, 10, -19, 4, 6, -8};
//        int[] arr = {10, 2, 5, 3};
//        int[] arr = {0, 0};

// [-2,0,10,-19,4,6,-8]

        CheckNDoubleExist checkNDoubleExist = new CheckNDoubleExist(arr);

        System.out.println(checkNDoubleExist.naive());


    }

}
