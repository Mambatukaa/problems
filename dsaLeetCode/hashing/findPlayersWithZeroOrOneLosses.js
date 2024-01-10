// Time Complexity: O(n * logn)
// Space Complexity: O(n)
const findWinners = (matches) => {
  const totalMatches = new Map();
  const totalWins = new Map();

  for(const [winner, loser] of matches) {
      totalMatches.set(winner, (totalMatches.get(winner) || 0) + 1);
      totalMatches.set(loser, (totalMatches.get(loser) || 0) + 1);

      totalWins.set(winner, (totalWins.get(winner) || 0) + 1);
  };

  const answer = [[],[]];
  const sortedMatches = new Map([...totalMatches.entries()].sort((a,b) => a[0] - b[0]));

  for(const [key, matches] of sortedMatches) {
      const totalWin = totalWins.get(key) || 0;

      // no lost
      if(matches === totalWin) {
          answer[0].push(key);
      } else if (matches - 1 === totalWin) {
          answer[1].push(key);
      }
  };

  return answer;

};

// Time Complexity: O(n + k) matches iteration + lossesCount iteration
// Space Complexity: O(k); k all players
// array
const findWinnersII = (matches) => {
  const lossesCount = new Array(Math.pow(10, 5) + 1).fill(-1);

  for(const [winner, loser] of matches) {
    if(lossesCount[winner] === -1) {
      lossesCount[winner] = 0;
    };

    if(lossesCount[loser] === -1) {
      lossesCount[loser] = 1;
    } else {
      lossesCount[loser]++;
    };
  };

  const answer = [[],[]];

  for(let i = 0; i < lossesCount.length; i++) {
    if(lossesCount[i] === 0) {
      answer[0].push(i);
    } else if(lossesCount[i] === 1) {
      answer[1].push(i);
    }
  };


  return answer;
};

const matches = [[3,4], [2,4], [1,3], [2,3], [5,6]];

console.log(findWinnersII(matches));
