/**
 * @param {number[]} nums
 * @return {boolean}
 */
// Time Complexity: O(n)
// Space Complexity: O(n)
var containsDuplicate = function(nums) {
    const seen = new Set();

    for(const num of nums) {
        if(seen.has(num)) {
            return true;
        }

        seen.add(num);
    }
    
    return false;
};
