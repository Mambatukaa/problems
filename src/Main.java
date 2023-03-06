import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] candies = {2, 3, 5, 1, 3};

        KidsWithGreatestNumCandies kidsWithGreatestNumCandies = new KidsWithGreatestNumCandies(candies, 3);

        System.out.println(kidsWithGreatestNumCandies.naive());
    }

}
