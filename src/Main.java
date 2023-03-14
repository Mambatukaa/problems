import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] arr = {17, 18, 5, 4, 6, 1};

        ReplaceWithGreatestRightSide replaceWithGreatestRightSide = new ReplaceWithGreatestRightSide(arr);

        System.out.println(Arrays.toString(replaceWithGreatestRightSide.naive()));
    }

}
