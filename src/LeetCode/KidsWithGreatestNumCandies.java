package LeetCode;

import java.util.ArrayList;
import java.util.List;

// 1432
public class KidsWithGreatestNumCandies {
    final private int[] candies;
    final private int extraCandies;

    public KidsWithGreatestNumCandies(int[] candies, int extraCandies) {
        this.candies = candies;
        this.extraCandies = extraCandies;
    }

    // Space complexity: O(n)
    // Time complexity: O(2n) ~ O(n): remove constant
    public List<Boolean> naive() {
        int max = Integer.MIN_VALUE;

        for (int candy : candies) {
            if (max < candy) {
                max = candy;
            }
        }

        List<Boolean> res = new ArrayList<>();

        for (int candy : candies) {
            res.add(candy + extraCandies >= max);
        }

        return res;
    }
}
