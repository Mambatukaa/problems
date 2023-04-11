package LeetCode.Array;

import java.util.Arrays;

public class DuplicateZeros {
    final private int[] arr;

    public DuplicateZeros(int[] arr) {
        this.arr = arr;
    }


    private void shift(int[] arr, int index) {
        for (int i = arr.length - 1; i > index; i--) {
            arr[i] = arr[i - 1];
        }

    }

    // Time complexity:
    // Space complexity:

    public int[] naive() {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) {
                shift(arr, i);
                i++;
            }
        }

        return arr;
    }


}
