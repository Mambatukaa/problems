


const luckyNumber = (x, y, n) => {
  const temp = x;
  x = Math.max(x, y);
  y = Math.min(y, temp);

  const arr = [];
  let sum = 0;

  while(sum <= n - y) {
    arr.push(y);
    sum += y;
  };

  if(sum === n) {
    return arr;
  };


  for(let i = 0; i < arr.length; i++) {
    console.log(i, 'hahahha')
    if(sum - y + x === n) {
      arr[i] = x;
      return arr;
    }

    if(sum - y + x > n) {
      continue;
    };

    arr[i] = x;
    sum = sum - y + x;
  };

};

const x = 7;
const y = 4;

// 777777 = 42 

console.log(luckyNumber(x, y, 14));
