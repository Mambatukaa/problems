function last(arr: number[]) {
  return arr[arr.length - 1];
}

// 30,40,50
// stack = []
// answer = []

// Space Complexity: O(n)
// Time Complexity: O(n)
function dailyTemperatures(temperatures: number[]) {
  const stack: number[] = [];
  const answer = new Array(6);

  for(let currDay = 0; currDay < temperatures.length; currDay++) {
    const currTemp = temperatures[currDay];

    while(stack.length && currTemp > temperatures[last(stack)]) {
      const prevDay = stack.pop() || 0;

      answer[prevDay] = currDay - prevDay;
    }


    stack.push(currDay);
  }

  if(stack.length) {
    for(let i of stack) {
      answer[i] = 0;
    }
  }

  return answer;
}


console.log(dailyTemperatures([73,74,75,71,69,72,76,73]));
