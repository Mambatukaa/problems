
const getWinnerIndex = (idx) => idx === 0 ? 1 : 0; 

// Time Complexity: O(n) n is competitions
// Space Complexity: O(k) k is teams
const tournamentWinner = (compeitions, results) => {
  const map = new Map();
  let bestTeam = '';
  map.set('bestTeam', 0);

  for(let i = 0; i < competitions.length; i++) {
    const game = competitions[i];
    const winner = game[getWinnerIndex(results[i])];

    if(!map.has(winner)) {
      map.set(winner, 3);
    } else {
      map.set(winner, map.get(winner) + 3);
    }

    const bestTeamScore = map.get('bestTeam');
    const winnerScore = map.get(winner);


    if(bestTeamScore < winnerScore) {
      bestTeam = winner;

      map.set('bestTeam', winnerScore);
    }

    console.log(map)
  }

  return bestTeam;
}

const competitions = [
  ["A", "B"],
  ["B", "C"],
  ["C", "A"]
];

const results = [0,0,1];

console.log(tournamentWinner(competitions, results));


