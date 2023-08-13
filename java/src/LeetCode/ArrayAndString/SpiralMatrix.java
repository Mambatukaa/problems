package LeetCode.ArrayAndString;

import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    final private int[][] matrix;

    public SpiralMatrix(int[][] matrix) {
        this.matrix = matrix;
    }

    //
    public List<Integer> naive() {
        int rows = matrix.length;
        int columns = matrix[0].length;

        int up = 0;
        int left = 0;

        int right = columns - 1;
        int down = rows - 1;

        ArrayList<Integer> result = new ArrayList<Integer>();

        while (result.size() < rows * columns) {

            // left --> right
            for (int column = left; column <= right; column++) {
                result.add(matrix[up][column]);
            }

            // up --> down (right)
            for (int row = up + 1; row <= down; row++) {
                result.add(matrix[row][right]);
            }

//             left --> right
            // right --> left has already printed
            if (up != down) {
                for (int column = right - 1; column >= left; column--) {
                    result.add(matrix[down][column]);
                }
            }

            // down --> up
            // up --> down has already printed
            if (right != left) {
                for (int row = down - 1; row > up; row--) {
                    result.add(matrix[row][left]);
                }
            }

            left++;
            up++;
            right--;
            down--;
        }

        return result;
    }
}
