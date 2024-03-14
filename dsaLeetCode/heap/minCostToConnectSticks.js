/**
 * @param {number[]} sticks
 * @return {number}
 */
// Time Complexity: O(n * log n)
// Space Complexity: O(n)
var connectSticks = function(sticks) {
    const minHeap = new MinPriorityQueue();
    
    for(const stick of sticks) {
        // add stick to heap
        minHeap.enqueue(stick);
    };
    
    let totalCost = 0;
    
    while(minHeap.size() > 1) {
        const firstMin = minHeap.dequeue().element;
        const secondMin = minHeap.dequeue().element;
        
        const sum = firstMin + secondMin;
        totalCost += sum;
        
        minHeap.enqueue(sum);
    };
    
    return totalCost;
};

/*

  TO COST MIN CALCULATE MIN TWO STICKS


    get 2 min values from sticks and add sum to sticks. Update totalCost
        repeat the above method until sticks left one element
    the reason why adding two min elements is make cost minimum
    
    to get 2 min values from array. It takes sort + array deletion TC: O(n) ====> n times O(n^2)
        to reduce complexity use minHeap; TC: O(log n) ===> n times TC: O(n * log n)
        
        

*/
