/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(n)
var numSubarraysWithSum = function(nums, goal) {
    const map = new Map();
    map.set(0, 1);

    let answer = 0;
    let prefix = 0;

    for(const num of nums) {
        console.log(map, 'hahahaha')
        prefix += num;

        const diff = prefix - goal;

        if(map.has(diff)) {
            answer += map.get(diff);
        };

        map.set(prefix, (map.get(prefix) || 0) + 1);
    }

    return answer;
};


/*
  nums = [1,0,1,0,1]; goal = 2;
  Output: 4

  [[1,0,1],0,1];
  [[1,0,1,0],1];
  [1, [0,1,0,1] ];
  [1,0, [1,0,1] ];


              r
          l
  nums = [1,0,1,0,1]
          0 1 2 3 4

              x
    l 0 0 0 0 0 
    r 0 1 2 3 4
    c 1 0 2 2 3

    currSum = 1 => 1 => 2 => 2 => 3

    1 - 2 = -1 X
    1 - 2 = -1 X
    2 - 2 = 0 > => answer += 1;
    2 - 2 = 0 > => answer+= 1
    3 - 2 = 1 > => answer+=2 
    
    {
        0: 1,
        1: 2,
        2: 2
        3: 1
    }


    [0, 0, 0, 0, 0];

    0 - 0 => 0 answer+=1
    0 - 0 => 0 answer+=2
    0 - 0 => 0 answer+=3
    0 - 0 => 0 answer+=4
    0 - 0 => 0 answer+=5






    {
        0:3
    }
 */
