package LeetCode.ArrayAndString;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PascalsTriangle {
    final private int numRows;

    public PascalsTriangle(int numRows) {
        this.numRows = numRows;
    }

    // Time complexity: O(n^2)
    // Space complexity: O(1)
    public List<List<Integer>> naive() {

        List<List<Integer>> result = new ArrayList<>(numRows);

        List<Integer> item1 = new ArrayList<>();

        item1.add(1);

        result.add(item1);

        for (int i = 1; i < numRows; i++) {
            List<Integer> item = new ArrayList<>(i);

            item.add(1);

            for (int j = 1; j <= i - 1; j++) {
                List<Integer> lastItem = result.get(i - 1);

                item.add(lastItem.get(j - 1) + lastItem.get(j));
            }

            item.add(1);

            result.add(item);

        }


        return result;
    }
}
