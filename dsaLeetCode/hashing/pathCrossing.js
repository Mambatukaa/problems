/**
 * @param {string} path
 * @return {boolean}
 */


 /*


N = cord[1]++
E = cord[0]++;
S = cord[0]--;
W = cord[1]--;
 */
// Time Complexity: O(n)
// Space Complexity: O(n)
var isPathCrossing = function(path) {
    let y = 0; // north south
    let x = 0; // east west

    const visited = new Set();
    visited.add("0,0");

    for(const dir of path) {
        switch(dir) {
            case 'N':
                y--;
                break;
            case 'S':
                y++;
                break;
            case 'E':
                x--;
                break;
            // W
            default:
                x++;
        }

        const currentPos = `${x},${y}`;

        console.log(visited, '------', currentPos);

        if(visited.has(currentPos)) {
            return true;
        };

        visited.add(currentPos);
    };

    return false;
    
};

console.log(isPathCrossing("NNSWWEWSSESSWENNW"));


/*

path = "NES";
[0,0]
N = [0, 1]
E = [1, 1]
S = [0, 1]

Str   End
,     ,
,     ,
> , , ^ 


cord = [0, 0]

N = cord[1]++
E = cord[0]++;
S = cord[0]--;
W = cord[1]--;


path = 'NESWW"
cord = [0, 0]

N = [0, 1]
E = [1, 1]
S = [0, 1]
W = [0, 0]

true;

TC: O(n)
SC: O(1)


S---- ---- ----
|              |
|              |
|              |
 ---- ---- ----
            


*/


