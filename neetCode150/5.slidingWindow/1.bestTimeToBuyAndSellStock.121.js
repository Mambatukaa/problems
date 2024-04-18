/**
 * @param {number[]} prices
 * @return {number}
 */
// Time Complexity: O(n)
// Space Complexity: O(1)
// 10 minutes
var maxProfit = function(prices) {
  let left = 0;
  let profit = 0;

  for(let right = 0; right < prices.length; right++) {
    // buy cheaper stock 
    if(prices[left] > prices[right]) {
      left = right;
    };

    profit = Math.max(profit, prices[right] - prices[left]);
  };
    
  return profit;
};

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfitII = function(prices) {
  let left = 0;
  let profit = 0;

  for(let right = 0; right < prices.length; right++) {
    // buy cheaper stock 
    while(prices[left] > prices[right]) {
      left++;
    };

    profit = Math.max(profit, prices[right] - prices[left]);
  };
    
  return profit;
};




/*

to find best time to buy and sell is BUY WHEN STOCK IS CHEAPER SALE IT WHEN EXPENSIVE

1. Buy stock when cheaper
2. Try to sell when stock expensive.

track current min price

check next value is expensive it's expensive


    l
       r
[2, 1, 2, 1, 0, 1, 2]

*/




/*

to find best time to buy and sell is BUY WHEN STOCK IS CHEAPER SALE IT WHEN EXPENSIVE

1. Buy stock when cheaper
2. Try to sell when stock expensive.

track current min price

check next value is expensive it's expensive


    l
       r
[2, 1, 2, 1, 0, 1, 2]

*/
