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


// 1. compare next day temperatures
// 2. if next day's temperature warmer set one
// else compare next warmer day using next days value
//
// Time Complexity: O(n)
// Space Complexity: O(1)
function dailyTemperaturesBest(temperatures: number[]) {
  const answer: number[] = [];
  let hottest: number = 0;


  for(let currDay = temperatures.length - 1; currDay >= 0; currDay--) {
    const currentTemp = temperatures[currDay];

    if(currentTemp >= hottest) {
      hottest = currentTemp;

      answer[currDay] = 0

      continue;
    }

    let days: number = 1;

    while(temperatures[currDay + days] <= currentTemp) {
      days += answer[currDay + days];
    }

    answer[currDay] = days;

  }

  return answer;
}


console.log(dailyTemperaturesBest([73,74,75,71,69,72,76,73]));
