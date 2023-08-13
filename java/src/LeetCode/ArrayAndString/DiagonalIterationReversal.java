package LeetCode.ArrayAndString;

import java.util.ArrayList;
import java.util.Collections;

public class DiagonalIterationReversal {
    final private int[][] matrix;

    public DiagonalIterationReversal(int[][] matrix) {
        this.matrix = matrix;
    }

    // Space complexity: O(n)
    // Time complexity: O(n^2)
    public int[] naive() {
        // Check for empty matrices
        if (matrix == null || matrix.length == 0) {
            return new int[0];
        }

        int m = matrix[0].length;
        int n = matrix.length;

        int[] result = new int[m * n];

        // result index tracker
        int k = 0;

        ArrayList<Integer> intermediate = new ArrayList<Integer>();

        for (int d = 0; d < n + m - 1; d++) {
            intermediate.clear();

            int row = d < m ? 0 : d - m + 1;
            int column = d < m ? d : m - 1;

            while (row < n && column > -1) {
                intermediate.add(matrix[row][column]);

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

    // Space complexity: O(1)
    // Time complexity: O(n*m)
    public int[] solution() {
        int column = 0;
        int row = 0;

        int n = matrix.length;
        int m = matrix[0].length;

        System.out.println(n + " m " + m);

        // upward going
        int direction = 1;

        int[] result = new int[n * m];
        int i = 0;

        while (row < n && column < m) {
            System.out.println(direction);
            System.out.println(row + " " + column);

            result[i++] = matrix[row][column];

            int new_row = row + (direction == 1 ? -1 : 1);
            int new_column = column + (direction == 1 ? 1 : -1);

            // if it's true out of bounds
            if (new_row < 0 || new_row == n || new_column < 0 || new_column == m) {
                if (direction == 1) {
                    row += (column == m - 1 ? 1 : 0);
                    column += (column < m - 1 ? 1 : 0);
                } else {
                    column += (row == n - 1 ? 1 : 0);
                    row += (row < n - 1 ? 1 : 0);
                }

                direction = 1 - direction;
            } else {
                row = new_row;
                column = new_column;
            }

        }


        return result;
    }
}

