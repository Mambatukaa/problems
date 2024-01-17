/**
 * @param {string[][]} paths
 * @return {string}
 */
// Time Complexity: O(n)
// Space Complexity: O(n)
var destCity = function(paths) {
    const map = new Map();

    for(const path of paths) {
        map.set(path[0], 1);

        if(!map.has(path[1])) {
            map.set(path[1], 0);
        };
    };
    
    console.log(map, 'hahahaha')

    for(const [key, value] of map) {
        if(value === 0) {
            return key;
        }
    };
}


/*
paths = [ [a,b], [b, c], [c,d]]

paths = [ [c,d], [b, c], [a,b] ]

{
    a: 1,
    b: 1,
    c: 1,
    d: 0
}

return key which has 0 value;

1 destination city

TC: O(n) 2 elements in the item
SC: O(n) store all elements in the map

*/
