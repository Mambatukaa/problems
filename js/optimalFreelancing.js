// Space complexity: O(n);
// Time complexity: O(nlog*n);
const optimalFreelancing = (jobs) => {
  const LENGTH_OF_WEEK = 7;

  const answer = new Array(LENGTH_OF_WEEK);

  jobs.sort((a,b) => b.payment - a.payment)

  for(let i = 0; i < jobs.length; i++) { 
    let deadline = jobs[i].deadline;
    const payment = jobs[i].payment;

    if(deadline > LENGTH_OF_WEEK) {
      deadline = LENGTH_OF_WEEK;
    }

    while(deadline > 0) {
      if(!answer[deadline]) {
        answer[deadline] = payment

        break;
      }

      deadline--;
    }
  }

  console.log(answer)

  let income = 0;

  for(const payment of answer) {
    if(!payment) {
      continue;
    }

    income += payment;
  }

  return income;
}

const jobs = [
  {deadline: 1, payment: 1},
  {deadline: 2, payment: 1},
  {deadline: 3, payment: 1},
  {deadline: 4, payment: 1},
  {deadline: 5, payment: 1},
  {deadline: 6, payment: 1},
  {deadline: 7, payment: 1},
  {deadline: 8, payment: 1},
  {deadline: 9, payment: 1},
  {deadline: 10, payment: 1},
];

console.log(optimalFreelancing(jobs));
