package AlgoExpert.easy;

import java.lang.reflect.Array;
import java.util.Arrays;

public class SortedSquaredArray {
    final private int[] array;

    public SortedSquaredArray(int[] array) {
        this.array = array;
    }

    // Space complexity O(n), TC O(n)
    public int[] solution() {
        int[] subArray = new int[array.length];
        int leftIndex = 0;
        int rightIndex = array.length - 1;


        for (int i = array.length - 1; i >= 0; i--) {
            int leftItem = array[leftIndex];
            int rightItem = array[rightIndex];

            if (Math.abs(leftItem) < Math.abs(rightItem)) {
                subArray[i] = rightItem * rightItem;
                rightIndex--;
            } else {
                subArray[i] = leftItem * leftItem;
                leftIndex++;
            }
        }

        return subArray;
    }


}
