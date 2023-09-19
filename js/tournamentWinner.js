
const getWinnerIndex = (idx) => idx === 0 ? 1 : 0; 

// Time Complexity: O(n)
// Space Complexity: O(n)
const tournamentWinner = (compeitions, results) => {
  const map = new Map();

  for(let i = 0; i < competitions.length; i++) {
    const game = competitions[i];
    const winner = game[getWinnerIndex(results[i])];

    if(!map.has(winner)) {
      map.set(winner, 3);
    } else {
      map.set(winner, map.get(winner) + 3);
    }
  }


  let bestScore = 0;
  let winner = '';

  for(let entry of map.entries()) {
    const team = entry[0];
    const teamScore = entry[1];

    if(teamScore > bestScore) {
      bestScore = teamScore;
      winner = team
    }
  }


  return winner;
}

const competitions = [
  ["A", "B"],
  ["B", "C"],
  ["C", "A"]
];

const results = [0,0,1];

console.log(tournamentWinner(competitions, results));


