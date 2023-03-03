import AlgoExpert.array.TwoNumberSum1;
import AlgoExpert.easy.SortedSquaredArray;
import AlgoExpert.easy.TournamentWinner;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] array = {3, 5, 1};
        int target = 6;

        TwoNumberSum1 twoNumberSum1 = new TwoNumberSum1(array, target);


        System.out.println(Arrays.toString(twoNumberSum1.solution()));

    }

}
