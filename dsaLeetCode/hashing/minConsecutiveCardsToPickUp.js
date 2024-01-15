// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (cards) => {
  const map = new Map();
  let answer = Infinity;

  for(let i = 0; i < cards.length; i++) {
    answer = Math.min(answer, ((i - map.get(cards[i])) || Infinity) + 1);

    map.set(cards[i], i);
  };

  return answer === Infinity ? - 1: answer;
};

const cards = [3,4,2,3,4,7];

console.log(fn(cards));
