/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
// TC: O(n)
// SC: O(2n)
var isIsomorphic = function(s, t) {
    const sMap = new Map();
    const tMap = new Map();

    for(let i = 0; i < s.length; i++) {

        if(sMap.has(s[i])) {
            if(sMap.get(s[i]) !== t[i]) {
                return false;
            }
        } else {
            sMap.set(s[i], t[i]);
        }

        if(tMap.has(t[i])) {
            if(tMap.get(t[i]) !== s[i]) {
                return false;
            }
        } else {
            tMap.set(t[i], s[i]);
        }


    };
    

    return true;
}


/*

is isomorphic

s = "egg", t = "add"
output true;

explanation: 
e
{
    e: a,
    g: d
}


1. contraints s.length === t.length
2. use map
3. 0 - 3
4. check s character from the map it's exists value must be the same with t character otherwise return true, 
5. is not exist in the map add to the map s character as a key t character as a value
6 return true

TC: O(n)
SC: O(n)

badc
baba

{
    b: b,
    a: a,
    d: b
}

*/
