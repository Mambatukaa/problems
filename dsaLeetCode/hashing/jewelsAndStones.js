/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
// Space Complexity: O(n)
// Time Complexity: O(n + m)
var numJewelsInStones = function(jewels, stones) {
    const map = new Map();

    for(const ch of stones) {
        map.set(ch, (map.get(ch) || 0) + 1);
    };

    let answer = 0;

    for(const ch of jewels) {
        if(map.has(ch)) {
            answer += map.get(ch); 
        }

    };

    return answer;
};


/*

jewels = "aA";
stones = "aAAbbbb";

stones = {
    a: 1,
    A: 2,
    b: 4
};

jewels = {
    a: 1,
    A
};

*/
