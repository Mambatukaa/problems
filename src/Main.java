import LeetCode.ArrayAndString.DiagonalIterationReversal;
import LeetCode.ArrayAndString.LongestCommonPrefix;
import LeetCode.ArrayAndString.StrStr;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[][] mat = {{2, 3}};

        DiagonalIterationReversal diagonalIterationReversal = new DiagonalIterationReversal(mat);

        System.out.println(Arrays.toString(diagonalIterationReversal.solution()));
    }

}
