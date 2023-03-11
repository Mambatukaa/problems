import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] arr = {3, 6, 5, 6, 7, 6, 5, 3, 0};

        ValidMountainArray validMountainArray = new ValidMountainArray(arr);

        System.out.println(validMountainArray.solution());
    }

}
