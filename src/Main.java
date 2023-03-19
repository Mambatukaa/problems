import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {3, 4, 0, 0, 0, 0};

        SortArrayByPriority sortArrayByPriority = new SortArrayByPriority(nums);


        System.out.println(Arrays.toString(sortArrayByPriority.naive()));
    }

}
