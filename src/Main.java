import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] encoded = {6, 2, 7, 3};
        int first = 4;

        DecodeXorArray decodeXorArray = new DecodeXorArray(encoded, first);

        System.out.println(Arrays.toString(decodeXorArray.naive()));

    }

}
