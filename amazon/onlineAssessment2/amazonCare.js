
// Time Complexity: O(k)
// Space Complexity: O(k)
const amazonCare = (n, days, k) => {
  let curr = 0;
  let max = 0;

  const scores = [];

  // convert days to scores
  for(const day of days) {
    for(let i = 1; i <= day; i++) {
      scores.push(i);
    };
  };

  const s = scores.length;

  // sliding window
  let left = 0;
  let right = 0;
  let windowSize = 1;

    console.log(scores)

  while(left <= s - 1) {
    curr += scores[right];

    // shrink the window
    while(windowSize >= k) {
      max = Math.max(max, curr);

      curr -= scores[left];

      left++;
      windowSize--;
    };

    // slide window
    windowSize++;
    right++;

    if(right >= s) {
      right %= s;
    };
  };

  return max;
};

const n = 5;

const days = [7, 4, 6, 3, 5]

const k = 8;

console.log(amazonCare(n, days, k))

/*


n = 3;

days = [2, 3, 2];

k = 4;


Employee wants to complete the tasks in k days.


days[i] = 1 -> i points;

days = [2, 3, 2];

                      1    2  3  4 => 8
                              1  2    3  4 => 8          
daysWithPoints = [[1, 2], [1, 2, 3], [1, 2]];

********************************************************************

n = 5;

days = [7, 4, 6, 3, 5]

k = 8;


k =     2  3  4  5  6  7  8   => 33                                                     1
days [ [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5]];



k = 8;
        
        L
                             R
days = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 3, 4, 5];


Find the k length subarray that sum is maximum;

if k reaches the end start from first element


when left pointer reaches the end break;
 
 */
