import LeetCode.ArrayAndString.DiagonalIterationReversal;
import LeetCode.ArrayAndString.LongestCommonPrefix;
import LeetCode.ArrayAndString.SpiralMatrix;
import LeetCode.ArrayAndString.StrStr;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

        SpiralMatrix spiralMatrix = new SpiralMatrix(matrix);

        System.out.println(spiralMatrix.naive());
    }

}
