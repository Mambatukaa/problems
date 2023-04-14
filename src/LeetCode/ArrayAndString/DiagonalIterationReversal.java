package LeetCode.ArrayAndString;

import java.util.ArrayList;
import java.util.Collections;

public class DiagonalIterationReversal {
    final private int[][] mat;

    public DiagonalIterationReversal(int[][] mat) {
        this.mat = mat;
    }

    // Space complexity: O(n)
    // Time complexity: O(n^2)
    public int[] naive() {
        // Check for empty matrices
        if (mat == null || mat.length == 0) {
            return new int[0];
        }

        int m = mat[0].length;
        int n = mat.length;

        int[] result = new int[m * n];

        // result index tracker
        int k = 0;

        ArrayList<Integer> intermediate = new ArrayList<Integer>();

        for (int d = 0; d < n + m - 1; d++) {
            intermediate.clear();

            int row = d < m ? 0 : d - m + 1;
            int column = d < m ? d : m - 1;

            while (row < n && column > -1) {
                intermediate.add(mat[row][column]);

                row++;
                column--;
            }

            // reverse even numbered diagonals
            if (d % 2 == 0) {
                Collections.reverse(intermediate);
            }

            for (int num : intermediate) {
                result[k++] = num;
            }
        }

        return result;
    }
}

