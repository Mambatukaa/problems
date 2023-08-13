package AlgoExpert.easy;

import java.util.Arrays;

public class ValidateSubsequence {
    final private int[] array;
    final private int[] sequence;

    public ValidateSubsequence(int[] array, int[] sequence) {
        this.array = array;
        this.sequence = sequence;
    }

    /*
     * Check subsequence array is validate or not
     * Validate subsequence array means sequence elements order same as array
     *  */


    // 1. loop iterate entire array
    // 2.

    // array = {1, 2, 3, 4};
    // sequence = {1, 3, 4};

    public boolean solution() {
        int index = 0;

        for (int item : array) {
            System.out.println(item);
            if (item != sequence[index]) {
                continue;
            }

            index++;
//
            if (index == sequence.length) {
                return true;
            }


        }

        return false;
    }
}
