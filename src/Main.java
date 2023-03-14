import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 5};

        RemoveDuplicatesFromSortedArr removeDuplicatesFromSortedArr = new RemoveDuplicatesFromSortedArr(nums);

        System.out.println(removeDuplicatesFromSortedArr.solution());
    }

}
