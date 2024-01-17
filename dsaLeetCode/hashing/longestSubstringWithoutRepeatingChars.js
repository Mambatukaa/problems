/**
 * @param {string} s
 * @return {number}
 */
// Time Complexity: O(n)
// Space Complexity: O(n)
var lengthOfLongestSubstring = function(s) {
    const map = new Map();
    let l = 0;
    let answer = 0;

    for(let r = 0; r < s.length; r++) {
        const ch = s[r];

        while(map.get(ch)) {
            map.delete(s[l]);

            l++;
        };

    console.log(map, '-----')

        map.set(ch, 1);

        answer = Math.max(answer, r - l + 1);
    };


    return answer;
    
};

console.log(lengthOfLongestSubstring("pwwkew"))



/*

        r
     l
s = "abcabcbb";
output: 3, "abc"

 {
     a: 1,
     b: 1,
     c: 1,

 }

 slide window

 check string before slide

 shrink window
 while(map.has(ch)) {
     l++;
     map.delete(s[l]);
 };

 map.set(ch, 1);

 answer = max(answer, r - l + 1);

 r++;




a = 1
ab = 2
abc = 3
a <- bca = 3;
ab <- cab = 3;
abc <- abc = 3;
abcab <- cb = 2;
abcabcb <- b = 2;

*/
