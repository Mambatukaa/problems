/**
 * @param {string} s
 * @return {string}
 */
// Space Complexity: O(n logn)
// Time Complexity: O(n)
var frequencySort = function(s) {
    const strArr = s.split("");
    const map = new Map();

    for(const ch of strArr) {
        map.set(ch, (map.get(ch) || 0) + 1);
    };

    // Time complexity: O(n)
    const sortedMap = new Map([...map.entries()].sort((a, b) => b[1] - a[1]));

    const answer = [];

    for(const [key, value] of sortedMap) {
        answer.push(key.repeat(value));
    };

    console.log(answer)
    
    return answer.join('');
};

const s = "tree"

console.log(frequencySort(s));


/*

s = "tree";

1. 
{
    t: 1,
    r: 1,
    e: 2
}

2. sort the map based on the value

{
    e: 2,
    r: 1,
    t: 1

}

3. declare an answer array or string
4. multiple the k by value
5. push to the array
6. convert array to string and return

// Time Complexity: O(n logn) // sorting
// Space Complexity: O(n)




*/
