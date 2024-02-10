

// how many movements need to take the minBlock to the left and maxBlock to the right
//  s s                     s s                  s s                      s s
// [3,2,1] ====> step => [2,3,1] ===> step ===> [2,1,3] ====> step ====> [1,2,3]
const fn = (blocks) => {
  let minBlockIdx = 0;
  let maxBlockIdx = 0;

  for(let i = 1; i < blocks.length; i++) {
    const curr = blocks[i];
    const minBlock = blocks[minBlockIdx];
    const maxBlock = blocks[maxBlockIdx];

    if(curr > maxBlock) {
      maxBlockIdx = i;
    };

    if(curr < minBlock) {
      minBlockIdx = i;
    };
  };

  let counter = 0;

  // move min element to the left
  for(let i = minBlockIdx; i > 0; i--) {
    [blocks[i], blocks[minBlockIdx]] = [blocks[minBlockIdx], blocks[i]]; 

    counter++;
  };

  // move max element to the left
  for(let i = maxBlockIdx; i < ; i--) {
    [blocks[i], blocks[minBlockIdx]] = [blocks[maxBlockIdx], blocks[i]]; 

    counter++;
  };


};



const blocks = [3,2,1];

fn(blocks)
