package AlgoExpert.easy;

import java.util.Arrays;
import java.util.HashMap;

public class TournamentWinner {
    private final String[][] competitions;
    private final int[] results;

    public TournamentWinner(String[][] competitions, int[] results) {
        this.competitions = competitions;
        this.results = results;
    }

    /*
        String[][] competitions = {
                {"1", "2"},
                {"2", "3"},
                {"1", "3"},
        };

        int[] results = {0, 0, 0};
    */

    // results = {0, 0, 1};
    // {Home, Away}
    // 0 means Away won, 1 means Home won.
    // Won get 3 score. Lose get 0 score.

    public String solution() {
        System.out.println(Arrays.deepToString(competitions));
        System.out.println(Arrays.toString(results));

        String bestTeam = "";
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        map.put(bestTeam, 0);


        for (int i = 0; i < competitions.length; i++) {
            int result = results[i] == 0 ? 1 : 0;
            String winningTeam = competitions[i][result];

            updateScore(map, winningTeam);

            if (map.get(winningTeam) > map.get(bestTeam)) {
                bestTeam = winningTeam;
            }

        }

        System.out.println(map);

        return bestTeam;
    }


    private static void updateScore(HashMap<String, Integer> map, String winningTeam) {

        if (!map.containsKey(winningTeam)) {
            map.put(winningTeam, 3);
        } else {
            Integer score = map.get(winningTeam);
            map.put(winningTeam, score + 3);

        }

    }

}
