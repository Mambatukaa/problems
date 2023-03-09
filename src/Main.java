import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] arr = {1, 0, 2, 3, 0, 4, 5, 0};

        DuplicateZeros duplicateZeros = new DuplicateZeros(arr);

        System.out.println(Arrays.toString(duplicateZeros.naive()));

    }

}
