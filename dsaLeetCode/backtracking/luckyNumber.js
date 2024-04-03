


const luckyNumber = (x, y, n) => {
// Determine the maximum counts for x and y in the lucky number
    let count_x = Math.min(n / x, 9);  // Maximum count for x is 9 (since it's a single digit)
    let count_y = Math.min((n - count_x * x) / y, 9);  // Maximum count for y
    
    // Construct the lucky number
    let luckyNumber = x.toString().repeat(count_x) + y.toString().repeat(count_y);
    return luckyNumber;

};

const x = 3;
const y = 4;

// 777777 = 42 

console.log(luckyNumber(x, y, 13));
