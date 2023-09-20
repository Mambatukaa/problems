
const getWinnerIndex = (idx) => idx === 0 ? 1 : 0; 
const updateScore = (winner, scores) => {
    if(!scores.has(winner)) {
      scores.set(winner, 0);
    } 

    scores.set(winner, scores.get(winner) + 3);
}

// Time Complexity: O(n) n is competitions
// Space Complexity: O(k) k is teams
const tournamentWinner = (compeitions, results) => {
  const scores = new Map();
  scores.set('bestTeam', 0);
  let bestTeam = '';

  for(let i = 0; i < competitions.length; i++) {
    const game = competitions[i];
    const winner = game[getWinnerIndex(results[i])];

    updateScore(winner, scores);

    const bestTeamScore = scores.get('bestTeam');
    const winnerScore = scores.get(winner);


    if(bestTeamScore < winnerScore) {
      bestTeam = winner;

      scores.set('bestTeam', winnerScore);
    }
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


