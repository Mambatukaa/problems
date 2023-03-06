import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 1, 1};

        RunningSumOfArray runningSumOfArray = new RunningSumOfArray(nums);

        System.out.println(Arrays.toString(runningSumOfArray.solution()));
    }

}
